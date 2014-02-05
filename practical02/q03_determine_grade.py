#q03_determine_grade.py
score = int(input("Enter score: "))
if score > 0 and score < 100:
    if score >= 70:
        print("A")
    if score <= 35 :
        print("U")
    if score >= 60 and score < 70:
        print("B")
    if score >=55 and score < 60:
        print("C")
    if score >= 50 and score < 55:
        print("D")
    if score >= 35 and score < 45:
        print("S)")
else:
    print("Invalid! Score must be within 0 - 100.")

    
    
