def get_grade(average_score):
    if average_score >= 4.0:
        return "A"
    elif average_score >= 3.0:
        return "B"
    elif average_score >= 2.0:
        return "C"
    elif average_score >= 1.0:
        return "D"
    elif average_score >= 0.0:
        return "F"

grades_to_test = [4.5, 3.5, 2.5, 1.5, 0.5]

for grade in grades_to_test:
    print(f"Средний балл: {grade} → Грейд: {get_grade(grade)}")
