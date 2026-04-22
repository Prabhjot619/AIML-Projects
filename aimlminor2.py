# Student Grade Management System

def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    
    marks = []
    for j in range(3):
        m = float(input(f"Enter marks of subject {j+1}: "))
        marks.append(m)
    
    avg = sum(marks) / 3
    grade = calculate_grade(avg)

    students.append({
        "name": name,
        "marks": marks,
        "average": avg,
        "grade": grade
    })

# Display Data
print("\n--- Student Report ---")
topper = students[0]

for s in students:
    print(f"\nName: {s['name']}")
    print(f"Marks: {s['marks']}")
    print(f"Average: {s['average']:.2f}")
    print(f"Grade: {s['grade']}")

    if s["average"] > topper["average"]:
        topper = s

print(f"\n Topper: {topper['name']} with {topper['average']:.2f}")