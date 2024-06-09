from datetime import detatime
import time
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def task3():
    await asyncio.sleep(4)
    print("Task 3 completed")

async def task4():
    await asyncio.sleep(5)
    print("Task 4 completed")

async def main():
    print(datetime.now())
    await asyncio.gather(task1(), task2())
    print(datetime.now())

if __name__ == "__main__":
    asyncio.run(main())