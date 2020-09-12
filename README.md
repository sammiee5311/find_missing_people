# self_inform (In Progress)
If it finds a person through camera, a picture of the person and time automatically will be sent to personal e-mail(gmail).

## How to use
+ Change to your email and password 'self.server.login('email', 'password')' on mail.py(42 line)
+ Change to from_email and to_email 'email_from = 'from_email'' 'email_to = ['to_email']' on mail.py(69,70 lines)
+ Change to image path and names that you want to find 'video_face_recog = video_face_recog.face_recog('./Images path', wanted_names=['name'])' on main.py(9 line)

## How it works
Dowload the csv file which includes people names and pictures from website(or server). <br>
Use raspberry pi, arduino or computer to initialize face-recognition in python. <br>
Put the people names and pictures in the list. <br>
It will look all faces through connected camera. <br>
Once the person who is in the list is appeared, that person is taken a picture and automatically sent the picture and the time to personal e-mail(gmail).

## Requirements
+ opencv-python
+ cmake
+ dlib
+ face-recognition
+ smtplib
+ BeautifulSoup
+ urllib
+ requests

### Refrence
+ https://github.com/ageitgey/face_recognition
