import requests
from bs4 import BeautifulSoup
import os

home = '\\'.join(os.getcwd().split('\\')[:-1])

def getSoup(url):
    source = requests.get(url, headers={'User-Agent' : "Magic Browser"}).text
    return BeautifulSoup(source)

def saveImage(data, comic, number):
    pagenum = str(number)
    while (len(pagenum) < 5):
        pagenum = '0' + pagenum
    filename = home + '/Pages/' + comic + '/Data/' + pagenum + '.png'
    file = open(filename,'wb')
    file.write(data)
    file.close()
