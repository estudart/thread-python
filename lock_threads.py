import threading

balance = 0

# a lock object
balance_lock = threading.Lock()

def update_balance(amount):
    global balance
    # the lock acquisition
    with balance_lock:
        print(f"Balance before update: {balance}")
        balance += amount
        print(f"Balance after update: {balance}")


t1 = threading.Thread(target=update_balance, args=(100,))
t2 = threading.Thread(target=update_balance, args=(-50,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final balance: {balance}")