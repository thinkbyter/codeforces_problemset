# https://codeforces.com/problemset/problem/41/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-08
# Time: 00:07:11

s = input()
t = input()
msg = 'YES'
if len(s) != len(t):
  msg = 'NO'
  
if msg != 'NO':
  i = 0
  while i < len(s) and msg == 'YES':
    if s[i] != t[len(t) - 1 - i]:
      msg = 'NO'
    i += 1
      
print(msg)