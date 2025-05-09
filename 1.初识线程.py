###创建了俩个线程thread1 和thread2，并启动


import threading
import time 

def print_message(threading_name, delay):
    for i in range(3):
        print(f"{threading_name} is running{time.ctime(time.time())}")

thread1 = threading.Thread(target=print_message, args=("Thread 1", 1))
thread2 = threading.Thread(target=print_message, args=("Thread 2", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("退出主线程")
