teams = [
    ("CodeStars", 4, [80, 90]),
    ("ByteBuilders", 3, [85, 85]),
    ("LogicCrew", 2, [95, 90]),
    ("Debuggers", 5, [70, 88])
]

valid = []
for name, members, scores in teams:
    if 3 <= members <= 5:
        total = sum(scores)
        valid.append((name, total))
    else:
        print(name, "invalid team size:", members)

valid.sort(key=lambda team: team[1], reverse=True)

print("Valid team ranking")
for rank, (name, total) in enumerate(valid, start=1):
    print(rank, name, "Total:", total)

