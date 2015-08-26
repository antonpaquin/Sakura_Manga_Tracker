import time
import threading
from Scraper import GrabOrchestrator

def run():
    GrabOrchestrator.run()
    print('ding')

while(True):
    threading.Thread(target=run).start()
    time.sleep(60*60)
