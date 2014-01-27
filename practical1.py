#q1_fahrenheit_to_celsius.py
def q1_fahrenheit_to_celsius():
    fahrenheit = input(" enter your fahrenheit to be converted :")
    celsius = (5/9)*( float(fahrenheit)- 32)
    print(celsius)
q1_fahrenheit_to_celsius()


#q2_calc_cylinder_volume.py
def q2_calc_cylinder_volume():
    import math 
    radius = input("input the radius :")
    length = input("input the length :")
    area = float(radius) ** 2 * math.pi
    volume = area * float(length)
    print ( "area :" + str(area) , "volume :" + str(volume)) 
q2_calc_cylinder_volume() 


#q3_miles_to_kilometre.py
def q3_miles_to_kilometre():
    miles = input("input miles to be converted :")
    kilometers = float(miles) * 1.60934
    print( "%.2f" % (kilometers))
q3_miles_to_kilometre()


#q4_sum_digits.py
def q4_sum_digits():      
    while True:
        i = int(input( "please enter a number between 0-1000 :"))
        if i >= 0 and i <= 1000:
            break
    digit_0 = i%10
    digit_1 = (i%100)//10
    digit_2 = (i%1000)//100
    digit_3 = i // 1000

    sum_digit = digit_0 + digit_1 + digit_2 + digit_3
    print(sum_digit)
q4_sum_digits()

#q5_upper_to_lower.py
def q5_upper_to_lower():
    upper = input("input a phrase :")
    print(chr(ord(upper)+32))
q5_upper_to_lower()

#q6_find_ascii_char.py
def q6_find_ascii_char():
    index = int(input("enter a ASCII code :"))
    print(chr(index))
q6_find_ascii_char()

#q7_generate_payroll.py
def q7_generate_payroll:
    name = input("Enter  Name : ")
    work_hr = input("Enter number of hours worked weekly: ")
    pay_rate = input("Enter hourly pay rate: ")
    cpf = input("Enter CPF contribution rate(%): ")
    gross_pay = float(work_hr) * float(pay_rate)
    cpf_cont = gross_pay * float(cpf)/100
    net_pay = gross_pay - cpf_cont
    print("Payroll statement for %s" % (name))
    print("Number of hours worked in week: %s" % (work_hr))
    print("Hourly pay rate: $%s" % (pay_rate))
    print("Gross pay = $%s" % (gross_pay))
    print("CPF contribution at %s = $%s" % (cpf , cpf_cont))  
    print("Net pay = $%s" % ( net_pay))
q7_generate_payroll()
    
   
        
            
