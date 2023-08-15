
#Fixed values Course units and CUs for course unit.
course =[
    {"course_unit": "CMP1101", "CU":3},
    {"course_unit": "CMP1102", "CU":4},
    {"course_unit": "CMP1103", "CU":4},
    {"course_unit": "CMP1104", "CU":4},
    {"course_unit": "CMP1105", "CU":3}
    ]
for course_unit in course:
    print(course_unit["course_unit"])

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