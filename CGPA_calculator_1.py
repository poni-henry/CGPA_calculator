
#Fixed values Course units and CUs for course unit.

#Including all course units in all 4 years of course and only showing course units for the current semester.

#Separating course units for each semester.
import course

for course_unit in course:
    Grade= int(input("Please input your grade: "))
    print(course_unit["course_unit"], Grade)
    
def weight_calculation():
    if Grade >=80:
        GP = 5 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 75:
        GP = 4.5 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 69:
        GP = 4.0 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 65:
        GP = 3.5 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 60:
        GP = 3.0 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 55:
        GP = 2.5 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 50:
        GP = 2.0 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    elif Grade > 45:
        GP = 1.5 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
    else:
        GP = 1 * course_unit["CU"]
        #print(f"Your GPA in {Grade} is {GP}")
        return GP
for course_unit in course:
    weight = course_unit["CU"] * weight_calculation()
    print(weight)
    GPA = weight / 18
    print(f"Your GPA is {GPA}")
for course_unit in course:
    print(course_unit["course_unit"],course_unit["CU"], Grade,GPA)