import threading

shared_list = []

list_condition = threading.Condition()

def add_to_list(n):
    global shared_list
    with list_condition:
        shared_list.append(n)
        list_condition.notify()
        print(f"Number {n} appended to list: {shared_list}")

t1 = threading.Thread(target=add_to_list, args=(1,))
t2 = threading.Thread(target=add_to_list, args=(2,))
t3 = threading.Thread(target=add_to_list, args=(3,))
t4 = threading.Thread(target=add_to_list, args=(4,))

def main():
    t1.start()
    t3.start()
    t2.start()
    t4.start()

main()