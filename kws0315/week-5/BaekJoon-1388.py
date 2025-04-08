from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    # Input
    N, M = map(int, input().split())
    board = [[*input().rstrip()] for _ in range(N)] # 바닥타일을 받아온다.

    # Solve
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'X': #방문한 곳은 건너 뛴다. (cnt 증가X)
                continue

            cnt += 1 # continue하지 않으면 타일이 생성된 것이니 때문에 일단 cnt를 +1해준다.
            if board[i][j] == '-': # j번부터 열크기만큼 열을 탐색한다.
                for y in range(j, M):
                    if board[i][y] != '-': # '-'가 발견되면 break 후 'X'로 변경하고 다시 측정되는 것을 방지
                        break
                    board[i][y] = 'X' # X로 바꿔서 하나로 취급해준다. Ex) 01, 02가 -, -라면 02를 X로 바꿔서
                                      # 검색되지 않도록 변경한다.
            if board[i][j] == '|':
                for x in range(i, N): # i번부터 행크기만큼 행을 탐색한다.
                    if board[x][j] != '|':
                        break
                    board[x][j] = 'X'
    # Output
    print(cnt)
