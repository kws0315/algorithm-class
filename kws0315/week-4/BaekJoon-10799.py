from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    # Input
    F = [*input().rstrip()]

    # Solve
    stack = []
    cnt = 0
    for i in range(len(F)):
        if F[i] == '(':
            stack.append(F[i])
        else:  # F[i] == ')'
            stack.pop()
            if F[i - 1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print(cnt)