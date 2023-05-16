# First, we create an empty dictionary to store the students and their grades
student_records = {}

# We read the number of students from the input
n = int(input())

# We go through each student
for _ in range(n):
    # We read the student's name and grade from the input
    name, grade = input().split()
    grade = float(grade)

    # If the student is already in the dictionary, we append the grade to their list of grades
    if name in student_records:
        student_records[name].append(grade)
    # If the student is not in the dictionary, we add them with a list containing their grade
    else:
        student_records[name] = [grade]

# We go through each student and their grades in the dictionary
for name, grades in student_records.items():
    # We calculate the average grade
    avg_grade = sum(grades) / len(grades)

    # We print the student's name, their grades and their average grade, formatted as required
    grades_str = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")
