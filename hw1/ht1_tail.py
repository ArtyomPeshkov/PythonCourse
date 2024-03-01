import sys

if __name__ == "__main__":
    input = []
    limit = 10
    cnt = 0

    if len(sys.argv) < 2:
        limit = 17
        input.append(sys.stdin.read().split("\n"))
        input[0].pop()
    else:
        for i in range(len(sys.argv) - 1):
            input.append(open(sys.argv[i + 1], 'r'))

    for file in input:
        if len(sys.argv) > 2:
            print("==> " + sys.argv[cnt + 1] + " <==")
        cnt += 1
        lines = [line.rstrip() for line in file]
        for line in lines[-limit:]:
            print(line)
        if len(sys.argv) > 2:
            print("")
