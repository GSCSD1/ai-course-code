"""
    循环流程 ：  开始点 起点 计数：记圈  结束条件：跑完十圈   循环内容：跑步

    循环作用：
        1、避免重复、提高效率
        2、处理大批量数据（检查数据） 记录键盘 qwer 放技能  记事本打字
        3、条件不同次数不同  灵活控制程序行为

    while 循环条件:
        代码块
"""
# 模拟罚跑次数  10圈
TOTAL_LAPS = 10
# 记录圈数
current_lap = 0
# 什么时候  不执行循环  current_lap>=TOTAL_LAPS
while  current_lap < TOTAL_LAPS:
    # 计数  迭代点
    current_lap += 1
    print(f"跑步的人完成第{current_lap}圈")

# 输出1-100偶数
print(2)
print(4)
print(6)
num = 1
# 什么时候不执行循环 ： num >=   101
while num <  101:
    if num %2 == 0:
        print(num)
    num +=1

"""
    自动贩卖机：
        这个机器只支持硬币，假设只卖一种饮料，每瓶价格是5块
        用户需要一直投币，只到金额足够，机器才会提供饮料  
        币种：1,2,3元三种币种
"""
# 每瓶的价格
PRICE = 5
# 记录投币总金额
balance = 0
# 记录投币金额
coin = 0
# 什么时候不执行循环 ： balance>=PRICE
while balance<PRICE:
    coin = int(input("钱不够，请开始投币："))
    if coin==1 or coin == 2 or coin == 3:
        balance += coin
    else:
        print(f"对不起，不接受{coin}硬币,请重新投币")
# 找零
if  balance > PRICE:
    print(f"找零{balance-PRICE}")
print("购买成功")
