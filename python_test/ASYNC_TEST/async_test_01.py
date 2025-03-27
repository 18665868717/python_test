import asyncio

# 协程函数
async def func():
    print("携程执行 ")

# 协程对象
result=func()

# 注意：执行协程函数创建协程对象，函数内部代码不会执行
asyncio.run(result)