t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))
    a += 1

    n = int(input())

    for i in range(n):
        guess_num = (a + b) // 2

        print(guess_num)

        result = input()

        if result == 'CORRECT':
            break

        elif result == 'TOO_SMALL':
            a = guess_num + 1

        elif result == 'TOO_BIG':
            b = guess_num - 1

        else:
            if i == n - 1:
                continue

            else:
                exit()

