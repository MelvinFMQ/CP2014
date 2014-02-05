#q12_find_factors.py
num = int(input("Input number: "))
factors = []
divisor = 2
while divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num = num/divisor
    else:
        divisor += 1        
print(factors) 
    
    
 
        
    
