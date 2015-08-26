#!C:\Python34\pythonw.exe

import http.server
import socketserver
import os

port=8000

Handler = http.server.CGIHTTPRequestHandler

Handler.cgi_directories = ['/']
    
print(Handler.cgi_directories)

httpd = http.server.HTTPServer(("", port), Handler)

print('serving')
httpd.serve_forever()
