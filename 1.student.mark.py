student_name = []
student_id = []
dob = []
course_name = []
course_id = []
marks = []

# Student input
def student_input():
    for i in range(num_student):
        print("\nStudent number",i+1,":")
        student_name.append(input("Enter student name: "))
        student_id.append(input("Enter student's id: "))
        dob.append(input("Enter student's dob: "))

# Student output
def student_output(num_student):
    for i in range(num_student):
        print("\nName of student", i+1,": ", student_name[i], "\nID of student", i+1,": ", student_id[i], "\nDOB of student", i+1,": ", dob[i])

# Course input
def course_input():
    for i in range(num_course):
        print("\nCourse number",i+1,":")
        course_name.append(input("Enter course name: "))
        course_id.append(input("Enter course id: "))

# Course output
def course_output(num_course):
    for i in range(num_course):
        print("\nName of course", i+1,":", course_name[i], "\nId of course", i+1,":",course_id[i])

# Marks input
def marks_input(course_name, student_name):
    for i in course_name:
        a = []
        print("\nMarks for course",i)
        for j in student_name:
            print("Student",j,":")
            a.append(input())
        marks.append(a)

# Marks output
def marks_output(num_course, num_student, marks):
    for i in range(num_course):
        print("\nMarks for course", course_name[i])
        for j in range(num_student):
            print("Student",student_name[j], ":",marks[i][j],"\n")


# Main function
# Student input
num_student = int(input("\nEnter the number of student: "))
student_input()
# Print students
student_output(num_student)

# Course input
num_course = int(input("\nEnter the number of course: "))
course_input()
# Print course
course_output(num_course)

# Input marks
marks_input(course_name, student_name)
# Print marks 
marks_output(num_course, num_student, marks)
