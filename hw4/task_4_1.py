import time
import threading
import multiprocessing

N = 38

def fib(n):
    if (n <= 1):
        return n
    return fib(n - 1) + fib(n - 2)

def baseline(n):
    for _ in range(10):
        fib(n)

def thread(n):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fib, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def multiprocess(n):
    multiprocesses = []
    for _ in range(10):
        multiprocess = multiprocessing.Process(target=fib, args=(n,))
        multiprocess.start()
        multiprocesses.append(multiprocess)

    for multiprocess in multiprocesses:
        multiprocess.join()

if __name__ == "__main__":
    start = time.time()
    baseline(N)
    end = time.time()
    print("Baseline: ", end="")
    print(end - start)

    start = time.time()
    thread(N)
    end = time.time()
    print("Thread: ", end="")
    print(end - start)

    start = time.time()
    multiprocess(N)
    end = time.time()
    print("Multiprocess: ", end="")
    print(end - start)