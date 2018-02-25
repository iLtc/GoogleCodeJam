T = int(input())

for t in range(T):
    N = int(input())

    temp = input().split()
    temp = list(map(int, temp))

    GBuses = []

    for n in range(N):
        city1 = temp[2 * n]
        city2 = temp[2 * n + 1]
        if city1 < city2:
            GBuses.append((city1, city2))
        else:
            GBuses.append((city2, city1))

    P = int(input())

    results = []

    for p in range(P):
        city = int(input())

        result = 0

        for GBus in GBuses:
            if GBus[0] <= city <= GBus[1]:
                result += 1

        results.append(result)

    results = list(map(str, results))
    print("Case #{}: {}".format(t + 1, " ".join(results)))

    input()
