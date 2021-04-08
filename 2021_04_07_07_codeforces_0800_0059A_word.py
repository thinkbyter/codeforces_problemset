# https://codeforces.com/problemset/problem/59/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:03:42

s = input()

l = sum([x.islower() for x in s])

if len(s) - l > l:
  print(s.upper())
else:
  print(s.lower())