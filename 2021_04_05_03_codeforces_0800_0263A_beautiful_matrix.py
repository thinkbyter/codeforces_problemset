# https://codeforces.com/problemset/problem/263/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-05
# Time: 00:11:06

i, j = 0, 0
for r in range(1, 6):
  if i == 0:
    cs = input().split()
    if '1' in cs:
      i = r
      j = cs.index('1') + 1
  else:
    _ = input()

print(abs(i - 3) + abs(j - 3))