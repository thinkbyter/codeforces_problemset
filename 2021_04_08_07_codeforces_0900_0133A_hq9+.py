# https://codeforces.com/problemset/problem/133/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-08
# Time: 00:03:44

s = input()
msg = 'NO'
for x in s:
  if x in list('HQ9'):
    msg = 'YES'
    break
    
print(msg)