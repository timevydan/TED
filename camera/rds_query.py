import psycopg2
import os
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

def connect():
    conn = None
    try:
        print('connecting to the RDS database...')
        print(os.environ.get('DB_HOST'), os.environ.get('DB_NAME'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'))
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
            try:
                os.mkdir(dir)
            except:
                pass

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
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    connect()
