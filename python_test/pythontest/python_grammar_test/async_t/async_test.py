import asyncio
import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return delay
async def main():
    print(f"started at {time.strftime('%X')}")
    # 通过await等待运行，此时两个任务按顺序运行
    result1 = await say_after(2, 'hello')
    result2 = await say_after(1, 'world')
    print(result1, result2)
    task1 = asyncio.create_task(say_after(2, 'hello2'))
    task2 = asyncio.create_task(say_after(1, 'world2'))
    # 通过asyncio.task()包装为task然后await等待运行，此时两个任务并发运行
    result3 = await task1
    result4 = await task2
    print(result3, result4)
    print(f"finished at {time.strftime('%X')}")
# 通过asyncio.run()函数运行
asyncio.run(main())