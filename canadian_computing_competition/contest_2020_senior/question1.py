# Surmising a Sprinters Speed
#https://cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf

# Ajlal Paracha - Oct 10, 2021

number_of_data_points = int(input())
data_points = []
top_speed = 0

# Populating data points
for i in range(number_of_data_points): data_points.append(input())

for a in range(number_of_data_points): 
    time_a, pos_a = data_points[a].split()

    for b in range(number_of_data_points): 
        time_b, pos_b = data_points[b].split()
        if pos_a == pos_b or time_a == time_b:
            pass
        
        else: 
            speed = abs((int(pos_a) - int(pos_b))/(int(time_a) - int(time_b)))

            if speed >= top_speed: top_speed = speed

print(top_speed)


# 3
# 0 100
# 20 50
# 10 120
