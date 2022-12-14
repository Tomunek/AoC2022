# --- Day 14: Regolith Reservoir ---
nodes = []


class Node:
    global nodes

    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y

    def move(self):
        if self.y >= 300:
            return -1
        if get_node_index(self.x, self.y + 1) == -1:
            self.y = self.y + 1
            return 0
        if get_node_index(self.x, self.y + 1) != -1 and get_node_index(self.x - 1, self.y + 1) == -1:
            self.y = self.y + 1
            self.x = self.x - 1
            return 0
        if get_node_index(self.x, self.y + 1) != -1 and get_node_index(self.x + 1, self.y + 1) == -1:
            self.y = self.y + 1
            self.x = self.x + 1
            return 0
        return 1


def get_node_index(x, y):
    global nodes
    for i in range(len(nodes)):
        if nodes[i].x == x and nodes[i].y == y:
            return i
    return -1


def draw():
    global nodes
    screen = ""
    for y in range(35, 55):
        for x in range(470, 520):
            if get_node_index(x, y) == -1:
                screen += "."
            else:
                screen += nodes[get_node_index(x, y)].t
        screen += "\n"

    print(screen)


def main():
    global nodes

    with open("input.txt") as f:
        for input_line in f.readlines():
            lines = input_line.split(" -> ")
            for line_num in range(len(lines) - 1):
                xb = int(lines[line_num].split(",")[0].strip())
                yb = int(lines[line_num].split(",")[1].strip())
                xe = int(lines[line_num + 1].split(",")[0].strip())
                ye = int(lines[line_num + 1].split(",")[1].strip())
                for x in range(min(xb, xe), max(xb, xe) + 1):
                    for y in range(min(yb, ye), max(yb, ye) + 1):
                        nodes.append(Node('#', x, y))

    full = False
    while not full:
        sand = Node('o', 500, 0)
        nodes.append(sand)
        # draw()
        stopped = False
        while not stopped:
            stopped = nodes[-1].move() != 0
            full = nodes[-1].move() == -1
            if full:
                stopped = True

    sand_count = -1
    for node in nodes:
        if node.t == "o":
            sand_count += 1

    print(f"Sand count: {sand_count}")


if __name__ == "__main__":
    main()
