import psycopg2
import os
import requests


def connect():
    """Retrieve images from the program database on RDS.

    Builds top level directory based on the list of names of known faces,
    then retrieves the urls for each associated image to that name and
    creates .png files locally for facial recoginition training.
    """
    
    conn = None

    try:
        print('connecting to the RDS database...')
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD')
        )

        cur = conn.cursor()
        print('Postgres db version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        cur.execute('SELECT * FROM ted_face;')
        rows = cur.fetchall()
        people = {}
        for row in rows:
            people[row[0]] = row[1]
            dir = './images/' + row[1]
            os.mkdir(dir)

        cur.execute('select * from ted_face inner join ted_picture on ted_face.id=ted_picture.face_id;')
        row2 = cur.fetchall()
        list = []
        counter = 0
        for i in row2:
            counter += 1
            url = i[3]
            r = requests.get(url, allow_redirects=True)

            open('./images/' + i[1] + '/' + str(counter) + '.png', 'wb').write(r.content)

            list.append((i[1], i[3]))

        print(list)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')


if __name__ == "__main__":
    connect()
