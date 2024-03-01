import sys
from sys import stdin

if __name__ == "__main__":
    input: str
    counter = 1

    if len(sys.argv) != 2:
        for line in stdin:
            if (line.rstrip() != ""):
                print(str(counter) + "\t" + line.rstrip())
                counter += 1
            else:
                print("")
            
    else:
        input = open(sys.argv[1], 'r')

    for line in input:
        print(str(counter) + "\t" + line.rstrip())
        counter += 1
