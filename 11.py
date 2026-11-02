marks = [int(input("Enter marks for subject 1: ")),
         int(input("Enter marks for subject 2: ")),
         int(input("Enter marks for subject 3: "))]
pass_mark = 40
grace_limit = 5
grace_used = 0
for i in range(len(marks)):
    if marks[i] < pass_mark and pass_mark - marks[i] <= grace_limit:
        marks[i] = pass_mark
        grace_used += pass_mark - (marks[i] - (pass_mark - marks[i]))
total = sum(marks)
percentage = total / len(marks)
if min(marks) < pass_mark:
    result = "Fail"
elif percentage >= 75:
    result = "Distinction"
elif percentage >= 60:
    result = "First Class"
else:
    result = "Pass"
print("Final marks:", marks)
print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)
