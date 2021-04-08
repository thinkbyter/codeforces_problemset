# https://codeforces.com/problemset/problem/734/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-08
# Time: 00:03:46

n = int(input())
s = input()
a = s.count('A')
if a > len(s) - a:
  print('Anton')
elif a < len(s) - a:
  print('Danik')
else:
  print('Friendship')