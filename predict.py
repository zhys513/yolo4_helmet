from yolo import YOLO
from PIL import Image
import os
import time
yolo = YOLO()


imgsPath = './img/'

imgsList = os.listdir(imgsPath)
for img in imgsList:
    start = time.time()
    imgPath = imgsPath + img
    # imgPath = imgsPath + 'hard_hat_workers3651.png'
    image = Image.open(imgPath)

    r_image = yolo.detect_image(image)
    print(time.time() - start)
    r_image.save('./result/' + img)

