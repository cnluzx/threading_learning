import multiprocessing
import time


def print_message(threading_name, delay):
    for i in range(3):
        print(f"{threading_name} is running {time.ctime(time.time())}")
        time.sleep(delay)


if __name__ == '__main__':###windows下运行时，必须要加上这一句，否则会报错fork spown   

    process1= multiprocessing.Process(target=print_message,args=("Process1",2))
    process2= multiprocessing.Process(target=print_message,args=("Process2",4))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes are done")