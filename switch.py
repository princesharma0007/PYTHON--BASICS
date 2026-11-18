marks=int(input("Enter marks (0-100): "))
name=input("Enter student name: ")
if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    grade = marks // 10

    match grade:
        case 10 :
            print("Grade: A+")
        case 8:
            print("Grade: A")
        case 7:
            print("Grade: B")
        case 6:
            print("Grade: C")
        case 5:
            print("Grade: D")
        case _:
            print("Grade: F")

    print("Student Name:", name)
    print("Marks:", marks)