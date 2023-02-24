student_name = []
student_id = []
dob = []
course_name = []
course_id = []

# Student input
def student_inputs():
    for i in range(num_student):
        a = input("Enter student name: ")
        student_name.append(a)
        b = input("Enter student's id: ")
        student_id.append(b)
        DOB = input("Enter student's dob: ")
        dob.append(DOB)

def student_listing(num_student):
    for i in range(num_student):
        print("Name of student", i+1,": ", student_name[i], "\nID of student", i+1,": ", student_id[i], "\nDOB of student", i+1,": ", dob[i],"\n")

# Course input
def course_inputs():
    for i in range(num_course):
        a = input("Enter course name: ")
        course_name.append(a)
        b = input("Enter course id: ")
        course_id.append(b)

def course_listing(num_course):
    for i in range(num_course):
        print("Name of course", i+1,": ", course_name[i], "\nId of course", i+1,": ",course_id[i],"\n")


# Test
# Test the student input functions
num_student = int(input("Enter the number of student: "))
student_inputs()

# Test the course input functions
num_course = int(input("Enter the number of course: "))
course_inputs()

# Print list
print("\n")
student_listing(num_student)
course_listing(num_course)

# Select course then input marks for student
