import sys

T, N = list(map(int, input().split()))

for t in range(T):
    for x in range(N - 1):
        print("M " + str(x + 1)  + " " + str(N))
        sys.stdout.flush()
        idx = int(input())
        if idx != x + 1:
            print("S " + str(x + 1) + " " + str(idx))
            sys.stdout.flush()
            input()
    print("D")
    sys.stdout.flush()
    input()