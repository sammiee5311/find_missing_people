# self_inform ( In Progress)
If it finds a person, a picture of the person and time automatically will be sent by mail or server. 

## How to use
+ Change to your email and password 'self.server.login('email', 'password')' on mail.py(42 line)
+ Change to from_email and to_email 'email_from = 'from_email'' 'email_to = ['to_email']' on mail.py(69,70 lines)
+ Change to image path and names that you want to find 'video_face_recog = video_face_recog.face_recog('./Images path', wanted_names=['name'])' on main.py(9 line)

## Requirements
+ opencv-python
+ cmake
+ dlib
+ face-recognition
+ BeautifulSoup
+ urllib
+ requests

### Refrence
+ https://github.com/ageitgey/face_recognition
