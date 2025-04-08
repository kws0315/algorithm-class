from collections import deque
from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    # Input
    X = int(input())

    # Solve
    queue = deque([(X, 0)])
    while queue:
        x, cnt = queue.popleft() #X를 빼서 x와 cnt에 부여한다.
        if x == 1:
            # Output
            print(cnt)
            break
        if x % 3 == 0:
            queue.append((x // 3, cnt + 1))
        if x % 2 == 0:
            queue.append((x // 2, cnt + 1))
        queue.append((x - 1, cnt + 1))
        print(queue)