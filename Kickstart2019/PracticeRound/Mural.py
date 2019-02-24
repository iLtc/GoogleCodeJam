import math

T = int(input())

for t in range(T):
    n = int(input())

    beauty_scores = list(map(int, list(input())))

    max_len = math.ceil(n / 2)

    beauty = sum(beauty_scores[:max_len])

    max_beauty = beauty

    for i in range(n - max_len):
        beauty = beauty - beauty_scores[i] + beauty_scores[i + max_len]

        if max_beauty < beauty:
            max_beauty = beauty

    print("Case #{}: {}".format(t + 1, max_beauty))
