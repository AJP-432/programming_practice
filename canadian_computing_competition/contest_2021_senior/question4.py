# Daily Commute
#https://cemc.uwaterloo.ca/contests/computing/2021/ccc/seniorEF.pdf

# Ajlal Paracha Jan 13, 2022

n, w, d = list(map(int, input().split()))
adj = [[] for i in range(n + 1)]
for _ in range(w):
    a, b = list(map(int, input().split()))
    adj[b].append(a)

print(adj)
