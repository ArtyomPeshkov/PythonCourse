import time
import sys
import multiprocessing 
import codecs
import threading

def process_A_logic(queue, out_pipe):
    while True:
        line = queue.get().lower()
        out_pipe.send(line)
        if line == "exit":
            break
        time.sleep(5)

def process_B_logic(in_pipe, out_pipe):
    while True:
        line = in_pipe.recv()
        encoded = codecs.encode(line, 'rot_13')
        out_pipe.send(encoded)
        if line == "exit":
            break

def print_encoded(pipe):
    while True:
        encoded = pipe.recv()
        if (encoded == codecs.encode("exit", 'rot_13')):
            break
        print(time.strftime('%H:%M:%S'))
        print("Output: ", encoded)
        print()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    a_b_rec, a_b_snd = multiprocessing.Pipe()
    b_main_rec, b_main_snd = multiprocessing.Pipe()

    process_A = multiprocessing.Process(target=process_A_logic, args=(queue, a_b_snd))
    process_A.start()

    process_B = multiprocessing.Process(target=process_B_logic, args=(a_b_rec, b_main_snd))
    process_B.start()

    thread = threading.Thread(target=print_encoded, args=(b_main_rec,))
    thread.start()

    for line in sys.stdin:
        line = line.strip()
        queue.put(line)
        if (line == "exit"):
            break
        print(time.strftime('%H:%M:%S'))
        print("Input: ", line)
        print()

    process_A.join()
    process_B.join()
    thread.join()

