# https://codeforces.com/problemset/problem/415/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-18
# Time: 00:32:06

n, m = map(int, input().split())

o = 'Akshat'
if min(n, m) % 2 == 0:
  o = 'Malvika'
 
print(o)