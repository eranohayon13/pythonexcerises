name = str(input("Enter name :"))
homework = int(input("Enter homework grade out of 25:"))
assessment = int(input("Enter assesment grade out of 50:"))
final_exam = int(input("Enter final exam grade out of 100: "))

ict_grade = homework + assessment + final_exam
average = ict_grade/3

def grades(average):
    if average >= 50:
        return "A"
    elif average >= 40:
        return "B"
    elif average >= 30:
        return "C"
    elif average < 20:
        return "Fail"

print(name, "got the final grade of: ",grades(average))
#you have to call in the function in the print statement to interact within it.