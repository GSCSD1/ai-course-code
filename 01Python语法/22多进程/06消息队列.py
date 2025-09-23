"""
    队列(排队) ： 先进先出队列
    栈(手枪子弹上膛) ： 后进先出队列
    queue.Queue()
        maxsize=0 : 队列容量，如果为0 无限内存

    Queue.get(item,timeout=None) 出列  数据空 如果timeout=None会一直等待入列一个元素
    Queue.get_nowait() 出列  数据空 直接报错

    Queue.put(item,timeout=None) 入列 数据满 如果timeout=None会一直等待出列一个元素
    Queue.put_nowait() 入列   数据满 直接报错
"""
import  queue

# # 实例化先进先出队列对象
# q = queue.Queue(5)
#
# # 入列 = 将元素存进去
# q.put(1)
# q.put("1234")
# q.put([123,5214,512])
# q.put((123,5214,512))
# q.put(2)
# # q.put(3)   # 数据满，一直等待，直到队列里面能存入下一个数据
# # q.put(3,timeout=3)   # 数据满，一直等待，直到队列里面能存入下一个数据
# q.put_nowait(3)  # # 数据满 直接报错
#
#
# # 出列 # 将元素取出来  取出来的顺序按照先进先出的规则
# print(q.get()) # 1
# print(q.get()) # "1234"
#
# print(q.get()) # [123,5214,512]
# print(q.get()) # (123,5214,512)

# print(q.get())  # 数据空 一直等待，直到有数据入列
# print(q.get(timeout=3))  #数据空 等待时间大于timeout 程序会直接报错
# print(q.get_nowait())  #数据空  直接报错

"""---------------------后进先出队列---------------------------------"""

# 实例化后进先出队列   put  get put_nowait  get_nowait
# LIFO  last in first out
# q =  queue.LifoQueue()
# q.put(1)
# q.put("1234")
# q.put([123,5214,512])
# q.put((123,5214,512))
# q.put(2)
# print(q.get())  # 2


"""---------------------优先级队列---------------------------------"""
# 实例化优先级队列
q = queue.PriorityQueue()  #数字越小，优先级越高
q.put((4,[1,34,534]))  # 第一个元素为优先级 第二个元素为数据
q.put((-1,[1,2,3]))
q.put((10,[4,5,6]))

print(q.get()) # 优先级高的先出列
print(q.get()) # 优先级高的先出列