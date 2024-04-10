import threading, time

def background_task():
    while True:
        time.sleep(1)
        print("Background task running...")

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

time.sleep(2)
print("Main program complete")