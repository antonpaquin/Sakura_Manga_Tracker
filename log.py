#!C:\Python34\pythonw.exe
import os
import pprint

def run():
    user = get_user(os.environ['HTTP_COOKIE'])
    params = {}
    for param in os.environ['QUERY_STRING'].replace('%20',' ').split('&'):
        s = param.split('=')
        params[s[0]] = s[1]

    if params['reason'] == 'page_scroll':
        userScrolled(user, params)

def userScrolled(user, params):
    old_f = open('Users/' + user + '/seen.conf','r')
    new_f = open('Users/' + user + '/seen.conf.new','w')
    add=True
    for line in old_f.readlines():
        s = line.strip().split('=')
        if s[0] == params['comic']:
            add=False
            new_f.write(params['comic'] + '=' + params['page'] + '\n')
        else:
            new_f.write(line)
    if (add):
        new_f.write(params['comic'] + '=' + params['page'] + '\n')
    old_f.close()
    new_f.close()
    os.remove('Users/' + user + '/seen.conf')
    os.rename('Users/' + user + '/seen.conf.new', 'Users/' + user + '/seen.conf')

def get_user(cookie):
    cookies = cookie.split('; ')
    for c in cookies:
        if c[:5] == 'User=':
            return c[5:]
    return 'null'

run()
