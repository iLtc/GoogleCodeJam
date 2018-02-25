"""
from copy import deepcopy

previous = ['0', '0', '1']

for _ in range(18):
    temp = deepcopy(previous)
    i = len(temp) // 2
    temp[i] = '1'

    previous = previous + ['0'] + temp

T = int(input())

for t in range(T):
    k = int(input())

    print("Case #{}: {}".format(t + 1, previous[k - 1]))
"""


def helper(k, lengths):
    if k == 1:
        return 0

    if k == 2:
        return 0

    small = 0
    for i in range(len(lengths)):
        if lengths[i] < k <= lengths[i + 1]:
            small = i
            break

    if k == lengths[small] + 1:
        return 0

    k -= (lengths[small] + 1)

    if 2 * k - 1 == lengths[small]:
        return 1

    return helper(k, lengths)


lengths = [1]
current = 1

for i in range(59):
    current = current * 2 + 1
    lengths.append(current)

T = int(input())

for t in range(T):
    k = int(input())

    result = helper(k, lengths)
    print("Case #{}: {}".format(t + 1, result))

