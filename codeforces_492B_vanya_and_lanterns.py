# Problem: https://codeforces.com/problemset/problem/492/B
# Difficulty: 1200
# Trials: 7
# Time: 00:29:30

n, l = map(int, input().split())
ax = list(map(int, input().split()))
ax.sort()

maxd = ax[0] * 2
for i, a in enumerate(ax):
  if i == n - 1:
    d = (l - ax[i]) * 2
  else:
    d = ax[i + 1] - a
    
  if d > maxd:
    maxd = d
    
print(maxd / 2) 