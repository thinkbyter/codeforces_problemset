# https://codeforces.com/problemset/problem/271/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-08
# Time: 00:05:59

y = int(input())

def f(y):
  ys = list(str(y))
  return len(ys) == len(set(ys))
  
y += 1
while not f(y):
  y += 1
  
print(y)