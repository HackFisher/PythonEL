import pickle
import random



f = open('description.pkl','rb')

dic = pickle.load(f)

l_hello = len(dic['hello'])
l_name = len(dic['name'])
l_sentence = len(dic['sentence'])
l_says = len(dic['says'])
l_bye = len(dic['bye'])

print(l_hello)
print(l_name)
print(l_sentence)
print(l_says)
print(l_bye)

hello = dic['hello']
name = dic['name']
sentence = dic['sentence']
says = dic['says']
bye = dic['bye']
for i in range(10000):
    print(hello[random.randint(0,l_hello-1)],name[random.randint(0,l_name-1)],sentence[random.randint(0,l_sentence-1)],says[random.randint(0,l_says-1)],bye[random.randint(0,l_bye-1)])