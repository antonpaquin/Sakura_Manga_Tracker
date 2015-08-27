#!C:\Python34\pythonw.exe
import os
import json

def run():
    print('Content-type: text/html\n')

    if 'HTTP_COOKIE' in os.environ:
        user = get_user(os.environ['HTTP_COOKIE'])
        if user == 'null':
            showUserSwap()
            return
    else:
        showUserSwap()
        return

    params = {}
    for param in os.environ['QUERY_STRING'].replace('%20',' ').split('&'):
        if param != '':
            s = param.split('=')
            params[s[0]] = s[1]

    if 'page' in params:
        if params['page'] == 'user':
            showUserSwap()
        elif params['page'] == 'updates':
            giveUpdates(user)
        return

    showGrid(user)

def showGrid(user):
    with open('Utils/HTML/Homepage.html') as base_f:
        base = '\n'.join(base_f.readlines())
    with open('Utils/HTML/ComicBox.html') as box_f:
        box = '\n'.join(box_f.readlines())
    with open('Users/' + user + '/grid.conf') as gridItems_f:
        gridItems = [g.strip() for g in gridItems_f.readlines()]

    if len(gridItems)==0:
        with open('Utils/HTML/EmptyGrid.html') as base_f:
            base = base_f.read()
        print(base)
        return

    grid = '<tr>'
    i = 0
    for item in gridItems:
        if i==7:
            i=0
            grid += '</tr><tr>'
        i+=1
        append = box
        append = append.replace('#updated#',checkUpdated(user, item))
        append = append.replace('#link#','comic.py?comic='+item+'&page='+str(updated[item]))
        append = append.replace('#cover#','Pages/' + item + '/cover.png')
        append = append.replace('#comic#',item)
        grid += append
    grid += '</tr>'

    base = base.replace('#grid#',grid)
    base = base.replace('#user#',user)
    print(base)

def showUserSwap():
    users_l = os.listdir('Users')
    if len(users_l) == 0:
        with open('Utils/HTML/Setup.html') as base_f:
            base = base_f.read()
        print(base)
    else:
        with open('Utils/HTML/SwapUser.html') as base_f:
            base = base_f.read()
        with open('Utils/HTML/SwapUser_user.html') as user_f:
            user_h = user_f.read()
        users = ''
        for user in users_l:
            users += user_h.replace('#user#',user)
        base = base.replace('#users#',users)
        print(base)

def giveUpdates(user):
    res = {}
    if not updated:
        with open('Users/'+user+'/seen.conf') as seen_f:
            for line in seen_f.readlines():
                s = line.split('=')
                updated[s[0]]=int(s[1])
    for obj in updated:
        res[obj] = checkUpdated(user, obj)
    print(json.dumps(res))

updated = {}
def checkUpdated(user, comic):
    if not updated:
        with open('Users/'+user+'/seen.conf') as seen_f:
            for line in seen_f.readlines():
                s = line.split('=')
                updated[s[0]]=int(s[1])
    if comic not in updated:
        updated[comic] = 1
        return 'updated'
    comic_position = int(os.listdir('Pages/'+comic+'/Data')[-1].split('.')[0])
    if comic_position > updated[comic]:
        return 'updated'
    else:
        return ''

def get_user(cookie):
    cookies = cookie.split('; ')
    for c in cookies:
        if c[:5] == 'User=':
            return c[5:]
    return 'null'

run()
