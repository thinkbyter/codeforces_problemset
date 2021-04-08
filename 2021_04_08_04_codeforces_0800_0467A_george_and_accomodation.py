# https://codeforces.com/problemset/problem/467/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-08
# Time: 00:03:13

n = int(input())

r = 0
for _ in range(n):
  p, q = map(int, input().split())
  r += q - p >= 2
  
print(r)