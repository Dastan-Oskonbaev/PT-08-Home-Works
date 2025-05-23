# async def say_hello():
#     print("Hello World!")
#
#
# coroutine = say_hello()
# print(coroutine)
import asyncio


# import asyncio
#
#
# async def hello():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#
#
# asyncio.run(hello())\


# import asyncio, time
#
#
# async def coro(tag, delay):
#     t0 = time.perf_counter()
#     await asyncio.sleep(delay)
#     print(tag, "done in", f'{time.perf_counter() - t0:.2f}s')
#
#
# async def main():
#     await asyncio.gather(
#         coro("Поиск в интернете", 8),
#         coro("Запрос на чат", 4),
#         coro("Запрос на Генерацию изображения", 5),
#         coro("Запрос в бд", 3)
#     )
#
#
# asyncio.run(main())


# import asyncio
# import time
#
#
# async def fake_request(name, delay):
#     await asyncio.sleep(delay)
#     return f"{name} ok"
#
#
# async def sequential():
#     t0 = time.perf_counter()
#     await fake_request("A", 1)
#     await fake_request("B", 1)
#     print("Sequential time:", time.perf_counter() - t0)
#
#
#
# async def parallel():
#     t0 = time.perf_counter()
#     await asyncio.gather(
#         fake_request("A", 1),
#         fake_request("B", 1),
#     )
#     print("Parallel time:", time.perf_counter() - t0)
#
#
# asyncio.run(sequential())
# asyncio.run(parallel())




# import asyncio
#
#
# async def long():
#     await asyncio.sleep(2)
#     return "Hello"
#
#
# async def main():
#     task = asyncio.create_task(long())
#     print("Doing something")
#     await asyncio.sleep(1)
#     print("Result", await task)
#
#
# asyncio.run(main())


# import asyncio, random
#
# sem = asyncio.Semaphore(2)
#
#
# async def download(i):
#     async with sem:
#         await asyncio.sleep(random.uniform(0.5, 1.5))
#         print(f"file {i} downloaded")
#
#
# async def main():
#     await asyncio.gather(*(download(i) for i in range(10)))
#
#
# asyncio.run(main())


hp = 100
v_lave = 0

async def fire():
    global v_lave, hp
    print('вы горите')
    while hp <= 0:
        await asyncio.sleep(0.5)
        hp -= 2
        print('-2')


async def main():
    print('перед вами лавы прыгнуть туда  ?')
    while 1:
        jump = input('ДА: ')
        if  jump.lower() == 'да':
            print('lol')
            v_lave = 1
            task = asyncio.create_task(fire())
            await task
        elif jump == 'НЕТ':
            v_lave = 0


asyncio.run(main())


