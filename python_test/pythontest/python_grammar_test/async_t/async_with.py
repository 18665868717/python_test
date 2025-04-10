import asyncio

#__aenter__ 开始执行协程函数
#__aexit__ 结束执行协程函数
class MyAsyncContextManager:
    async def __aenter__(self):
        # 异步资源的获取
        await asyncio.sleep(1)
        print("获取资源")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步资源的释放
        await asyncio.sleep(1)
        print("释放资源")

async def main():
    async with MyAsyncContextManager():
        # 异步资源的使用
        await asyncio.sleep(1)
        print("使用资源")

asyncio.run(main())