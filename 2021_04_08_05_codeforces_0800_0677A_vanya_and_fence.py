# https://codeforces.com/problemset/problem/677/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-08
# Time: 00:04:13

n, h = map(int, input().split())
w = 0
for a in map(int, input().split()):
  w += 1 if a <= h else 2
  
print(w)  