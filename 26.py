rows = 3
columns = 4
reserved = [(1, 2), (2, 3)]

for r in range(1, rows + 1):
    line = []
    for c in range(1, columns + 1):
        if (r, c) in reserved:
            seat = "R"
        elif c % 2 == 0:
            seat = "X"
        else:
            seat = "S"
        line.append(seat)
    print("Row", r, ":", " ".join(line))

