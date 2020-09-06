import xml.etree.ElementTree as ET
from os import getcwd


rootPath = 'E:/Datasets/helmets/'
Datasets = ['helmet', 'VOC2028']
types = ['train', 'val', 'test']
wd = getcwd()
classes = ["helmet", "head"]


def convert_annotation(rootPath, Dataset, image_id, list_file):
    in_file = open(rootPath + Dataset + '/Annotations/%s.xml' % (image_id), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    if Dataset == 'helmet':
        list_file.write(rootPath + Dataset + '/JPEGImages/%s.png' % (image_id))
    elif Dataset == 'VOC2028':
        list_file.write(rootPath + Dataset + '/JPEGImages/%s.jpg' % (image_id))
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text

        if cls == 'hat':
            cls = 'helmet'
        if cls == 'person':
            cls = 'head'
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        print(image_id, cls, cls_id)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

    list_file.write('\n')


list_file = open('helmet_train.txt', 'w')
for Dataset in Datasets:
    print(Dataset)
    for _type in types:
        image_ids = open('E:/Datasets/helmets/' + Dataset + '/ImageSets/Main/%s.txt' % (_type,)).read().strip().split()
        # list_file = open('%s_%s.txt' % ('helment', _type), 'w')
        for image_id in image_ids:
            convert_annotation(rootPath, Dataset, image_id, list_file)
list_file.close()
