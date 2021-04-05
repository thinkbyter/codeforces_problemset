# https://codeforces.com/problemset/problem/282/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-05
# Time: 00:04:39

n = int(input())

x = 0
for _ in range(n):
  s = input()
  if s[:2] == '++' or s[1:] == '++':
    x += 1
  else:
    x -= 1
    
print(x)