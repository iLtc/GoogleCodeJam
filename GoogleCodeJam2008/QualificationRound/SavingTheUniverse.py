N = int(input())

for n in range(N):
    S = int(input())
    search_engines = []

    for s in range(S):
        search_engines.append(input())

    Q = int(input())
    queries = []

    for q in range(Q):
        queries.append(input())

    if len(queries) > 0:
        switches = -1
    else:
        switches = 0

    while len(queries) > 0:
        max_index = -1

        for search_engine in search_engines:
            if search_engine not in queries:
                max_index = len(queries)
                break

            index = queries.index(search_engine)

            if index > max_index:
                max_index = index

        queries = queries[max_index:]
        switches += 1

    print("Case #{}: {}".format(n + 1, switches))

