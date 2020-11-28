
N = int(input())
ans = -1
for i in range(1, N+1):
    if N == int(i * 1.08):
        ans = i
if ans != -1:
    print(ans)
else:
    print(':(')