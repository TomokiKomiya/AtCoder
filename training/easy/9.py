N = int(input())
K = int(input())
X = list(map(int, input().split()))

k = 0
for x in X:
    if int(K/2) >= x:
        k += x
    else:
        k += (K - x)

t = 2 * k
print(t)