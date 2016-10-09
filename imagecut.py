import sys
import os
from operator import itemgetter
from PIL import Image, ImageEnhance, ImageFilter
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as IMG

CLARIFAI_APP_ID = 'qRE1Uj_OVHIpXK8PwQ9egmECNLotdyjWS6_y6gqz'
CLARIFAI_APP_SECRET = '7QcCSGN1ChCCOobwGU7YWFGnEaQPJHW-V6mCiprE'

app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)

model = app.models.get('f97fb98258e14f15abacffafb7187873')

sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2

def receipt_filter(filename):
    #path = filename
    #img = Image.open(path)
    #img = img.convert('RGBA')
    #pix = img.load()
    # modify image to maximize the readability of text
    #for y in range(img.size[1]):
     #   for x in range(img.size[0]):
      #      if pix[x, y][0] < 120 or pix[x, y][1] < 120 or pix[x, y][2] < 120:
       #         pix[x, y] = (0, 0, 0, 255)
        #    else:
         #       pix[x, y] = (255, 255, 255, 255)
    #img.save('temp.jpg')
    im = Image.open(filename)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('temp.jpg')
    img = Image.open('temp.jpg')
    img = img.convert('RGBA')
    pix = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 240 or pix[x, y][1] < 240 or pix[x, y][2] < 240:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)
    img.save('temp.jpg')
    return "temp.jpg"

imgstr = receipt_filter("fig-receipt-oasis-04-12.jpg")
im = cv2.imread(imgstr)
image = Image.open(imgstr)
im3 = im.copy()

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

#################      Now finding Contours         ###################

_, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#keys = [i for i in range(48,58)]
coordlist = list()

for cnt in contours:
    if cv2.contourArea(cnt)>25:
        [x,y,w,h] = cv2.boundingRect(cnt)

        if  h>25:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            coordlist.append((x, y, x + w, y + h))
coordlist = sorted(coordlist, key=itemgetter(0))
coordlist = sorted(coordlist, key=itemgetter(1))
imagelist = list()
for coord in coordlist:
    imagelist.append(image.crop(coord))


count = 1
for imgs in imagelist:
    imgs.save('%i.jpg' %count)
    climage = IMG(file_obj=open("%i.jpg" %count, 'rb'))
    predict_return = model.predict([climage])
    print predict_return[u'outputs'][0][u'data'][u'concepts'][0][u'id']
    count += 1

cv2.imshow('norm',im)
key = cv2.waitKey(0)
if key == 27:
    sys.exit()

