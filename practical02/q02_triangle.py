#q02_triangle.py
is_triangle = False
side1 = int(input("enter side :"))
side2 = int(input("enter side :"))
side3 = int(input("enter side :"))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    perimeter = side1 + side2 + side3
    print("Perimeter = " + str(perimeter))
else:
    print("Invalid triagnle!")
