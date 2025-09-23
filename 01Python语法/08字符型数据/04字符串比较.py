"""

   A  <  a
    字符串比较：字符串比较是逐个字符的ASCII码值进行比较，如果两个字符的ASCII码值
    相同，就会继续比较下一个字符
"""
print(ord('A'))
print(ord('a'))
print('A'  <  'a')  # True

s1 = "abcd123"
s2 = "abCd123"

print(s1  <  s2)  # False