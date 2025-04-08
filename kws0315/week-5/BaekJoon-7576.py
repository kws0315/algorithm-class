from collections import deque
from sys import stdin

input = stdin.readline


def bfs():
    queue = deque([])
    empty_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j)) # 익은 토마토의 위치 정보를 Queue에 담는다.
            elif graph[i][j] == -1:
                empty_cnt += 1
    if len(queue) + empty_cnt == N * M: # 익은 토마토와 비어있는 칸을 더했을 때, 동일하다면 0을 배출해야한다. (처음부터 익어있는 상태)
        return 0
    day = -1
    same_level = 0 # same Level로 토마토가 익은 날짜를 뱉어낸다.
    cnt = len(queue) # 맨 처음에 익은 토마토 체크

    while queue:
        if same_level == 0:
            same_level = len(queue)
            day += 1 # 언제 하루가 지났는지 체크 (same_level이 0이 될 때마다 체크)
        x, y = queue.popleft() # 0일 째에 익은 토마토를 뺀다.
        for dx, dy in D: # 인접한 애들을 하나씩 보면서 좌표가 유효한지 찾아본다.
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: # 익지 않은 토마토인지 체크한다.
                cnt += 1 # 익은 토마토가 있으면 +1 해준다.
                graph[nx][ny] = 1
                queue.append((nx, ny))
            same_level -= 1
            return day if cnt + empty_cnt == N * M else -1 # 같지 않다면 -1을 출력한다 (안 익는 토마토가 존재함)



if __name__ == '__main__':
    # Input
    M, N = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]

    # Solve & Output
    print(bfs())