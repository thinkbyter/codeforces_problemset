# https://codeforces.com/problemset/problem/231/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-04
# Time: 00:04:12

n = int(input())

res = 0
for _ in range(n):
  p, v, t = map(int, input().split())
  if p + v + t >= 2:
    res += 1
    
print(res)