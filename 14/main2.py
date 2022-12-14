# --- Day 14: Regolith Reservoir ---

nodes = []


def move(x, y):
    global nodes
    # print(f"{x} {y}")
    assert nodes[x][y] == "o"
    if nodes[x][y + 1] == ".":
        nodes[x][y + 1] = nodes[x][y]
        nodes[x][y] = "."
        return x, y + 1
    if nodes[x - 1][y + 1] == ".":
        nodes[x - 1][y + 1] = nodes[x][y]
        nodes[x][y] = "."
        return x - 1, y + 1
    if nodes[x + 1][y + 1] == ".":
        nodes[x + 1][y + 1] = nodes[x][y]
        nodes[x][y] = "."
        return x + 1, y + 1
    return x, y


def draw():
    global nodes
    screen = ""
    for j in range(0, 20):
        for i in range(490, 510):
            screen += nodes[i][j]
        screen += "\n"
    print(screen)


def main():
    global nodes
    nodes = [["." for i in range(1000)] for j in range(1000)]
    max_y = 0

    with open("input.txt") as f:
        for input_line in f.readlines():
            lines = input_line.split(" -> ")
            for line_num in range(len(lines) - 1):
                xb = int(lines[line_num].split(",")[0].strip())
                yb = int(lines[line_num].split(",")[1].strip())
                xe = int(lines[line_num + 1].split(",")[0].strip())
                ye = int(lines[line_num + 1].split(",")[1].strip())
                if max(yb, ye) > max_y:
                    max_y = max(yb, ye)
                for x in range(min(xb, xe), max(xb, xe) + 1):
                    for y in range(min(yb, ye), max(yb, ye) + 1):
                        nodes[x][y] = "#"

    for i in range(1000):
        nodes[i][max_y + 2] = "#"

    full = False
    while not full:
        sand_x = 500
        sand_y = 0
        nodes[sand_x][sand_y] = "o"
        # draw()
        stopped = False
        while not stopped:
            new_s_x, new_s_y = move(sand_x, sand_y)
            if new_s_x == sand_x and new_s_y == sand_y:
                stopped = True
            else:
                sand_x = new_s_x
                sand_y = new_s_y
        if sand_x == 500 and sand_y == 0:
            full = True

    sand_count = 0
    for row in nodes:
        for item in row:
            if item == "o":
                sand_count += 1

    print(f"Sand count: {sand_count}")


if __name__ == "__main__":
    main()
