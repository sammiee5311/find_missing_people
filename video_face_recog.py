import cv2
import numpy as np
import face_recognition
from glob import glob
from datetime import datetime


class face_recog:
    def __init__(self, path, wanted_names):
        self.path = path
        self.images = []
        self.names_list = []
        self.people = glob(path + '/*.jpg')
        self.wanted = {}
        self.check_wanted = {}
        for name in wanted_names:
            self.wanted[name.upper()] = 0

    def find_face_encodings(self):
        encodings_list = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodings_list.append(face_recognition.face_encodings(img)[0])

        return encodings_list

    def start_face_recog(self):
        for person in self.people:
            cur = cv2.imread(person)
            self.images.append(cur)
            self.names_list.append(person.split('\\')[1][:-4])

        print(self.names_list)

        encode_known = self.find_face_encodings()
        print('Encoding Complete')

        self.video_capture(encode_known)

    def video_capture(self, encode_known):
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

                name = self.names_list[matched_idx].upper() if check[matched_idx] else 'UNKNOWN'
                top, right, bottom, left = location
                top, right, bottom, left = 4 * top, 4 * right, 4 * bottom, 4 * left

                if name in self.wanted and not self.wanted[name]:
                    cv2.imwrite(name+'.jpg', cv2.resize(img, (0,0), None, 0.5, 0.5))
                    now = datetime.now()
                    date_string = now.strftime('%Y-%m-%d %H:%M:%S')
                    self.check_wanted[name] = date_string
                    self.wanted[name] = 1

                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                cv2.imshow('img', img)
                cv2.waitKey(1)

            now = datetime.now()
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
            if now.strftime('%M')=='00':
                break

        cv2.destroyAllWindows()

    def get_names(self):
        return self.check_wanted
