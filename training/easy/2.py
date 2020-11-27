import math

N = int(input())
X = list(map(int, input().split()))

def mean(xs):
  return sum(xs) / len(xs)

Xmin = min(X)
Xmax = max(X)
ans = 1000000


for i in range(Xmin, Xmax+1):
    num = 0
    for j in range(N):
        num += (X[j] - i) ** 2
    ans = min(ans, num)

print(ans)