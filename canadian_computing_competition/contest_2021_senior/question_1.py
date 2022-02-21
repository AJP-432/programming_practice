#Crazy Fencing
#https://cemc.uwaterloo.ca/contests/computing/2021/ccc/seniorEF.pdf

# Ajlal Paracha Jan 7, 2022
# Practicing to sauce up the contest

# Taking input values
number_of_pieces = int(input())
heights = input().split()
widths = input().split()

area = 0

for i in range(len(widths)):
    area += (int(heights[i]) + int(heights[i+1]))/2.0 * int(widths[i])

print(area)
