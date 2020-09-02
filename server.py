import urllib.request
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import csv


class From_server:
    def __init__(self):
        self.images = []
        self.names = []
        self.file_link = ''

    def read_csv(self, url='https://sammiee5311.github.io/test/'):
        response = urllib.request.urlopen(url)

        soup = BeautifulSoup(response, 'html.parser')
        item = soup.select('.page__content a')
        a = str(item).split("\"")
        self.file_link = requests.get(a[1])
        print('read csv completed')

    def download_images(self, download_path='./Images/'):
        wrapper = csv.reader(self.file_link.text.strip().split('\n'))
        for record in wrapper:
            if record[1] != 'images':
                self.names.append(str(record[0]))
                self.images.append(str(record[1]))

        for i, image in enumerate(self.images):
            urlretrieve(image, download_path + self.names[i] + '.jpg')

        print('download images completed')

        return self.names