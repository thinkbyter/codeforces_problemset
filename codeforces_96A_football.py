# Problem: https://codeforces.com/problemset/problem/96/A
# Difficulty: 900
# Trials: 3
# Time: 00:09:53

ss = input()
prev = ss[0]
count = 1
msg = "NO"
for s in ss[1:]:
  if s == prev:
    count += 1
  else:
    count = 1
    prev = s
    
  if count >= 7:
    msg = "YES"
    break
    
print(msg)