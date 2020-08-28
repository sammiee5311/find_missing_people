import cv2
from mail import Inform
import video_face_recog

inform = Inform()

##### GET THE NAMES AND PICTURE FROM SERVER #####

while True:
    video_face_recog = video_face_recog.face_recog('./Images', wanted_names=['Sammy'])
    video_face_recog.start_face_recog()
    wanted_names = video_face_recog.get_names()
    for name in wanted_names:
    inform.send(name + '.jpg', name, wanted_names[name])
