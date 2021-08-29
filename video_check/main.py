import os
from collections import defaultdict
from typing import Any, Dict, List, Tuple

import cv2
import psycopg2
from config import config

############################################
from detect_missing_people import FaceRecog
############################################

PATH = '../media/'


class VideoCheck:
    def __init__(self) -> None:
        self.conn = self.connect()

    def connect(self) -> object:
        conn = None
        try:
            params = config()

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

    def get_binary_array(self, path: str) -> str:
        with open(path, "rb") as image:
            f = image.read()
            b = bytes(f).hex()
            return b

    def upload_missing_poeple_date(self, data_list: Dict[int, List[Tuple[str, str, str, int]]]):
        cur = self.conn.cursor()
        sql = "INSERT INTO accounts_imagesfromvideo(name, photo, date, user_id, missing_person_id) VALUES (%s, %s, %s, %s, %s)"
        mylist = []
        for missing_person_id, value in data_list.items():
            for name, image, date, user_id in value:
                mylist.append((name, image, date, user_id, missing_person_id))

        try:
            cur.executemany(sql, mylist)
            self.conn.commit()
            print("%d records inserted succeessully." %cur.rowcount)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    
    def disconnect(self) -> None:
        self.conn.close()
    
    def fetch_all_missing_people_data(self) -> Tuple[Dict[int, Tuple[str, str, int]], Dict[Any, Any]]:
        global PATH
        cur = self.conn.cursor()
        cur.execute("SELECT * from listings_listing")
        records = cur.fetchall()

        missing_people = {}
        missing_people_state = {}

        for record in records:
            _id = record[0]
            name = record[1]
            image_path = record[6]
            requestor_id = record[12]
            is_found = record[13]

            if is_found:
                continue

            missing_people[_id] = (name, PATH + image_path, requestor_id)
            missing_people_state[_id] = is_found

        return missing_people, missing_people_state


def save_images(images: Dict[int, List[Tuple[Any, ...]]], missing_people_data: Dict[int, Tuple[str, str, int]] ) -> Dict[int, List[Tuple[str, str, str, int]]]:
    global PATH
    sql_values = defaultdict(list)
    PATH += 'taken_photos/'
    for _id, images_info in images.items():
        for image, date in images_info:
            _path = PATH + date[:10] + '/' 
            os.makedirs(_path, exist_ok=True)
            _path += str(_id) + '.jpg'
            cv2.imwrite(_path, image)    
            sql_values[_id].append((missing_people_data[_id][0], _path, date, missing_people_data[_id][2]))

    return sql_values


if __name__ == '__main__':
    video_check = VideoCheck()

    missing_people_data, missing_people_state = video_check.fetch_all_missing_people_data()
    face = FaceRecog(missing_people_state)

    missing_people_images_from_videos = face.start_face_recog(missing_people_data, show=False)
    sql_values = save_images(missing_people_images_from_videos, missing_people_data)
    video_check.upload_missing_poeple_date(sql_values)

    video_check.disconnect()
