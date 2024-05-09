from multiprocessing import Process
import time

def worker(num):
    # Thread worker function
    print(f"Worker {num} is starting")
    time.sleep(2)
    print(f"Worker {num} is finishing")

if __name__ == '__main__':
    processes = []
    # create and start new processess
    for i in range(5):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    # wait for all to finish
    for p in processes:
        p.join()