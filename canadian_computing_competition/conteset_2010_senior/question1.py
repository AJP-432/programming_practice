# Problem S1: Computer Purchase
# Ajlal Fareed Paracha Feb 15, 2022

# Formula for performance: 2 ∗ R + 3 ∗ S + D.

computers = [input().split() for _ in range(int(input()))]

first, second, speed, new = 0, 0, [], []

for name, r, s, d in computers: 
    new.append(name)
    new.append(2*int(r) + 3*int(s) + int(d))
    speed.append(2*int(r) + 3*int(s) + int(d))

speed = sorted(speed)

print(speed)
print(new)
print(speed[-1], speed[-2])

print(f"{new[(new.index(speed[-1]))-1]}\n{new[(new.index(speed[-2]))-1]}")

