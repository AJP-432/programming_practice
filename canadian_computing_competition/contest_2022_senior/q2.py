
together = [set(input().split()) for _ in range(int(input()))]
apart = [set(input().split()) for _ in range(int(input()))]
current = [set(input().split()) for _ in range(int(input()))]

violations = len(together)

for value in together: 
    for seating in current: 
        if value.issubset(seating): 
            violations-=1
            break

for value in apart: 
    for seating in current: 
        if value.issubset(seating): 
            violations+=1
            break

print(violations)

