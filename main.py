import cv2
from mail import Inform
import video_face_recog
import server

inform = Inform()

serve = server.From_server() # write url
serve.read_csv()
wanted_names = serve.download_images() # write path where you want to download images

video_face_recog = video_face_recog.face_recog('./Images path', wanted_names=wanted_names)
video_face_recog.start_face_recog()
wanted_names = video_face_recog.get_names()
for name in wanted_names:
inform.send(name + '.jpg', name, wanted_names[name])
