# https://codeforces.com/problemset/problem/158/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-04
# Time: 00:12:08

n, k = map(int, input().split())
ax = list(map(int, input().split()))
p = ax[k - 1]
i = k - 1
if p > 0:
  while i < n and ax[i] == p:
    i += 1
  print(i)
else:
  while i >= 0 and ax[i] == 0:
    i -= 1
  print(i + 1)