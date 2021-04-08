# https://codeforces.com/problemset/problem/791/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:04:32

a, b = map(int, input().split())

y = 0
while a <= b:
  a *= 3
  b *= 2
  
  y += 1
  
print(y)