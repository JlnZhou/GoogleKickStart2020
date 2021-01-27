T = int(input())
for i in range(T):
    N = int(input())
    H = [int(s) for s in input().split(" ")]
    peak_nb = 0
    for j in range(1,(N-1)):
        if (H[j] > H[j-1])&(H[j] > H[j+1]):
            peak_nb += 1
    print("Case #{}: {}".format(i+1, peak_nb))