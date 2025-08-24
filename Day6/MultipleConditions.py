eng_marks = int(input("Enter marks in english: "))
math_marks = int(input("Enter marks in math: "))

if eng_marks > 80 and math_marks > 80:
    print("A Grade")
elif eng_marks > 80 or math_marks > 80:
    print("B Grade")
else:
    print("C Grade")