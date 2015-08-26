#!C:\Python34\pythonw.exe
import cgi
import os
import shutil

def run():
    print('Content-Type:text/html\n')
    if 'HTTP_COOKIE' in os.environ:
        user = get_user(os.environ['HTTP_COOKIE'])

    params = {}
    for param in os.environ['QUERY_STRING'].replace('%20',' ').split('&'):
        if param != '':
            s = param.split('=')
            params[s[0]] = s[1]

    if 'page' in params:
        if params['page'] == 'import':
            showImport(user)
        elif params['page'] == 'importp':
            doImport()
        elif params['page'] == 'useradd':
            showAddUser()
        elif params['page']=='useraddp':
            doAddUser()
        elif params['page'] == 'grid':
            showModGrid(user)
        elif params['page'] == 'gridp':
            doModGrid(user)
        return

    showSettingsHome(user)

def showSettingsHome(user):
    with open('Utils/HTML/Settings.html') as base_f:
        base = base_f.read()
    base = base.replace('#user#',user)
    print(base)

def showImport(user):
    with open('Utils/HTML/Import.html') as base_f:
        base = base_f.read()
    base = base.replace('#user#',user)
    print(base)

def doImport():
    data = cgi.FieldStorage() #name, link, cover
    name = data.getvalue('name')
    link = data.getvalue('link')
    cover = data.getvalue('cover')

    if name in os.listdir('Pages'):
        print('<h1>Manga already imported! Did not add duplicate.</h1>')
        return

    os.mkdir('Pages/'+name)
    os.mkdir('Pages/'+name+'/Data')
    cover_f = open('Pages/'+name+'/cover.png','wb')
    cover_f.write(cover)
    cover_f.close()
    sav_f = open('Scraper/conf/'+name+'.sav','w')
    sav_f.write(link + '\n') #initial link
    sav_f.write(link + '\n') #current link
    sav_f.write('1')
    sav_f.close()
    print('<h1>Added successfully!</h1><br/><a href="settings.py">Go Back</a>')

def showAddUser():
    with open('Utils/HTML/AddUser.html') as base_f:
        base = base_f.read()
    print(base)

def doAddUser():
    data = cgi.FieldStorage()
    name = data.getvalue('name')
    image = data.getvalue('image')

    if name in os.listdir('Users'):
        print('<h1>User already exists! Did not recreate.</h1>')
        return

    os.mkdir('Users/'+name)
    os.mkdir('Users/'+name+'/CSS')
    open('Users/'+name+'/grid.conf','w').close()
    open('Users/'+name+'/seen.conf','w').close()
    shutil.copy('Utils/CSS/template_comic.css','Users/'+name+'/CSS/comic.css')
    shutil.copy('Utils/CSS/template_home.css','Users/'+name+'/CSS/home.css')
    shutil.copy('Utils/CSS/template_import.css','Users/'+name+'/CSS/import.css')
    shutil.copy('Utils/CSS/template_modgrid.css','Users/'+name+'/CSS/modgrid.css')
    shutil.copy('Utils/CSS/template_settings.css','Users/'+name+'/CSS/settings.css')
    image_f = open('Users/'+name+'/profile.png','wb')
    image_f.write(image)
    image_f.close()

    print('<h1>Added successfully!</h1><br/><a href="index.py?page=user">Go Back</a>')

def showModGrid(user):
    with open('Utils/HTML/ModGrid.html') as base_f:
        base = base_f.read()
    with open('Utils/HTML/ModGrid_row.html') as row_f:
        row = row_f.read()
    with open('Users/'+user+'/grid.conf') as grid_f:
        grid = [g.strip() for g in grid_f.readlines()]
    comics_l = os.listdir('Pages')

    rows = ''
    for comic in comics_l:
        r = row
        r = r.replace('#image#','Pages/'+comic+'/cover.png')
        r = r.replace('#comic#',comic)
        r = r.replace('#addHidden#', 'hidden' if comic in grid else '')
        r = r.replace('#removeHidden#', '' if comic in grid else 'hidden')
        rows += r

    base = base.replace('#user#',user)
    base = base.replace('#rows#',rows)

    print(base)

def doModGrid(user):
    data = cgi.FieldStorage()
    method = data.getvalue('method')
    title = data.getvalue('title')

    if method=='remove':
        with open('Users/'+user+'/grid.conf') as grid_f:
            grid = [g.strip() for g in grid_f.readlines() if g.strip() != title]
        grid_new_f = open('Users/'+user+'/grid.conf.new','w')
        for line in grid:
            grid_new_f.write(line + '\n')
        grid_new_f.close()
        os.remove('Users/'+user+'/grid.conf')
        os.rename('Users/'+user+'/grid.conf.new', 'Users/'+user+'/grid.conf')
    elif method=='add':
        grid_f = open('Users/'+user+'/grid.conf','a')
        grid_f.write(title + '\n')
        grid_f.close()

def get_user(cookie):
    cookies = cookie.split('; ')
    for c in cookies:
        if c[:5] == 'User=':
            return c[5:]
    return 'null'


run()
