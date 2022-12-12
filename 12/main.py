# --- Day 12: Hill Climbing Algorithm ---
import sys

nodes = []
max_x = 0
max_y = 0


class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node:
    global nodes
    global max_x
    global max_y

    def __init__(self, _x, _y, height):
        self.x = _x
        self.y = _y
        self.height = height
        self.distance = 1000000
        self.daddy = -1

    def set_daddy(self, daddy):
        self.daddy = daddy

    def set_distance(self, dist):
        self.distance = dist

    def dijkstra(self, dst, parent):
        # print(f"{self.x} : {self.y}")
        self.distance = dst
        self.daddy = parent
        # up
        # print(f"up {self.x} : {self.y}")
        if self.x > 0:
            up = get_node(self.x - 1, self.y)
            if up != self.daddy:
                if up.height <= self.height + 1:
                    if up.distance > self.distance + 1:
                        up.dijkstra(self.distance + 1, self)

        # down
        # print(f"down {self.x} : {self.y}")
        if self.x < max_x - 1:
            down = get_node(self.x + 1, self.y)
            if down != self.daddy:
                if down.height <= self.height + 1:
                    if down.distance > self.distance + 1:
                        down.dijkstra(self.distance + 1, self)

        # left
        # print(f"left {self.x} : {self.y}")
        if self.y > 0:
            left = get_node(self.x, self.y - 1)
            if left != self.daddy:
                if left.height <= self.height + 1:
                    if left.distance > self.distance + 1:
                        left.dijkstra(self.distance + 1, self)

        # right
        # print(f"right {self.x} : {self.y}")
        if self.y < max_y - 1:
            right = get_node(self.x, self.y + 1)
            if right != self.daddy:
                if right.height <= self.height + 1:
                    if right.distance > self.distance + 1:
                        right.dijkstra(self.distance + 1, self)


def get_node(x: int, y: int) -> Node:
    global nodes
    for node in nodes:
        if node.x == x and node.y == y:
            return node


def print_map():
    global nodes
    node_map = [[0 for i in range(max_x)] for j in range(max_y)]
    dist_map = [[0 for i in range(max_x)] for j in range(max_y)]
    for node in nodes:
        node_map[node.x][node.y] = node.height
        dist_map[node.x][node.y] = node.distance

    strm = ""
    for i in range(len(node_map)):
        for j in range(len(node_map[0])):
            if dist_map[i][j] > 1000:
                strm += TerminalColors.FAIL
            else:
                strm += TerminalColors.OKGREEN
            strm += chr(node_map[i][j])
            strm += TerminalColors.END
        strm += "\n"

    print(strm)


def main():
    global nodes
    global max_x
    global max_y
    heightmap = []

    sys.setrecursionlimit(100000)

    with open("input.txt") as f:
        for line in f.readlines():
            heightmap.append(line.strip())

    max_x = len(heightmap)
    max_y = len(heightmap[0])

    for line_n in range(len(heightmap)):
        for cell in range(len(line)):
            nodes.append(Node(line_n, cell, ord(heightmap[line_n][cell])))

    for i in range(len(nodes)):
        if nodes[i].height == ord("S"):
            nodes[i].height = ord("a") - 1
        if nodes[i].height == ord("E"):
            nodes[i].height = ord("z") + 1

    for node in nodes:
        if node.height == ord("a") - 1:
            node.dijkstra(0, node)
            break

    # print_map()

    for node in nodes:
        if node.height == ord("z") + 1:
            print(node.distance)
            break


if __name__ == "__main__":
    main()
