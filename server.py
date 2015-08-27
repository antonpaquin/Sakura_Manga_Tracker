#!C:\Python34\pythonw.exe

import http.server
import socketserver
import os

pages_l = os.listdir()
if 'Users' not in pages_l:
    os.mkdir('Users')
if 'Pages' not in pages_l:
    os.mkdir('Pages')
if 'Conf' not in os.listdir('Scraper'):
    os.mkdir('Scraper/Conf')

port=8000

Handler = http.server.CGIHTTPRequestHandler

Handler.cgi_directories = ['/']

print(Handler.cgi_directories)

httpd = http.server.HTTPServer(("", port), Handler)

print('serving')
httpd.serve_forever()
