# 2の乗数が一番2で割れる. 

N = int(input())

for i in range(8):
    if N < 2**i:
        ans = 2 ** (i-1)
        break

print(ans)