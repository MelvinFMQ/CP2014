#q2_display_pattern.py
##def display_pattern(n):
##    num_pattern = ""
##    pattern = ""
##    spaces = n
##    for line in range(1,n+1):
##        num_pattern = str(line) + num_pattern 
##        pattern = " "*(len(str(spaces)))*(n-1) + num_pattern
##        n -= 1
##        print(pattern)
##display_pattern(10)

def display_pattern(n):
    num_pattern = ""
    for i in range(1 , n+1):
        num_pattern = str(i) + num_pattern 
        pattern = "{num:>{width}}".format(num = "" , width = (n-1)*(len(str(i)))) + num_pattern
        n -= 1
        print(pattern)
display_pattern(40)
    
