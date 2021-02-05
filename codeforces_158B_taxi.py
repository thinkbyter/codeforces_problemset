# Problem: https://codeforces.com/problemset/problem/158/B
# Difficulty: 1100
# Trials: 6
# Time: 00:45:14

n = int(input())

r = 0
d = {i: 0 for i in range(1, 4)}
for s in map(int, input().split()):
  if s == 4:
    r += 1
  else:
    d[s] += 1


r += d[2] // 2
d[2] %= 2

if d[2] == 1:
  r += 1
  if d[1] >= 2:
    d[1] -= 2
  if d[1] == 1 and d[3] == 0:
    d[1] -= 1

r += d[3]
d[1] -= min(d[1], d[3])

r += d[1] // 4
d[1] %= 4
if d[1] > 0:
  r += 1

print(r)