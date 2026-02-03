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

if n <= 1:
    print("No")
else:
    s = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s = False
            break
    print("Yes" if s else "No")

