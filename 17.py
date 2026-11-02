subjects = ["Python", "Maths", "English"]
exam1 = [65, 72, 58]
exam2 = [78, 68, 64]

for i in range(len(subjects)):
    change = exam2[i] - exam1[i]
    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "No change"
    print(subjects[i], "change:", change, "-", trend)

weak_index = exam2.index(min(exam2))
print("Weakest subject:", subjects[weak_index])
