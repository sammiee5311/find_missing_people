import cv2
import numpy as np
import face_recognition
from glob import glob
from datetime import datetime
from typing import List, Dict
from collections import defaultdict


class FaceRecog:
    def __init__(self, missing_people_state: Dict[str, bool]) -> None:
        self.missing_people_images = []
        self.missing_people_state = missing_people_state
        self.missing_people_ids = []
        self.missing_people_images_from_videos = defaultdict(list)

    def find_face_encodings(self) -> List[str]:
        encodings_list = []
        for img in self.missing_people_images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodings_list.append(face_recognition.face_encodings(img)[0])

        return encodings_list

    def start_face_recog(self, missing_people: Dict[str, tuple]) -> Dict[int, tuple]:
        for person_id, person_info in missing_people.items():
            person_image = cv2.imread(person_info[1])
            self.missing_people_images.append(person_image)
            self.missing_people_ids.append(person_id)

        encode_known = self.find_face_encodings()
        print('Encoding Complete')

        return self.video_capture(encode_known)
    
    def video_capture(self, encode_known: List[str]) -> None:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            success, img = cap.read()
            resized_img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

            cur_locations = face_recognition.face_locations(resized_img)
            cur_encodings = face_recognition.face_encodings(resized_img, cur_locations)

            for encodings_face, location in zip(cur_encodings, cur_locations):
                check = face_recognition.compare_faces(encode_known, encodings_face)
                face_distance = face_recognition.face_distance(encode_known, encodings_face)
                matched_idx = np.argmin(face_distance)

                missing_person_id = self.missing_people_ids[matched_idx]

                top, right, bottom, left = location
                top, right, bottom, left = 4 * top, 4 * right, 4 * bottom, 4 * left

                now = datetime.now()
                date_string = now.strftime('%Y-%m-%d %H:%M:%S')
                self.missing_people_images_from_videos[missing_person_id].append(cv2.resize(img, (0,0), None, 0.5, 0.5), date_string)

                '''
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                '''

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                cv2.imshow('img', img)
                cv2.waitKey(1)

        cv2.destroyAllWindows()