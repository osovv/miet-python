import threading

def consumer(cond):
    with cond:
        print("Consumer before wait")
        cond.wait()
        print("Consumer after wait")

def producer(cond):
    with cond:
        print("Producer before notify")
        cond.notify()
        print("Producer after notify")

condition = threading.Condition()

c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
p = threading.Thread(name="p", target=producer, args=(condition,))

c1.start()
p.start()
