from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

if __name__ == '__main__':
    heap = []
    res = []

    # Input
    for _ in range(int(input())):
        X = int(input())

        # Solve
        if X == 0:
            res.append(heappop(heap)[1] if heap else 0)
        else:
            heappush(heap, (abs(X), X))

    # Output
    print(*res, sep='\n')