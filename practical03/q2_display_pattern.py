#eg: number = 1000 ; width = (1000-999)*4 + (999-99)*3 + (99-9)*2 + 9
#                   last_width = 1        +  900* 3     + 90*2    + 9*1 
def display_pattern(n):
    num_pattern = ""  
    if n > 9:
    #if number is more than 9 , width would need to be calculated because some numbers are 2 digit, 3 digit...ect         
        foo = 9
        other_width = 0
        for i in range(1, len(str(n))):
            #iterate through the tens, hundreds , thousands and so on. 10s have 2 digits , 100s have 3 digits.
            #Number of elements between first 4 digit number and first 3 digit number is 9*100*(3-1) 
            other_width = other_width + (9*10**(i-1))*i
            if i > 1:
                #need to caculate the last_width one iteration later because want to form 1 less from the decimal point of the number.
                #eg: 3000;999 , 100;99
                foo = (foo*10) +9
        last_width = (n-(foo))*len(str(n))                       
        calculated_width = int(other_width + last_width)
    else:
    #if number is within 9 , width = number
        calculated_width = n    
    for i in range(1 , n+1):
        #make number n inclusive 
        num_pattern = str(i) + num_pattern 
        pattern = "{num:>{width}}".format(num = num_pattern , width = calculated_width)
        #width stays constant
        print(pattern)        
user_input = int(input("0 to quit , or enther number: "))
while user_input != 0:
    user_input = int(input("0 to quit , or enther number: "))
    display_pattern(user_input)
    
