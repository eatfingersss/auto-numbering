import os
import re

id = 0
name = ''
i = []
for i in os.listdir('.'):
    # if i.find('.')==-1:
    # 	continue
    name = i.split('.')[1]
    if name == 'png' or name == 'jpg' or name == 'jpeg' or name == 'bmp':
        os.rename('./' + i, './' + str(id) + '.' + name)
        print(i + '->' + str(id) + '.' + name + '\n')
        id += 1
