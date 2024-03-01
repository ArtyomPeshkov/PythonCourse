import sys
import os
 
if __name__ == "__main__":
    input = []
    cnt = 0

    if len(sys.argv) < 2:
        data = sys.stdin.read()
        print(len(data.split("\n")) - 1, end = " ")
        print(len(data.split()), end = " ")
        print(len(data.encode('utf-8')), end = " ")
    else:
        lines_t = 0
        words_t = 0
        bytes_t = 0
        
        for i in range(len(sys.argv) - 1):
            file = open(sys.argv[i + 1], 'r').read()
            lines = len(file.split("\n")) - 1
            words = len(file.split())
            bytes = os.path.getsize(sys.argv[i + 1])

            lines_t += lines
            words_t += words
            bytes_t += bytes

            print(lines, end = " ")
            print(words, end = " ")
            print(bytes, end = " ")
            print(sys.argv[i + 1])

        if (len(sys.argv) > 2):
            print(lines_t, end = " ")
            print(words_t, end = " ")
            print(bytes_t, end = " ")   
            print("total")


