import re
import requests
import threading



def quick_charcter():
    url = 'https://www.character-generator.org.uk/quick/'
    data = {
        'type':5,
        'count':100,
        'gender':'m'
    }
    content = requests.post(url,data)
    content = re.findall('<div class="quick_character">(.+?)</div>',content.text)
    for c in content:
        name = re.findall('\.( .+?),',c)[0]
        name = name.split()
        description = re.findall('</h4>(.+)',c)[0]
        if name[0] in description:
            description = description.replace(name[0],'NAME')
            last = re.findall('NAME (.+ ?)is a',description)
            if len(last)>0:
                description = description.replace(last[0],'')
        if 'year-old' in description:
            year_word = re.findall(' (.+-year-old) ',description)[0]
            description = description.replace(year_word,'AGE')
        print(description)

for i in range(200):
    t = threading.Thread(target=quick_charcter)
    t.start()
