from heapq import heappush, heappop
from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    heap = []
    res = []

    # Input
    for _ in range(int(input())):
        x = int(input())

        # Solve
        if x == 0:
            # if문으로 heap이 Empty하면 0을 append한다.
            res.append(heappop(heap) if heap else 0)
        else: #0이 입력되기 전까지 값을 받는다.
            heappush(heap, x)

    # Output
    print(*res, sep='\n')