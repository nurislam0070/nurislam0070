# n = int(input())
# x = list(map(int, input().split()))
# d = x[0]
# e =0
# for i in range(n):
#     if x[i] > d :
#         d = x[i]
#         e = i
# print(e+1)




n = int(input())
x = list(map(int, input().split()))
d = x[0]
e =0
for i in range(n):
    if x[i] > d :
        d = x[i]
        e = i
print(e+1)
