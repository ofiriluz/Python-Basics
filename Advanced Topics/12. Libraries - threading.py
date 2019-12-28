# Threading support is simillar to any other language
# And is easily used in python, along with locking mechanisms
# Threading library is commonly used for threads and different types of locks
# However it contains more objects such as semaphors and events and timers
import threading
import time

global_counter = 1
# We can create a global lock and acquire / release it like any normal lock
global_lock = threading.Lock()

def f1():
    global global_counter
    global global_lock
    global_lock.acquire()
    time.sleep(3.0)
    global_counter+=1
    global_lock.release()

def f2(some_args, more_args):
    time.sleep(5.0)

class A:
    def f3(self):
        time.sleep(3.0)

if __name__ == "__main__":
    # We can easily create and start threads and given them args
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f1)
    t3 = threading.Thread(target=f2, args=('5', 'ads',))
    # We can also use it for object methods
    a = A()
    t4 = threading.Thread(target=a.f3)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()