teams = [
    ("Falcons", 7, 8),
    ("Tigers", 7, 12),
    ("Wolves", 5, 4),
    ("Eagles", 9, 6)
]

teams.sort(key=lambda team: (team[1], team[2]), reverse=True)

print("Tournament ranking")
for rank, (name, points, difference) in enumerate(teams, start=1):
    print(rank, name, "Points:", points, "Difference:", difference)

