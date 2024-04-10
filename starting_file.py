import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number from thread: {i}")


number_thread = threading.Thread(target=print_numbers)
number_thread.start()
number_thread.join()
print("Finish thread")