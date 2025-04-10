# import asyncio
#
# async def mul(x,y):
#     return x**y
#
# loop=asyncio.get_event_loop()
# res=loop.run_until_complete(mul(5,5))
# print(res)
#
# import asyncio
#
# async def mul(x, y):
#     await asyncio.sleep(5)
#     return x*y
#
# loop = asyncio.new_event_loop()  #new_event_loop返回一个异步事件循环。事件循环是 需要执行异步代码
#
# res2 = loop.run_until_complete(mul(5, 5))#run_until_complete 函数运行事件循环，直到将来 完成了。它返回未来的结果，或引发其异常。未来 表示异步操作的最终结果
# print(res2)


import asyncio
import time


# async def main():
#     print("hello")
#     # await asyncio.sleep(6)
#     print("word")
#
# def test_o():
#     # time.sleep(5)
#     print("进程")
# asyncio.run(main())
# test_o()


# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#     print(f"finished at {time.strftime('%X')}")
# asyncio.run(main())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def main():
    task1 = asyncio.create_task(say_after(0, 'hello'))
    task2 = asyncio.create_task(say_after(0, 'world'))
    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())


