##
异步编程中的“非阻塞”指的是在等待 I/O 操作的过程中，程序不会阻塞 CPU 的执行，而是允许 CPU 去处理其他任务。任务的执行是“非连续”的，即它们可以在多个时间点占用 CPU，之间可以暂停等待 I/O 结果

## 事件循环
import asyncio

async def fetch_data():
    print("开始获取数据...")
    await asyncio.sleep(1)  # 模拟 I/O 操作，暂停 1 秒
    print("数据获取完毕")
    return "数据内容"

async def main():
    result = await fetch_data()
    print(result)

# 运行一个事件循环并执行主协程
asyncio.run(main())


## 创建与并发运行多个协程任务
import asyncio

async def coroutine_1():
    await asyncio.sleep(2)
    print("job 1 finished")

async def coroutine_2():
    await asyncio.sleep(1)
    print("job 2 finished")

async def main():
    task1 = asyncio.create_task(coroutine_1())
    task2 = asyncio.create_task(coroutine_2())
    await task1
    await task2
    # await task1, task2

asyncio.run(main())


## asyncio.gather() 会并发运行多个协程并返回它们的结果
import asyncio

async def coroutine_1():
    await asyncio.sleep(2)
    print('1 finished')
    return 'from1'

async def coroutine_2():
    await asyncio.sleep(1)
    print('2 finished')
    return 'from2'

async def main():
    results = await asyncio.gather(coroutine_1(), coroutine_2())
    # results = await asyncio.gather(*[coroutine_1(), coroutine_2()])
    print(results)

asyncio.run(main())


##
import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    html = await fetch_url('http://example.com')
    print(html)

asyncio.run(main())
