candidates = [
    ("Asha", 80, 75, 90),
    ("Ravi", 55, 62, 70),
    ("Mina", 35, 88, 91),
    ("Kiran", 70, 70, 70)
]

eligible = []
for name, math, physics, computer in candidates:
    average = (math + physics + computer) / 3
    if math >= 40 and physics >= 40 and computer >= 40 and average >= 60:
        eligible.append((name, average))

eligible.sort(key=lambda item: item[1], reverse=True)

print("Admission ranking")
for rank, candidate in enumerate(eligible, start=1):
    print(rank, candidate[0], round(candidate[1], 2))
