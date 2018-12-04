import urllib.request
import urllib.error
import json
import threading
import matplotlib.pyplot as plt

dict = {}
num = 0
i = 1200000
#body = ['sphynx', 'siberian', 'lynx', 'lynx', 'birman', 'himalayan', 'himalayan', 'lynx', 'bobtail', 'ragamuffin', 'savannah', 'siberian', 'ragdoll', 'lynx', 'lynx', 'munchkin', 'siberian', 'siberian', 'siberian', 'toyger', 'lynx', 'siberian', 'pixiebob', 'ragdoll', 'siberian', 'siberian', 'koladiviya', 'sphynx', 'lynx', 'selkirk', 'lynx', 'lynx', 'lynx', 'chantilly', 'lynx', 'mekong', 'sphynx', 'munchkin', 'savannah', 'sphynx']
eye = []
def scrapy(x,y):
    for i in range(x,y):
        try:
            content = urllib.request.urlopen('https://api.cryptokitties.co/kitties/'+str(i))
            content = json.loads(content.read())
            print(content['bio'])
        except:
            pass

for i in range(200):
    t = threading.Thread(target=scrapy(1200500+i*20,1200500+(i+1)*20))
    t.start()
