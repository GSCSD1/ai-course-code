"""
    变量 ： 可能变化的量   钱 年龄 体重 身高  时间  头发
    常量： 一直不变的量    e  pi

    python数据类型  ：
        float int  bool complex str  list tuple set dict

    变量的三个基本属性：
                id号：内存地址

                类型 ： 数据类型
                值：存储的值
"""
my_float = 12.213
my_int = 12
my_bool = True
my_complex = 1 + 2j
my_str = "hello world"
my_list = [my_float, my_int, my_bool, my_str, [1231, 4213, 4123]]
my_tuple = (my_float, my_int, my_bool, my_str, [1231, 4213, 4123])
my_set = {my_float, my_int, my_bool, my_str}
my_dict = {"name": "job", "age": 10, "height": 23}
# 打印my_float内存地址
print(id(my_float))

"""
    注释 ： 
            单行注释 #  多行注释 ： """ """  ''' '''
"""

"""
    标识符 ： 见名知意
        描述姓名  
        小驼峰：myName   第一个单词首字母，其余单词首字母大写
        大驼峰：MyName     所有字母都要大写   所有首字母都要大写  
    格式化代码  ctrl+alt + l
"""
# 名字
my_name = "job"
myName = "job"
MyName = "job"
nName = "job"
