
#Fixed values Course units and CUs for course unit.

#Including all course units in all 4 years of course and only showing course units for the current semester.
course =[
    {"course_unit": "CMP1101", "CU":3},
    {"course_unit": "CMP1102", "CU":4},
    {"course_unit": "CMP1103", "CU":4},
    {"course_unit": "CMP1104", "CU":4},
    {"course_unit": "CMP1105", "CU":3},
    {"course_unit": "CMP1106", "CU":3},
    {"course_unit": "CMP1201", "CU":3},
    {"course_unit": "CMP1202", "CU":4},
    {"course_unit": "CMP1203", "CU":4},
    {"course_unit": "CMP1204", "CU":4},
    {"course_unit": "CMP1205", "CU":3},
    {"course_unit": "CMP2101", "CU":3},
    {"course_unit": "CMP2102", "CU":4},
    {"course_unit": "CMP2103", "CU":4},
    {"course_unit": "CMP2104", "CU":4},
    {"course_unit": "CMP2105", "CU":3},
    {"course_unit": "CMP2201", "CU":3},
    {"course_unit": "CMP2202", "CU":4},
    {"course_unit": "CMP2203", "CU":4},
    {"course_unit": "CMP2204", "CU":4},
    {"course_unit": "CMP2205", "CU":3},
    {"course_unit": "CMP3101", "CU":3},
    {"course_unit": "CMP3102", "CU":4},
    {"course_unit": "CMP3103", "CU":4},
    {"course_unit": "CMP3104", "CU":4},
    {"course_unit": "CMP3105", "CU":3},
    {"course_unit": "CMP3201", "CU":3},
    {"course_unit": "CMP3202", "CU":4},
    {"course_unit": "CMP3203", "CU":4},
    {"course_unit": "CMP3204", "CU":4},
    {"course_unit": "CMP3205", "CU":3},
    {"course_unit": "CMP4101", "CU":3},
    {"course_unit": "CMP4102", "CU":4},
    {"course_unit": "CMP4103", "CU":4},
    {"course_unit": "CMP4104", "CU":4},
    {"course_unit": "CMP4105", "CU":3},
    {"course_unit": "CMP4201", "CU":3},
    {"course_unit": "CMP4202", "CU":4},
    {"course_unit": "CMP4203", "CU":4},
    {"course_unit": "CMP4204", "CU":4},
    {"course_unit": "CMP4205", "CU":3},
    {"course_unit": "CMP2301", "CU":2},
    {"course_unit": "CMP3301", "CU":2},
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
    GPA = weight / 18
    print(f"Your GPA is {GPA}")
