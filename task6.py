import re

subjects = {}
with open("study_data.txt") as file:
    for line in file.readlines():
        total_hours = 0
        subject, lectures, practice, labs = line[:-1].split(" ")
        subject = subject[:-1]
        for activity in [lectures, practice, labs]:
            if activity != "" and activity != '-':
                hours = int(re.match(r"\d+(?=\()", activity)[0])
                total_hours += hours
        subjects[subject] = total_hours

print(subjects)
