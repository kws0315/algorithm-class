from sys import stdin
import math
input = stdin.readline

if __name__ == '__main__':
    for _ in range(int(stdin.readline())):
        result = 1.0
        N, M = map(int, stdin.readline().split())
        for i in range(N):
            result *= M - i
            result //= 1 + i
        print(int(result))

