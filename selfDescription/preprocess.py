import re
import nltk
import nltk.data
import json
import Levenshtein
import pickle

with open("second_sentence.txt") as f:
    text = f.readlines()
n=0
sentence = []
for t in text:
    try:
        senten = re.findall('[a-zA-Z, ,\,,\',\-,\.,\",!,?,;]+',t)[0]
        if len(senten) > 5 and len(senten)<100:
            senten = senten.capitalize()
            if senten not in sentence:
                sentence.append(senten)
                n+=1
    except:
        pass
for s in sentence:
    print(s)
print(n)