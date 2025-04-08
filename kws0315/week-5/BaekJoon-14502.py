from itertools import combinations
from copy import deepcopy
from collections import deque
from sys import stdin

input = stdin.readline

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    def _bfs():
        board = deepcopy(graph)
        virus_cnt = 0
        queue = deque(virus)
        while queue:
            x, y = queue.popleft()
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    board[nx][ny] = 2
                    virus_cnt += 1
                    queue.append((nx, ny))
        return len(safe_area) - virus_cnt - 3
    safe_area = []
    virus = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                safe_area.append((i, j))
            elif graph[i][j] == 2:
                virus.append((i, j))
    res = 0
    for wall_list in combinations(safe_area, 3):
        for x, y in wall_list:
            graph[x][y] = 1
        res = max(res, _bfs())
        for x, y in wall_list:
            graph[x][y] = 0
    return res

if __name__ == '__main__':
    # Input
    N, M = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]

    # Solve & Output
    print(bfs())
