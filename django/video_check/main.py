import psycopg2
from config import Config

class VideoCheck:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        conn = None
        try:
            params = Config()

            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            
            cur = conn.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            return conn

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            
        finally:
            if conn is not None:
                print('Database connected successfully.')
    
    def fetch_all_missing_people_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from listings_listing")
        records = cur.fetchall()

        missing_people = {}

        for record in records:
            _id = record[0]
            name = record[1]
            image_path = record[6]
            requestor_id = record[12]
            is_found = record[13]

            if is_found:
                continue

            missing_people[_id] = (name, image_path, requestor_id)

        return missing_people


if __name__ == '__main__':
    video_check = VideoCheck()
    missing_people_data = video_check.fetch_all_missing_people_data()
    print(missing_people_data)
    video_check.conn.close()