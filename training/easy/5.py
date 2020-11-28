N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

count = 0
for a in A:
    ans = 0
    for i in range(M):
        ans += a[i] * B[i]
    ans += C
    if ans > 0:
        count += 1

print(count)