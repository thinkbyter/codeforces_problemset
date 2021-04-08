# https://codeforces.com/problemset/problem/617/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:02:33

x = int(input())

n = x // 5
if x % 5 != 0:
  n += 1

print(n)
