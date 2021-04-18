# https://codeforces.com/problemset/problem/318/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-09
# Time: 00:07:31

n, k = map(int, input().split())

h = n // 2 + n % 2
if k <= h:
  print(k * 2 - 1)
else:
  print((k - h) * 2)
