A, B, C = map(int, input().split())

if A == B == C:
    if A % 2 == 0:
        print('-1')
        exit()
    else:
        print("0")
        exit()

ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    ans += 1
    _A = int(B / 2) + int(C / 2)
    _B = int(C / 2) + int(A / 2)
    _C = int(A / 2) + int(B / 2)
    A = _A
    B = _B
    C = _C

print(ans)