# https://codeforces.com/problemset/problem/112/A
# Difficulty: 800
# Attempts: 1 
# Date: 2021-04-05
# Time: 00:04:14

s1 = input().lower()
s2 = input().lower()

if s1 < s2:
  print(-1)
elif s2 < s1:
  print(1)
else:
  print(0)