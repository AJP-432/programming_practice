# Lunch Concert
#https://cemc.uwaterloo.ca/contests/computing/2021/ccc/seniorEF.pdf

# Ajlal Paracha Jan 7, 2022

data_list = []

for _ in range(int(input())): data_list.append(list(map(int, input().split())))

def time_compute(location):

    total_time = 0

    for p, w, d in data_list:

        # outside range to left
        if location < (p-d): total_time += w * (p-d-location)
        # outside range to right
        elif location > (p+d): total_time += w * (location-p-d)
        else: pass

    return total_time

# binary search
left, right = 0, 10**9

while left+1 < right: 
    mid = (left + right)//2
    y1 = time_compute(mid)
    y2 = time_compute(mid+1)

    if y1 < y2: right = mid
    else: left = mid+1

print(min(time_compute(left), time_compute(right)))



print(data_list)

# # Looping position 0 to position furthest away
# for location in range(furthest_away+1):
#     for a in range(len(data_list)):
    
#         # if outside range to left
#         if location < (data_list[a][0]-data_list[a][2]):
#             time_temp += data_list[a][1] * (data_list[a][0]-data_list[a][2]-location)
        
#         # to right
#         elif location > (data_list[a][0]+data_list[a][2]):
#             time_temp += data_list[a][1] * (location-data_list[a][0]-data_list[a][2])
        
#         else: pass

#     print(time_temp)
#     if time_temp < time: 
#         time = time_temp
#         time_temp = 0
#         spot = location

# print(f"The shortest time is {time} seconds at location {spot}!")








