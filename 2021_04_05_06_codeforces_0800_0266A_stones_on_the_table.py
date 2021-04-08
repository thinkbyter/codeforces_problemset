# https://codeforces.com/problemset/problem/266/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-05
# Time: 00:05:45

n = int(input())
xs = input()
res = 0

for i, x in enumerate(xs):
  if i < len(xs) - 1:
    if x == xs[i + 1]:
      res += 1

print(res)