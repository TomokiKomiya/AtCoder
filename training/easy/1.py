import math

A, B = map(int, input().split())

c = math.ceil((B - A) / (A - 1)) + 1

print(c)