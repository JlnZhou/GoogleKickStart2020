import numpy as np
T = int(input())
for i in range(T):
    N, B = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")]
    A.sort()
    A_cumsum = np.cumsum(A)
    res = 0
    for j in range(N):
        if A_cumsum[j] <= B:
            res += 1
    print("Case #{}: {}".format(i+1, res))