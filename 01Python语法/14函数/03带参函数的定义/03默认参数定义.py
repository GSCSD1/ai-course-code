
# 默认参在定义时，直接对形参赋值，必须放在形参的最右边
# 如果允许默认参可以放在任何位置会导致和位置参数矛盾
def setData(Day,Month,Year=2025):
    print(f"设置成功，日期为：{Day}/{Month}/{Year}")

# 默认参数在传递时，如果不需要修改默认参数的值，可以不传递
setData(Day = 10,Month=7)
# setData(10,7,2026)