"""
    将data目录中的图片随机拿出85% 放到   dataset/train
    将data目录中的图片随机拿出10% 放到   dataset/valid
    将data目录中的图片随机拿出5% 放到    dataset/test
"""
import os
"""
    1、创建目录
"""
datasetName = ["test","valid","train"]
for i in range(3):
    os.makedirs(f"./dataset/{datasetName[i]}", exist_ok=True)

"""
    2、
            计算data图片数量
            计算放入到dataset/train 数量 
            计算放入到dataset/valid 数量 
            计算放入到dataset/test 数量 
"""
img_list = []
count = 0
for i in os.listdir("./data"):
    if i[-3:]=="jpg":
        img_list.append(i)
        count += 1
import random
# 打乱里面的元素
random.shuffle(img_list)


print(img_list)
print("图片总量：",count)

train_num = int(count*0.85)
valid_num = int(count*0.1)
test_num  = int(count-train_num-valid_num)

numStruct = [test_num,valid_num,train_num]
print(f"训练集数量：{train_num} 验证集数量：{valid_num}  测试集数量：{test_num}")
"""
    3、拷贝
"""
import shutil
src_path = r"C:\Users\33122\Desktop\01Python语法\21文件和目录操作\data"
dst_path =r"C:\Users\33122\Desktop\01Python语法\21文件和目录操作\dataset"

# 先拷贝测试集
for j  in range(len(datasetName)):
    for i in range(numStruct[j]):
        src =os.path.join(src_path,img_list[i])  #fr"C:\Users\33122\Desktop\01Python语法\21文件和目录操作\data\{img_list[i]}"
        shutil.copy(src, os.path.join(dst_path, datasetName[j]))
        print(f"{src}已写入...")



