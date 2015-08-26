#!C:\Python34\pythonw.exe

import time
import os
from PIL import Image

def run():
    print('Content-Type:text/html\n')

    user = get_user(os.environ['HTTP_COOKIE'])

    params = {}
    for param in os.environ['Query_String'].replace('%20',' ').split('&'):
        s = param.split('=')
        params[s[0]]=s[1]

    if 'comic' not in params:
        print('badly formed')
        return

    if 'page' not in params:
        params['page'] = 1

    showPage(user, params['comic'], int(params['page']))

def showPage(user, comic, start):
    with open('Utils/HTML/ComicPage.html') as base_f:
        base = '\n'.join(base_f.readlines())
    with open('Utils/HTML/ComicImage.html') as image_template_f:
        image_template = '\n'.join(image_template_f.readlines())

    images_html = ''
    images_list = os.listdir('Pages/' + comic + '/Data')

    if len(images_list)==0:
        print("<html><p>The scraper hasn't picked this up yet. Try coming back after it has run</p></html>")
        return

    for image in images_list:
        if int(image.split('.')[0]) >= start:
            src = 'Pages/' + comic + '/Data/' + image
            im = Image.open(src)
            size = 'width="' + str(im.size[0]) + '" height="' + str(im.size[1]) + '"'
            images_html += image_template.replace('#src#',src).replace('#size#',size)

    base = base.replace('#user#',user)
    base = base.replace('#images#',images_html)
    print(base)


def getNumSeen(user, comic):
    with open('Users/' + user + '/seen.conf') as seen_f:
        for line in seen_f.readlines():
            s = line.split('#')
            if s[0] == comic:
                return s[1]
    return 0

def get_user(cookie):
    cookies = cookie.split('; ')
    for c in cookies:
        if c[:5] == 'User=':
            return c[5:]
    return 'null'

run()
