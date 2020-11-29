
H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
else:
    ans = int((H * W + 1) / 2)
print(ans)



# box = [[0 for j in range(W)]for i in range(H)]
# count = 0
# box[0][0] = 1
# r1 = 0
# c1 = 0
# for _ in range(H * W):
#     for h in range(H):
#         for w in range(W):
#             if box[h][w] == 1:
#                 r1 = h
#                 c1 = w
#                 for j in range(H):
#                     for i in range(W):
#                         if r1 + c1 == j + i:
#                             box[j][i] = 1
#                         elif r1 - c1 == j - i:
#                             box[j][i] = 1
# ans = 0
# for i in box:
#     ans += i.count(1)
# print(ans)