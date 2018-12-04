import urllib.request
import urllib.error
import json
import matplotlib.pyplot as plt
import threading


lock = threading.RLock()

amount = '500000'
count = '50'
number = 200

global data
global right_number
right_number = 0
data = [0 for x in range(50)]


def calculater():
    lock.acquire()
    global data
    global right_number
    try:
        for i in range(50):
            content = urllib.request.urlopen(
                'https://alpha.evolution.land/api/test/red_packet?amount=' + amount + '&count=' + count)
            content = json.loads(content.read())
            per_data = [int(x) for x in content['data']]
            for j in range(50):
                data[j] += float(per_data[j])
            right_number += 1
            print(right_number)
    except urllib.error.URLError as e:
        print(e.reason)
    lock.release()


for i in range(int(number/50)):
    t = threading.Thread(target=calculater)
    t.start()
    t.join()



fig = plt.figure('fig')
print(right_number)
data = [x / right_number for x in data]
data_min = min(data)
data_max = max(data)
plt.bar([x for x in range(len(data))], data, width=0.5, facecolor='lightskyblue', edgecolor='white')

plt.xlim(0, 51)
plt.ylim(data_min - 10, data_max + 10)
plt.title("data")
plt.xlabel("count")
plt.ylabel("value")
plt.show()


