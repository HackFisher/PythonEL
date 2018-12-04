import re
import json

dic = {}
female_first_list = []
female_first = open('data/dist.female.first').readlines()[0:1000]
for female in female_first:
    female_first_list.append(re.findall('\w+',female)[0])

dic['female_first']=female_first_list

male_first_list = []
male_first = open('data/dist.male.first').readlines()[0:1000]
for male in male_first:
    male_first_list.append(re.findall('\w+',male)[0])

dic['male_first'] = male_first_list

all_last_list = []
all_last = open('data/dist.all.last').readlines()[0:1000]
for all in all_last:
    all_last_list.append(re.findall('\w+',all)[0])

dic['all_last'] = all_last_list

json_data = json.dumps(dic)
f = open('names.json', 'w')
f.write(json_data)
f.close()