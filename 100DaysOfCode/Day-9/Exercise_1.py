#convert students scores to grades


student_scores = {

    "Harry":81,
    "Ron":78,
    "Hermoine":99,
    "Draco":74,
    "Neiville":62
}

student_grades = {}

for names in student_scores:
    if(student_scores[names]>91):
        student_grades[names] = "Outstanding"
    elif(student_scores[names]>80 and student_scores[names]<90 ):
        student_grades[names] = "Exceeds Expectation"
    elif (student_scores[names] > 70 and student_scores[names] < 80):
        student_grades[names] = "Acceptable"
    elif (student_scores[names] > 60 and student_scores[names] < 70):
        student_grades[names] = "improvement required"


print(student_grades)



