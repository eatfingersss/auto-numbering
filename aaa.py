#encoding=utf-8
#author: walker
#date: 2014-05-15
#function: 更改图片尺寸大小
import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def minImgOut(file_add,out_add):
  img = Image.open(filein)
  print(img.size)
  # out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
  # out.save(fileout, type)

if __name__ == "__main__":
  filein = '.\\0.jpg'
  img = Image.open(filein)
  print(img.size)
  #out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
  #out.save(fileout, type)