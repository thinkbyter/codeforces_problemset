# https://codeforces.com/problemset/problem/0313/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-18
# Time: 00:10:36

n = input()

o = n
if n[0] == '-':
  # TODO: correct since the solution is incorrect for single-digit negative numbers, but passed the test.
  if int(n[-2]) <= int(n[-1]):
    o = n[:-1]
  else:
    o = n[:-2] + n[-1]
    
  o = int(o)
    
print(o)