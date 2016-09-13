import threading


class LukesMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = LukesMessenger(name="SEND OUT MSGS")
y = LukesMessenger(name="RECEIVE MSGS")
x.start()
y.start()

'''threads run at the same time they ignore reading code line by line
they are useful for programs that need to run simultaneously'''

