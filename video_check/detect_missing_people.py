import cv2
import numpy as np
import face_recognition
from glob import glob
from datetime import datetime
from typing import List, Dict, Any, Tuple
from collections import defaultdict


class FaceRecog:
    def __init__(self, missing_people_state: Dict[str, bool]) -> None:
        self.missing_people_images: List[Any] = []
        self.missing_people_state = missing_people_state
        self.missing_people_ids: List[int] = []
        self.missing_people_images_from_videos: Dict[int, List[Tuple[Any, ...]]] = defaultdict(list)

    def find_face_encodings(self) -> List[str]:
        encodings_list = []
        for img in self.missing_people_images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodings_list.append(face_recognition.face_encodings(img)[0])

        return encodings_list

    def start_face_recog(self, missing_people: Dict[int, Tuple[str, str, int]], show: bool = True) -> Dict[int, List[Tuple[Any, ...]]]:
        for person_id, person_info in missing_people.items():
            person_image = cv2.imread(person_info[1])
            self.missing_people_images.append(person_image)
            self.missing_people_ids.append(person_id)

        encode_known = self.find_face_encodings()
        print('Encoding Complete')

        return self.video_capture(encode_known, show)
    
    def check_time_difference(self, current_time, previous_taken_time):
        if len(previous_taken_time) == 0:
            return True 
        elif abs(int(previous_taken_time[-1][-1][14:16]) - int(current_time[14:16])) < 1:
            return False
        else: return True

    def video_capture(self, encode_known: List[str], show: bool) -> Dict[int, List[Tuple[Any, ...]]]:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
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

                now = datetime.now()
                date_string = now.strftime('%Y/%m/%d %H:%M:%S')

                if self.check_time_difference(date_string, self.missing_people_images_from_videos[missing_person_id]):
                    self.missing_people_images_from_videos[missing_person_id].append((cv2.resize(img, (0,0), None, 0.5, 0.5), date_string))
                
                if show:
                    top, right, bottom, left = location
                    top, right, bottom, left = 4 * top, 4 * right, 4 * bottom, 4 * left
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.imshow('img', img)
                
            if cv2.waitKey(1) & 0xFF == ord('q') or len(self.missing_people_images_from_videos[5]) == 1:
                break

        cv2.destroyAllWindows()

        return self.missing_people_images_from_videos