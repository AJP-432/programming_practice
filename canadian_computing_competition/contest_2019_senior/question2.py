#https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf
# Pretty Average Primes 

# Ajlal Paracha - Feb 3, 2022

def prime_check(num):
    if num==2: return True
    if num%2==0: return False
    
    for n in range(3, int(num**0.5), 2):
        if num%n==0: return False
    
    return True

def mean_finder(num_to_mean):
    if num_to_mean%2==0: index = 1
    else: index = 2

    while True: 
        if prime_check(num_to_mean-index) and prime_check(num_to_mean+index): break
        else: index += 2

    print(f"{num_to_mean-index}  {num_to_mean+index}")

values = [int(input()) for _ in range(int(input()))]

for value in values: mean_finder(value)