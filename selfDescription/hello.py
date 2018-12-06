import re
import nltk
import nltk.data
import json
import Levenshtein
import pickle


def splitSentence(paragraph):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(paragraph)
    return sentences


# Get raw text as string.
with open("miao.txt") as f:
    text = f.readlines()

E_hello = []
E_name = []
C_hello = []
for t in text:
    t_h = splitSentence(t)
    try:
        if '*' not in t_h[0]:
            if len(re.findall('[a-zA-Z]', t_h[0])) > 0:
                if t_h[0] not in E_hello and "I" not in t_h[0] and len(t_h[0]) >= 4 and len(t_h[0]) <= 15:
                    flag = 0
                    for e_h in E_hello:
                        if Levenshtein.ratio(t, e_h) > 0.8:
                            flag = 1
                            break
                    if flag == 0:
                        E_hello.append(t_h[0])
                E_name.append(t_h[1])
            else:
                C_hello.append(t_h[0])
    except IndexError:
        pass

# print(E_hello)
E_name_module = []
for e in E_name:
    try:
        name = re.findall('[A-Z][a-z]+ [A-Z][a-z]+', e)[0]
        e = e.replace(name, 'his_name')
        if e not in E_name_module and len(re.findall('[A-Z]', e)) < 2 and len(re.findall('\d', e)) == 0:
            flag = 0
            for e_n in E_name_module:
                if Levenshtein.ratio(e, e_n) > 0.8:
                    flag = 1
                    break
            if flag == 0:
                E_name_module.append(e)
    except:
        pass


with open("1000_english.txt") as f:
    text = f.readlines()

sentence = []
says = []
bye = []

for t in text:
    t = t.replace('\n', '')
    if len(t) <= 30:
        bye.append(t)
    else:
        sentence.append(t)

with open("says_english.txt") as f:
    text = f.readlines()


for t in text:
    t = t.replace('\n','')
    if len(t) <= 30:
        bye.append(t)
    else:
        says.append(t)
print(len(E_hello))
print(len(E_name_module))
print(len(sentence))
print(len(bye))
print(len(says))


dic = {}
dic['hello'] = E_hello
dic['name'] = E_name_module
dic['sentence'] = sentence
dic['says'] = says
dic['bye'] = bye

f = open('description.pkl', 'wb')

pickle.dump(dic,f)
