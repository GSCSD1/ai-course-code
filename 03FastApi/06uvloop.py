"""
    uvloop 第三方事件循环 将asynicIO中事件循环替换为uvloop
    性能可以提高三倍  和go语言比肩
"""
import asyncio
import uvloop

async def nested():
    print('进入IO')
    await  asyncio.sleep(1)
    print('结束IO')
    return 42

async def main():
    # 方法1
    # task1 =  asyncio.create_task(nested())
    # task2 = asyncio.create_task(nested())
    # res1 =  await task1
    # res2 = await task2
    # print(res1,res2)
    # 方法2
    # done : 存放执行完成的任务
    # pending: 默认不填  当指定timeout参数时  存放未执行完成的任务
    done,pending = await asyncio.wait([asyncio.create_task(nested(),name='a'),asyncio.create_task(nested(),name='b')])
    print(done)

    for task in done:  # py3.8之后每个任务会有name属性,可以通过该属性区分不同任务
        print(task.get_name(),task.result())

# 执行main函数
asyncio.run(main())