"""Given a dictionary of students and their marks, print the names of students who scored
more than 80."""


students = {
    "Saquib" : 78,
    "Shobnom": 85,
    "Shayan" : 79
    }

for i in students:
    if students[i] > 80:
        print(i)