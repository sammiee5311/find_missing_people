import cv2

##########################
from mail import Inform
import video_face_recog
import server
##########################

inform = Inform()

serve = server.From_server()
serve.read_csv() # write url
wanted_names = serve.download_images() # write path where you want to download images

video_face_recog = video_face_recog.face_recog('./Images', wanted_names=wanted_names)
video_face_recog.start_face_recog()
wanted_pictures = video_face_recog.get_pictures()
wanted_names = video_face_recog.get_names()

for name, picture in wanted_pictures.items():
    cv2.imwrite(name + '.jpg', picture)
for name in wanted_names:
    inform.send(name + '.jpg', wanted_names[name])
