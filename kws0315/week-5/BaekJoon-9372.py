from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    # Input
    res = []
    for _ in range(int(input())):
        N, M = map(int, input().split())
        for _ in range(M):
            input()

        # Solve
        res.append(N - 1)

    # Output
    print(*res, sep='\n')