#!/usr/bin/python3
import sys

def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    def dfs(curr, cols, main_diag, anti_diag, result):
        row, n = len(curr), len(cols)
        if row == n:
            result.append(map(lambda x: '.'*x + "Q" + '.'*(n-x-1), curr))
            return
        for i in range(n):
            if cols[i] or main_diag[row+i] or anti_diag[row-i+n]:
                continue
            cols[i] = main_diag[row+i] = anti_diag[row-i+n] = True
            curr.append(i)
            dfs(curr, cols, main_diag, anti_diag, result)
            curr.pop()
            cols[i] = main_diag[row+i] = anti_diag[row-i+n] = False

    result = []
    cols, main_diag, anti_diag = [False]*n, [False]*(2*n), [False]*(2*n)
    dfs([], cols, main_diag, anti_diag, result)
    print(result[1])
    return result

if (len(sys.argv) == 2):
    try:
        if (int(sys.argv[1]) >= 4):
            solveNQueens(int(sys.argv[1]))
        else:
            print("N must be at least 4\n")
            sys.exit(1)
    except TypeError as e:
        print("N must be a number\n")
        sys.exit(1)
else:
    print("Usage: nqueens N\n")
    sys.exit(1)


