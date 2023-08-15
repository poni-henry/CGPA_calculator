#Fixed values Course units and CUs for course unit.
#user inputs grades for semester course units
#connect grade provided with course unit and CU S
#for calculation of GPA per semester need CU, grade input by user 
#GP per course unit based on grade input by user
#GPA calculated from total GP/total CUs for semester
#store values from previous semesters
#CGPA adding totals of GPs and CUs for current and all semesters before 
#want both GPA and CGPA per semester.
#when someone retakes  a course unit
#when get a retake
#when redo course unit the next semester
#saying degree class
#grading different users per semester or per CGPA
#deans, vice councillors list, retake

def main():
    semester()


def semester():
    #incrementing course units by 1
    for i in range(1,3):
        #assign value of grade to course unit
        course_i = int(input("please input grade obtained: "))
        print(f"course_{i} = {course_i}")
        GP_calculation(course_i)

def GP_calculation(course_i):
    if course_i > 80:
        GP = 5 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 75:
        GP = 4.5 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 69:
        GP = 4.0 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 65:
        GP = 3.5 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 60:
        GP = 3.0 * 4 
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 55:
        GP = 2.5 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 50:
        GP = 2.0 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    elif course_i > 45:
        GP = 1.5 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True
    else:
        GP = 1 * 4
        print(f"Your GPA in {course_i} is {GP}")
        return True 

while True:
    total_GP = 45+45
    break

def calculate_GPA(total_GP):
    CTCU = 4 *2
    print(CTCU)
    GPA = total_GP /CTCU


main()
