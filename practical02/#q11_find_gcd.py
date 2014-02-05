#q11_find_gcd.py
n1 = int(input("first number: "))
n2 = int(input("second number: "))
if n1 < n2:
    greatest_divisor = n1
    while n2 % greatest_divisor != 0 or n1 % greatest_divisor != 0:
        greatest_divisor -= 1    
if n2 < n1:
    greatest_divisor = n2
    while n2 % greatest_divisor != 0 or n1 % greatest_divisor != 0:
        greatest_divisor -= 1      
elif n1 == n2:
    greatest_divisor = n1 
print(greatest_divisor)
