T = int(input()) # Number of test cases
for i in range(T):
    N= int(input())
    V = [int(s) for s in input().split(" ")]
    result = 0
    current_max = V[0]
    if (N > 1) & (V[0] > V[1]):
        result += 1
    for j in range(1, N-1):
        if (V[j] > current_max) & (V[j] > V[j+1]):
            result += 1
            current_max = V[j]
    if V[N-1] > current_max:
        result += 1
    print("Case #{}: {}".format(i+1, result))