import cv2
from mail import Inform
import video_face_recog


alert = Inform()
video_face_recog = video_face_recog.face_recog('./Images','',names=[], wanted_names=[])
video_face_recog.start_face_recog()
wanted_names = video_face_recog.get_names()
cv2.destroyAllWindows()
print(wanted_names)
for name in wanted_names:
    alert.send(name + '.jpg', name, wanted_names[name])