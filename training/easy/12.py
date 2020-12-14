
K, N = map(int, input().split())
A = list(map(int, input().split()))

ans = 10 ** 6
for i in range(N - 1):
    A.append(A[i] + K)

for i in range(N):
    ans = min(ans, A[N + i - 1] - A[i])

print(ans)
