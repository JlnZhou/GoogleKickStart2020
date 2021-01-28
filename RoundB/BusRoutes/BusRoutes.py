T = int(input()) # Number of test cases
for i in range(T):
    # N number of bus routes
    # the journey has to be finished by day D
    N, D = [int(s) for s in input().split(" ")]
    # Bus routes availability days
    X = [int(s) for s in input().split(" ")]
    journey_beginning = D
    for j in reversed(range(N)):
        journey_beginning = journey_beginning - (journey_beginning%X[j])
    print("Case #{}: {}".format(i+1, journey_beginning))