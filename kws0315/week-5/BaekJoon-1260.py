from sys import stdin
from collections import deque
input = stdin.readline

def dfs(start):
    visited[start] = True
    res_dfs.append(start)
    for v in graph[start]:
        if not visited[v]:
            dfs(v) # 재귀함수로 방문했을 때, 다시 위로 올라간다.

def bfs(start):
    visited[start] = True
    res_bfs.append(start)
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for v in graph[cur]:
            if not visited[v]:
                visited[v] = True # 방문 표시
                res_bfs.append(v)
                queue.append(v) # 큐에 넣어준다. (각 레벨별로 탐색한다)

if __name__ == '__main__':
    # Input
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)] # 간선을 추가하기 위해서 빈 2차원 리스트를 생성(빈 값으로 +1해서
                                       # 모든 코드의 x-1, y-1을 뺴준다. (코드를 간략하게 구성
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, N + 1): # 만들어진 그래프 정보 확인
        print(i, ":", graph[i])

    # DFS 탐색 후 결과를 담을 리스트 res_dfs
    res_dfs = []
    visited = [False] * (N + 1)
    dfs(V)

    res_bfs = []
    visited = [False] * (N + 1)
    bfs(V)

    print(*res_dfs)
    print(*res_bfs)