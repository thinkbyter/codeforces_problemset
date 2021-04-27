# https://codeforces.com/problemset/problem/118/A
# Difficulty: 1000
# Attempts: 1
# Date: 2021-04-19
# Time: 00:07:29

vowels = ["A", "O", "Y", "E", "U", "I"]

s = list(input())

o = []
for x in s:
  if not x.upper() in vowels:
    o.append('.' + x.lower())
    
print(''.join(o))