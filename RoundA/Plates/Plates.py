import numpy as np
T = int(input())
for i in range(T):
#    print("Case #{}".format(i+1))
    N, K, P = [int(s) for s in input().split(" ")]
    plates = [[] for j in range(N)]
    for j in range(N):
        plates[j] = [int(s) for s in input().split(" ")]
#    print("Case #{}: Inputs OK".format(i+1))
    plates_cumsum = [[] for j in range(N)]
    for j in range(N):
        plates_cumsum[j] = np.cumsum(plates[j])
    cumulative_res = plates_cumsum[0].copy() # With one stack of plates
    # The values in cumulative_res[p-1] contains the solution for p plates and the stacks considered
#    print("Case #{}: Cumsum OK".format(i+1))
    if N == 1:
        res = cumulative_res[P-1]
        print("Case #{}: {}".format(i+1, res))
    else:
        for n in range(1, N): # We incrementally include the remaining stacks
#            print("Case #{}: Include stack {}".format(i+1, n+1))
            old_cumulative_res = cumulative_res.copy() 
            for p in range(len(cumulative_res)): # We update the pth values
#                print("Case #{}: p = {}".format(i+1, p))
                for k in range(1, min(p, K+1)): #k is the number of plates taken from the new stack
#                    print("Case #{}: k = {}".format(i+1, k))
                    cumulative_res[p] = max(cumulative_res[p], plates_cumsum[n][k-1] + old_cumulative_res[p-k])
                if p < K:
                    cumulative_res[p] = max(cumulative_res[p], plates_cumsum[n][p])
            if len(old_cumulative_res) < P: # if there are not enough plates taken into account so far
#                print("Case #{}: Extend cumulative result".format(i+1))
                for p in range(len(old_cumulative_res), P):
                    cumulative_res = np.append(cumulative_res, old_cumulative_res[-1])
                    for k in range(1,K+1):
                        cumulative_res[-1] = max(cumulative_res[-1], plates_cumsum[n][k-1] + old_cumulative_res[p-k])
        res = cumulative_res[P-1]
        print("Case #{}: {}".format(i+1, res))
#    print("OK")