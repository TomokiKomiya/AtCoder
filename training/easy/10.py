N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
x = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        x += a
    else:
        x -= a
print(x)