import time
from datetime import datetime
def task1():
    time.sleep(2)
    print("call 1")

def task2():
    time.sleep(3)
    print("call 2")

def task3():
    time.sleep(5)
    print("call 3")

def task4():
    time.sleep(1)
    print("call 4")

def task5():
    time.sleep(7)
    print("call 5")

def task6():
    time.sleep(2)
    print("call 6")

def task7():
    time.sleep(1)
    print("call 7")

def task8():
    time.sleep(3)
    print("call 8")

def task():
    print(datetime.now())
    task5()
    task7()
    task1()
    task2()
    task3()
    task4()
    task6()
    task8()
    print(datetime.now())

if __name__ == "__main__":
    task()
