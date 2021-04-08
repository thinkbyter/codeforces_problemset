# https://codeforces.com/problemset/problem/116/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:06:00

n = int(input())
c = 0
p = 0
for _ in range(n):
  a, b = map(int, input().split())
  p = p - a + b
  if p > c:
    c = p
print(c)