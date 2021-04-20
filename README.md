# Find_missing_people (version 1.0)
+ It is a program which is automatically informing wanted people if the camera is pointing their faces. <br>
+ It detects faces which are on the server. <br>

## The motivation
+ There are a number of criminal activities nowadays, I wanted to make a program that makes finding people easier. <br>
+ However, everyone who has a self-driving car can help to find people. <br>
+ The camera which is attached on the car will look faces during people driving so that it will be easier to find people.

## Test
![](./Images/test.gif)

+ I've just combined with my self-driving car which I made with a raspberry-pi to show how would be worked with a [self-driving car](https://github.com/sammiee5311/raspberry_pi/tree/master/self_driving_car). <br>

## How to use
+ Change to your `email` and `password` [(code)](https://github.com/sammiee5311/self_inform/blob/41bb73744aee67f02bb74c691e6c67ce32c3296d/mail.py#L42)
```python
self.server.login('email', 'password') (42 line on mail.py)

# example
self.server.login('abcd@gmail.com', 'abcd'
```

+ Change to `from_email` and `to_email` [(code)](https://github.com/sammiee5311/self_inform/blob/e118cf4923e131d78759ce730d6ffd87813a4a17/mail.py#L69)
```python
email_from = 'from_email' (69,70 lines on mail.py)
email_to = ['to_email']

# example
email_from = 'abcd@gmail.com'
email_to = 'efgh@gmail.com'
```

+ Write `csv_file` link [(code)](https://github.com/sammiee5311/self_inform/blob/e118cf4923e131d78759ce730d6ffd87813a4a17/main.py#L12)
``` python
serve.read_csv() (12 line on main.py)

# example
serve.read_csv('https://sammiee5311.github.io/test/') 
```

+ Write path where you want to download images [(code)](https://github.com/sammiee5311/self_inform/blob/e118cf4923e131d78759ce730d6ffd87813a4a17/main.py#L13)
``` python
wanted_names = serve.download_images() (13 line on main.py)

# example
wanted_names = serve.download_images('./Images')
````

+ Change to image path and names that you want to find [(code)](https://github.com/sammiee5311/self_inform/blob/e118cf4923e131d78759ce730d6ffd87813a4a17/main.py#L15)
``` python
video_face_recog = video_face_recog.face_recog('./Images', wanted_names=wanted_names) (15 line on main.py)
```

## How it works
+ Dowload the csv file which includes people names and pictures from website(or server). <br>
+ Use raspberry pi, arduino or computer to initialize face-recognition in python. <br>
+ Put the people names and pictures in the list. <br>
+ It will look all faces through connected camera. <br>
+ Once the person who is in the list is appeared, that person is taken a picture and automatically sent the picture and the time to personal e-mail(gmail).

## Requirements
+ opencv-python
+ cmake
+ dlib
+ face-recognition
+ smtplib
+ BeautifulSoup
+ urllib
+ requests

## Todo
- [ ] Use Django

### Refrence
+ https://github.com/ageitgey/face_recognition
+ https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
