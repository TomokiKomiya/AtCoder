import sys
import numpy as np

A = []
for _ in range(3):
    A.extend(map(int, input().split()))
N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))

for i, a in enumerate(A):
    if a in B:
        A[i] = True
    else:
        A[i] = False

A = np.array(A)
A = A.reshape(3, 3)
A_ = np.fliplr(A)

if np.diag(A).sum() == 3:
    print('Yes')
    sys.exit()
elif np.diag(A_).sum() == 3:
    print('Yes')
    sys.exit()
elif 3 in A.sum(axis = 1):
    print('Yes')
    sys.exit()
elif 3 in A.sum(axis = 0):
    print('Yes')
    sys.exit()
else:
    print('No')
    sys.exit()