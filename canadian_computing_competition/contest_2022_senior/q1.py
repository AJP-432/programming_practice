
def combos(num): 
    num_of_ways = 0 
    if num%4==0: num_of_ways+=1
    if num%5==0: num_of_ways+=1

    while num>5: 
        num-=5
        if num%4==0: 
            num_of_ways+=1
    
    print(num_of_ways)

combos(int(input()))