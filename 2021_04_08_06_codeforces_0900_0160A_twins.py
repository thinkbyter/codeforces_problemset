# https://codeforces.com/problemset/problem/160/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-08
# Time: 00:08:36

n = int(input())
ax = list(map(int, input().split()))
t = sum(ax)
ax.sort(reverse=True) 
i = 0
s = 0
while s <= t - s: 
  s += ax[i]
  i += 1
  
print(i)