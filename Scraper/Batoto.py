import requests
from bs4 import BeautifulSoup
import ScraperUtils

def getNextPage(soup):
    script = [a for a in soup.find_all('script') if 'Hotkeys' in str(a.contents)][0].contents[0]
    script = between(script, 'right', '}')
    script = between(script, '\'', '\'')
    return script

def getImage(soup):
    candidates = [a['src'] for a in soup.find_all('img') if 'img.bato.to/comics' in a['src']]
    candidates = [c for c in candidates if '/comics/misc' not in c]
    return requests.get(candidates[0]).content

def hasUpdates(soup):
    if ('http://bato.to/comic/_' in getNextPage(soup)):
        return False
    else:
        return True

def between(src, a, b):
    res = src[src.find(a)+len(a):]
    res = res[:res.find(b)]
    return res
