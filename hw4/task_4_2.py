import math
import time
import logging
import concurrent.futures

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate_part(f, a, begin, end, step):
    res = 0
    for i in range(begin, end):
        res += f(a + i * step) * step
    return res

def integrate_parallel(f, a, step, executor, n_jobs, n_iter, log):
    logging.debug(log)
    acc = 0
    
    subs = []
    part = (n_iter // n_jobs)
    for i in range(n_jobs):
        begin = i * part
        end = begin + part
        if i == n_jobs - 1:
            end = n_iter

        subs.append(executor.submit(integrate_part, f, a, begin, end, step))
    
    for submission in subs:
        acc += submission.result()
    
    return acc

if __name__ == "__main__":
    logging.basicConfig(filename="./artifacts/artifacts_4_2_logs.txt", filemode="w", level=logging.DEBUG, format='%(asctime)s: %(message)s')

    n_iter = 10000000
    f = math.cos
    a = 0
    b = math.pi / 2
    step = (b - a) / n_iter

    cpu_num = 6

    print("Thread:")
    for n_jobs in list(range(1, cpu_num*2+1)):
        executor = concurrent.futures.ThreadPoolExecutor()
        start = time.time()
        integrate_parallel(f, a, step, executor, n_jobs, n_iter, f"Started integrating with {n_jobs} threads")
        end = time.time()
        print(f"{n_jobs}: {end - start}")
    print()

    print("Multiprocess:")
    for n_jobs in list(range(1, cpu_num*2+1)):
        executor = concurrent.futures.ProcessPoolExecutor()
        start = time.time()
        integrate_parallel(f, a, step, executor, n_jobs, n_iter, f"Started integrating with {n_jobs} processes")
        end = time.time()
        print(f"{n_jobs}: {end - start}")