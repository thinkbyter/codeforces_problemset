# https://codeforces.com/problemset/problem/208/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-17
# Time: 00:12:14

ws = input().split('WUB')

first = True
for w in ws:
  if w:
    prefix = '' if first else ' '
    print(prefix + w, end='')
      
    first = False
    
print()