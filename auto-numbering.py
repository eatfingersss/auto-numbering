import os
import re
import fileinput
import random

id = 0
name = ''
i = []
for i in os.listdir('.'):
    if i.find('.')==-1:
        continue
    name = i.split('.')[1]

    if name == 'png' or name == 'jpg' or name == 'jpeg' or name == 'bmp':
        os.rename('./' + i, './' + str(int(random.random()*10000000000)) + '.' + name)

for i in os.listdir("."):
    if i.find('.')==-1:
        continue
    name = i.split('.')[1]
    if name == 'png' or name == 'jpg' or name == 'jpeg' or name == 'bmp':
        print(i + '->' + str(id) + '.' + name)
        os.rename('./' + i, './' + str(id) + '.' + name)
        id += 1
direct=open('res.json','w')
res='{\"MaxCount\" :'+str(id-1)+'}'
direct.write(res)
direct.close()
os.system('PAUSE')
