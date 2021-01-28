T = int(input()) # Number of test cases
for i in range(T):
    # N number of bus routes
    # We count the K-countdowns
    N, K = [int(s) for s in input().split(" ")]
    # A Array of integers
    A = [int(s) for s in input().split(" ")]
    nb = 0
    current = 0
    for j in range(1,N):
        if (A[j] == A[j-1] - 1):
            current += 1
        else:
            current = 0
        if (A[j] == 1) & (current >= (K-1)):
            nb += 1
    print("Case #{}: {}".format(i+1, nb))