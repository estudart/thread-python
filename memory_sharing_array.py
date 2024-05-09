from multiprocessing import Process, Array
import time

def increment(shared_array, start_index, value_inc):
    for i in range(start_index, start_index + 5):
        time.sleep(0.1)
        with shared_array.get_lock():
            shared_array[i] += value_inc
            print(f"Element {i} inc by {value_inc}")

if __name__ == '__main__':
    shared_array = Array('i', 10)
    p1 = Process(target=increment, args=(shared_array, 0, 1))
    p2 = Process(target=increment, args=(shared_array, 5, 3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"shared_array: {list(shared_array)}")
