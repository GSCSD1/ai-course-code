
import  time
for i in range(101):
    print(f"进度:[{'=' * i + ' ' * (100 - i)}] {i}%", end='\n')    # 方式一
    # print(f"\r进度:[{'=' * i + ' ' * (100 - i)}] {i}%",end='')   # 方式二
    time.sleep(0.1)