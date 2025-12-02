import matplotlib.pyplot as plt
import os

menu = """1. Student grade
2. Assignment statistics
3. Assignment graph

Enter your selection: """

#make student dict {student_name : id_number)}
with open('data/students.txt', 'r') as file:
    content = file.read().splitlines()
    students = dict()
    for line in content:
        students[line[3:]] = line[:3]
#make assignment list [(assignment_name, assignment_id, point_value)]
with open('data/assignments.txt', 'r') as file:
    content = file.read().splitlines()
    assignments = []

    for index, line in enumerate(content):
        if line.isdigit():
            continue
        assignments.append((content[index], content[index + 1], content[index + 2]))
#makes list of assignment names
assignment_names = []
for assignment in assignments:
    assignment_names.append(assignment[0])
#makes list of all assignment grades
assignment_grades = []
for filename in os.listdir("data/submissions/"):
    file_path = "data/submissions/" + filename
    with open(file_path, 'r') as file:
        content = file.read()
        assignment_grades.append(content.split("|"))
def get_grades(student_id):
    student_assignments = []
    for assignment in assignment_grades:
        if assignment[0] == student_id:
            student_assignments.append(assignment[1:])

    student_assignments.sort(key=lambda x: int(x[0]))
    final_grades = []
    for index, assignment in enumerate(student_assignments):
        grade = assignment[1]
        points = assignments[index][2]
        final_grades.append([int(grade), int(points)])

    return final_grades

def calculate_average(grades):
    grade_sum = 0
    total_points = 0
    for grade, points in grades:
        grade_sum += grade * points
        total_points += points
    return grade_sum / total_points

def get_assignment_code(assignment_name):
    for assignment in assignments:
        if assignment[0] == assignment_name:
            return assignment[1]

def calculate_statistics_assignment(grades):
    return [min(grades), sum(grades) / len(grades), max(grades)]

def get_assignment_grades(assignment_code):
    grades = []
    for assignment in assignment_grades:
        if assignment[1] == assignment_code:
            grades.append(int(assignment[2]))
    return grades


selection = input(menu)

if selection == "1":
    student_name = input("What is the student's name: ")
    if student_name not in students:
        print("Student not found")
        exit()
    print(str(calculate_average(get_grades(students[student_name])))[:2]+"%")

elif selection == "2":
    assignment_name = input("What is the assignment name: ")
    if assignment_name not in assignment_names:
        print("Assignment not found")
        exit()
    statistics = calculate_statistics_assignment(get_assignment_grades(get_assignment_code(assignment_name)))
    print("Min:", str(statistics[0])[:2]+"%")
    print("Avg:", str(statistics[1])[:2]+"%")
    print("Max:", str(statistics[2])[:2]+"%")

elif selection == "3":
    assignment_name = input("What is the assignment name: ")
    if assignment_name not in assignment_names:
        print("Assignment not found")
        exit()
    scores = get_assignment_grades(get_assignment_code(assignment_name))
    min_score = ((min(scores)-10) // 5) * 5
    bins = range(min_score, 100, 5)
    print(bins)

    plt.hist(scores, bins)
    plt.show()


