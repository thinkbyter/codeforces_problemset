# https://codeforces.com/problemset/problem/580/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-09
# Time: 00:05:30

n = int(input())

m = 1
c = 1
pa = None
for a in map(int, input().split()):
  if pa is not None:
    if a >= pa:
      c += 1
      if c > m:
        m = c
    else:
      c = 1
    
  pa = a
  
print(m)