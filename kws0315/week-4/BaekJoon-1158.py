from collections import deque
from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    # Input
    N, K = map(int, input().split())
    queue = deque(range(1, N + 1))
    res = []
    # Solve
    while queue:
        for _ in range(K - 1):
            queue.append(queue.popleft())
        res.append(str(queue.popleft()))
    # Output
    print('<' + ', '.join(res) + '>')
