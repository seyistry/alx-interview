#!/usr/bin/python3
import sys


def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if (len(sys.argv) == 2):
    try:
        if (int(sys.argv[1]) >= 4):
            for solution in queens(int(sys.argv[1]), 0, [], [], []):
                for item in range(len(solution)):
                    solution[item] = [item, solution[item]]
                print(solution)
        else:
            print("N must be at least 4\n")
            sys.exit(1)
    except ValueError as e:
        print("N must be a number\n")
        sys.exit(1)
else:
    print("Usage: nqueens N\n")
    sys.exit(1)
