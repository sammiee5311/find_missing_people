FROM python:3.8.4

ENV PYTHONUNBUFFERED 1
RUN apt-get -y update

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('a@a.com', 'admin', 'password')" | python manage.py shell
