# https://codeforces.com/problemset/problem/266/B
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:06:44

n, t = map(int, input().split())
s = list(input())

for _ in range(t):
  bi = [i for i, x in enumerate(s[:-1]) if x == 'B' and s[i + 1] == 'G'] 
  for i in bi:
    s[i] = 'G'
    s[i + 1] = 'B'
    
print(''.join(s))