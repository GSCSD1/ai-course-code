"""
    isdigit 判断是否只包含数字
    isalpha 判断是否只包含字母
    isalnum  判断是否只包含字母或数字
    isspace  判断是否只包含空格
    startswith  是否以某字符串开头
    endswith    是否以某字符串结尾
"""
str1 = "@123*"

print(str1.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isspace())
print(str1.isspace())
print(str1.startswith('@'))
print(str1.endswith('*'))

