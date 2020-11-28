
N, A, B = map(int, input().split())
S = list(input())

count = 0
b_count = 0
ans = []
for j in S:
    if A + B > count and j == 'a':
        count += 1
        ans.append('Yes')
    elif A + B > count and B > b_count and j == 'b':
        count += 1
        b_count += 1
        ans.append('Yes')
    else:
        ans.append('No')

for a in ans:
    print(a)

# for j in S:
#     if j == 'c':
#         ans.append('No')
#         continue
#     # 国内
#     if All_max > count:
#         if j == 'a':
#             count += 1
#             ans.append('Yes')
#     else:
#         if j == 'a':
#             ans.append('No')
#     # 国外
#     if All_max > count and B > b_count:
#         if j == 'b':
#             count += 1
#             b_count += 1
#             ans.append('Yes')
#     else:
#         if j == 'b':
#             ans.append('No')
