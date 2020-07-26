#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import os
import time
yolo = YOLO()

# img = './img/street.jpg'

imgsPath = './img/'

imgsList = os.listdir(imgsPath)
for img in imgsList:
    start = time.time()
    imgPath = imgsPath + img
    image = Image.open(imgPath)

    r_image = yolo.detect_image(image)
    print(time.time() - start)
    r_image.save('./result/' + img)

