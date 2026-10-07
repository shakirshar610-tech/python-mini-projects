marks = []

for subject in ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]:
    value = float(input(f"{subject} marks (0-100): "))
    if not 0 <= value <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    marks.append(value)

average = sum(marks) / len(marks)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
