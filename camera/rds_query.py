import requests
import psycopg2
import os

# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Macaca_sinica_-_01.jpg/220px-Macaca_sinica_-_01.jpg"
# r = requests.get(url, allow_redirects=True)
# open('filename.png', 'wb').write(r.content)


def connect():
    try:
        print('connecting to the RDS database...')
        conn = psycopg2.connect(host=os.environ.get('DB_HOST'), database=os.environ.get('DB_NAME'), user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASSWORD') )
        cur = conn.cursor()

        print('Postgres db version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')

if __name__ == "__main__":
    connect()