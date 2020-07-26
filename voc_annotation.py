import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

wd = getcwd()
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
# classes = ["otherObj", "person"]

def convert_annotation(year, image_id, list_file):
    in_file = open('E:/Datasets/VOC/VOCtrainval_06-Nov-2007/VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    list_file.write('E:/Datasets/VOC/VOCtrainval_06-Nov-2007/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(year, image_id))
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # print(cls)
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        if cls == 'person':
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(1))
        else:
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(0))

    list_file.write('\n')

for year, image_set in sets:
    image_ids = open('E:/Datasets/VOC/VOCtrainval_06-Nov-2007/VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(2020, image_set), 'w')
    for image_id in image_ids:
        convert_annotation(year, image_id, list_file)
    list_file.close()
