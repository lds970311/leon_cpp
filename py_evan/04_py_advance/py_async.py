# coding:utf-8
# time: 2023/5/12
# author: evan
# Python异步
import asyncio
import random


async def a():
    for i in range(10):
        print(i, 'a')
        await asyncio.sleep(random.random() * 2)

    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b')
        await asyncio.sleep(random.random() * 3)

    return 'b function'


async def main():
    result = await asyncio.gather(
        a(),
        b(),
    )
    print(result)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(b())
