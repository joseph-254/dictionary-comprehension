import random
students_names = ["Ann", "Mark", "Ben", "Andy", "Joe", "Brian"]

stud_scores = {student:random.randint(1,100) for student in students_names}
print(stud_scores)


        ## 1st Method
# passed_students = { stud_name : stud_scores[stud_name] for stud_name in stud_scores if stud_scores[stud_name] > 60}
# print(passed_students)


        ##2nd method

  ## New_dict = {New_ key: New_value for (key, value) in dict.items() if test}

passed_students = {student: score for (student, score) in stud_scores.items() if score > 60}
print(passed_students)
