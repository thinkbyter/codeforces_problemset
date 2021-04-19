# https://codeforces.com/problemset/problem/1343/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-18
# Time: 00:08:58

t = int(input())

for _ in range(t):
  n = int(input())
  k = 2
  tk = 2 * 2
  while n % (tk - 1) != 0:
    k += 1
    tk *= 2
  print(n // (tk - 1))