from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    # Input
    N = int(input())
    F = [*input().rstrip()]
    num = {}
    for i in range(N):
        num[chr(ord("A") + i)] = int(input())

    # Solve
    stack = []

    # 나머지연산이 있었을 땐, else를 나머지연산으로 놓고 if문을 추가해서 if f in ['+', '-', '*', '/']:를 추가한다. Or 아스키코드를 통해서 알아본다.
    for f in F:
        if f.isalpha(): # 숫자일 때는 값을 더한다.
            stack.append(num[f])
        else:
            B = stack.pop()
            A = stack.pop()
            stack.append(eval(str(A) + f + str(B))) # A, B를 빼내서 사칙연산 후 append()한다.

    # Output
    print("%.2f" % stack[0])
