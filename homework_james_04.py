# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 3 Assignment: Python Lists



### 1. Python List Transformation ###
print("\n1. Python List Transformation \n")

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1.1 - sorting in descending order
grades.sort(reverse=True)
print("Sorted List: " + str(grades))

# Task 1.2 - calculate average
average = sum(grades) / len(grades)
print("Average Grade: " + str(average))

# Task 1.3 - fail any grade below 80 (pretty harsh!)
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

print("Updated Grades: " + str(grades))



### 2. Advanced List Methods and Identity Operators ###
print("\n2. Advanced List Methods and Identity Operators \n")

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 2.1 - determine which students both submitted assignments and attended class
overachievers = []
for student in submitted:
    if student in attended:
        overachievers.append(student)
print(f"The follow students both submitted their assignments and attended class: {overachievers}")

# Task 2.2 - check if the two lists are identical
submitted.sort()
attended.sort()
print("The lists are identical!") if submitted == attended else print("The two lists are NOT identical.")

# Task 2.3 - remove students from attended who did not submit assignments (also harsh!)
attended_copy = attended.copy()
for i in range(len(attended_copy)):
    if attended_copy[i] not in submitted:
        attended.remove(attended_copy[i])
print(f"Now the only students who get credit for attendance are: {attended}")



### 3. Advanced Slicing Techniques ###
print("\n3. Advanced Slicing Techniques \n")

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 
                91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 3.1 - get temperatures for second week
second_week_temps = temperatures[7:14]
print(f"Temperatures for Second Week: {second_week_temps}")

# Task 3.2 - get temperatures above 100
temps_above_one_hundred = temperatures[24:]
print(f"Temperatures above 100: {temps_above_one_hundred}")

# Coder's Note: I used list slicing since that's the objective of the assignment;
# in my heart, I would really like to be more precise and check the value
# of every item on the list, like so:
#
# temps_above_one_hundred = []
# for temp in temperatures:
#     if temp > 100:
#         temps_above_one_hundred.append(temp)
# print(temps_above_one_hundred)

# Task 3.3 - reverse list, extract temps from 5th and 10th days
reversed_temperatures = temperatures[::-1]
print(f"Reversed Temperatures List: {reversed_temperatures}")
print(f"5th Day Temperature: {reversed_temperatures[4]}")
print(f"10th Day Temperature: {reversed_temperatures[9]}")



### 4. Deep Dive into Python Lists ###
print("\n4. Deep Dive into Python Lists \n")

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 4.1 - filter out students who have grades below 80 (sorry Jane!)

# PREVIOUS SOLUTION: 
# check for grades below 80 
# grades_below_eighty = []
# for grade in grades:
#     if grade < 80:
#         grades_below_eighty.append(grade)

# # remove items in lists at index of grades below 80
# for i in grades_below_eighty:
#     index = grades.index(i)
#     removed_student = students.pop(index)
#     removed_grade = grades.pop(index)
#     removed_activity = activities.pop(index)
#     print(f"Removing Student: \"{removed_student}\", {removed_grade}, \"{removed_activity}\"")

for i in range(len(students)):
    if grades[i] < 80:
        print(f"\"{students[i]}\", {grades[i]}, \"{activities[i]}\"")

# Task 4.2 - add remaining students to new list

# PREVIOUS SOLUTION: students_approved = students.copy()
students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        students_approved.append(students[i])

# Task 4.3 - print new list
print(f"students_approved = {students_approved}")