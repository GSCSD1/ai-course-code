"""
    if 条件表达式：
        条件成立 执行要做的事情

    让程序学会做选择
"""

# money =   int(input("请输入你的存款"))

# if money >=10_000_000:
#     print("尊敬的至尊超级会员，欢迎来到超级会员专区")


"""
        if - else
        
         if 条件表达式：
                条件成立 执行要做的事情
        else:
            不满足条件 执行要做的事情
"""
age = 3
if age>=18:
    print("恭喜你，可以上网")
else:
    print("移步到黑网吧去")

"""
    if 条件表达式1：
                条件成立 执行要做的事情
    elif 条件表达式2:
                条件成立 执行要做的事情
    elif 条件表达式3:
                条件成立 执行要做的事情
                ....
    else:
        不满足条件 执行要做的事情

"""
# goods =  input("请输入要购买的商品:")
#
# if goods =="iphone":
#     print("恭喜你选择了肾机，友情提示： 买完记得吃点好的，补补腰子")
# elif goods == "华为平板":
#     print("国货之光，买了它，你就是爱国青年")
# elif goods =="小米电视":
#     print("小米电视，性价比之神")
# else:
#     print(f"你输入{goods}不在列表中，商品已记录，改天来购买。")
"""
    在线购物平台优惠券系统
    根据用户购车总额和会员等级，系统提供不同等级的折扣    
    
    1、如果用户是vip,购物总额超过100，提供20%折扣
    2、如果用户不是vip,但购物总额超过50,  提供10%折扣
    3、如果用户不是vip，购物总额不超过50，不提供任何折扣
    特殊情况：如果用户是vip，但购物车总额不超过100，也提供5%折扣
"""
is_vip = True
cart_total =200
disscount_rate = 0

if is_vip:
    if cart_total>100:
        disscount_rate = 0.2
    elif 0<=cart_total<=100:
        disscount_rate = 0.05
else:
    if cart_total > 50:
        disscount_rate = 0.1
    elif 0 <= cart_total <= 50:
        disscount_rate = 0

# if is_vip and  cart_total>100:
#     disscount_rate = 0.2
# elif not is_vip and cart_total>50:
#     disscount_rate = 0.1
# elif not is_vip and cart_total<50:
#     disscount_rate = 0
# else:
#     if is_vip and cart_total<100:
#        disscount_rate = 0.05

print(f"用户最后的折扣为{disscount_rate:.0%}")


"""
    公司内部资源权限问题
    员工可以访问不同的系统资源，取决于他们的职位和完成数量，权限规则如下：
    1、经理可以访问所有资源
    2、普通员工，完成5个以上的任务以后才能访问所有资源
    3、实习生完成10个任务以后，经过经理批准才能访问
"""
role = 1
completed_tasks =   10  
is_manager_approved = False

acess_allowd = (role == 1)or\
               (role == 2 and completed_tasks>=5)or\
               (role == 3 and completed_tasks>=10 and is_manager_approved)
if acess_allowd:
    print("有权访问")
else:
    print("无权访问")

# if role == 1:
#     print("经理可以访问所有资源")
# elif role == 2 and completed_tasks>=5:
#     print("普通员工可以访问所有资源")
# elif role == 3 and completed_tasks>=10 and is_manager_approved:
#     print("实习生可以访问所有资源")
# else:
#     print("无权访问")