import threading

def worker():


    print("Thread is running")


threads = []


for i in range(5):


    t = threading.Thread(target=worker)


    threads.append(t)


    t.start()



