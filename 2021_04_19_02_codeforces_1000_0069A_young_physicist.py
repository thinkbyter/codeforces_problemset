# https://codeforces.com/problemset/problem/69/A
# Difficulty: 1000
# Attempts: 1
# Date: 2021-04-19
# Time: 00:11:59

n = int(input())
tx, ty, tz = 0, 0, 0
for _ in range(n):
  x, y, z = map(int, input().split())
  tx += x
  ty += y
  tz += z
  
o = 'YES'
if tx != 0 or ty != 0 or tz != 0:
  o = 'NO'
  
print(o)