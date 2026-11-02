key = ["A", "C", "B", "D", "A"]
answers = ["a", "C", "D", "", "A"]

correct = 0
wrong = 0
blank = 0

for i in range(len(key)):
    answer = answers[i].upper()
    if answer == "":
        blank += 1
    elif answer == key[i]:
        correct += 1
    else:
        wrong += 1

score = correct * 2 - wrong * 0.5

print("Correct:", correct)
print("Wrong:", wrong)
print("Unanswered:", blank)
print("Final score:", score)
