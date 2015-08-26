import Batoto
import ScraperUtils
import os

def run():
    for comic in getComics():
        try:
            save = loadSaveData(comic)
            soup = ScraperUtils.getSoup(save['currentLink'])
            if (Batoto.hasUpdates(soup)):
                grab_updates(comic, save)
                writeSaveData(save, comic)
        except Exception as e:
            logError(comic, e)
            continue

def grab_updates(comic, save):
    soup = ScraperUtils.getSoup(save['currentLink'])
    while(Batoto.hasUpdates(soup)):
        ScraperUtils.saveImage(Batoto.getImage(soup), comic, save['currentPage'])
        save['currentLink'] = Batoto.getNextPage(soup)
        save['currentPage'] += 1
        soup = ScraperUtils.getSoup(save['currentLink'])
    ScraperUtils.saveImage(Batoto.getImage(soup), comic, save['currentPage'])


def getComics():
    return [item.split('.')[0] for item in os.listdir('conf')]

def loadSaveData(comic):
    save_f = open('conf/' + comic + '.sav','r')
    lines = save_f.readlines()
    save_f.close()
    return {'initialLink':lines[0].strip(),
            'currentLink':lines[1].strip(),
            'currentPage':int(lines[2].strip())}

def writeSaveData(save, comic):
    save_f = open('conf/' + comic + '.sav','w')
    save_f.write(save['initialLink'] + '\n')
    save_f.write(save['currentLink'] + '\n')
    save_f.write(str(save['currentPage']))
    save_f.close()

def logError(comic, e):
    f = open('../error.log','a')
    f.write(comic + ' : ' + str(e) + '\n')
    f.close()
