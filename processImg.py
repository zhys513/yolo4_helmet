idl_file = "E:/Datasets/head/brainwash/brainwash/brainwash_train.idl"
output = 'head_train.txt'



with open(output, 'w+', encoding='utf-8') as output:
    f = open(idl_file, 'r+')
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.replace(":", ";")
        img_dir = line.split(";")[0]
        img_boxs = line.split(";")[1]
        img_dir = img_dir.replace('"',"")
        output.write(img_dir)
        output.write(' ')

        img_boxs = img_boxs.replace(",","")              #删除“，”
        img_boxs = img_boxs.replace("(","")              #删除“(”
        img_boxs = img_boxs.split(")")                   #删除“)”

        for n in range(len(img_boxs) - 1):  # 消除空格项影响
            box = img_boxs[n]
            box = box.split(" ")
            print(box)
            output.write(str(int(float(box[1]))))
            output.write(',')
            output.write(str(int(float(box[2]))))
            output.write(',')
            output.write(str(int(float(box[3]))))
            output.write(',')
            output.write(str(int(float(box[4]))))
            output.write(',')
            output.write('0')
            output.write(' ')
        output.write('\n')