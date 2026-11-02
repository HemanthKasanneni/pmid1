violations = ["helmet", "signal", "overspeed"]
repeat = [False, True, False]
fine_table = {"helmet": 500, "signal": 1000, "overspeed": 2000}

total = 0
review = False

for i in range(len(violations)):
    fine = fine_table[violations[i]]
    if repeat[i]:
        fine = fine * 2
    total += fine
    print(violations[i], "fine:", fine)
    if violations[i] == "overspeed":
        review = True

print("Total fine:", total)
if review:
    print("Status: Requires review")

