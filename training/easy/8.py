a, b = map(int, input().split())

N = int(str(a) + str(b))

def is_square_num(n):
  i2 = 0
  for i in range(0, n + 1):
    if i2 == n:
      return True
    if i2 > n:
      return False
    i2 += i * 2 + 1

if is_square_num(N):
    print('Yes')
else:
    print('No')