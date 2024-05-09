from multiprocessing import Process, Value
import time

def increment(shared_value):
    for i in range(10):
        time.sleep(0.1)
        with shared_value.get_lock():
            shared_value.value += 1

if __name__ == '__main__':
    # shared numeric value, init with 0
    counter = Value('i', 0)
    p1 = Process(target=increment, args=(counter,))
    p2 = Process(target=increment, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"the counter value: {counter.value}")
