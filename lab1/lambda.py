# n = int(input())
# s = list(map(int, input().split()))
# ss=0
# for i in range(n):
#     if s[i] % 2==0:
#         ss += 1
# print(ss)

# n = int(input())
# words = input().split()

# for i, w in enumerate(words):
#     print(f"{i}:{w}", end=" ")

# s = input()
# aa = set("aeuioAEUIO")
# if any(n in aa for n in s):
#     print("Yes")
# else:
#     print("No")

# n = int(input())
# s = list(map(int, input().split()))
# print("Yes" if all(x >=0 for x in s) else "No")

# n = int(input())
# s = input().split()
# print(max(s, key=len))

# n = int(input())
# nums = map(int, input().split())

# distinct_sorted = sorted(set(nums))
# print(*distinct_sorted)

# n = int(input())
# keys = input().split()
# values = input().split()
# query = input()

# d = dict(zip(keys, values))
# print(d.get(query, "Not found"))

n = int(input())
nums = map(int, input().split())

print(sum(map(bool, nums)))