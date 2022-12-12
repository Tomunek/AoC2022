# --- Day 12: Hill Climbing Algorithm ---
import heapq

nodes = []
max_x = 0
max_y = 0


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
        self.visited = False

    def set_parent(self, daddy):
        self.daddy = daddy

    def set_distance(self, dist):
        self.distance = dist

    def visit(self):
        self.visited = True


def dijkstra(start_pos):
    global nodes
    queue = []

    heapq.heappush(queue, (nodes[start_pos].distance, start_pos))

    while queue:
        _, nodei = heapq.heappop(queue)
        nodes[nodei].visit()

        neighbours = []
        # up
        if nodes[nodei].x > 0:
            if get_node(nodes[nodei].x - 1, nodes[nodei].y).height <= nodes[nodei].height + 1:
                neighbours.append(get_node_pos(nodes[nodei].x - 1, nodes[nodei].y))

        # down
        if nodes[nodei].x < max_x - 1:
            if get_node(nodes[nodei].x + 1, nodes[nodei].y).height <= nodes[nodei].height + 1:
                neighbours.append(get_node_pos(nodes[nodei].x + 1, nodes[nodei].y))

        # left
        if nodes[nodei].y > 0:
            if get_node(nodes[nodei].x, nodes[nodei].y - 1).height <= nodes[nodei].height + 1:
                neighbours.append(get_node_pos(nodes[nodei].x, nodes[nodei].y - 1))

        # right
        if nodes[nodei].y < max_y - 1:
            if get_node(nodes[nodei].x, nodes[nodei].y + 1).height <= nodes[nodei].height + 1:
                neighbours.append(get_node_pos(nodes[nodei].x, nodes[nodei].y + 1))

        for neighbour in neighbours:
            if not nodes[neighbour].visited:
                if nodes[neighbour].distance > nodes[nodei].distance + 1:
                    nodes[neighbour].set_parent = nodei
                    nodes[neighbour].distance = nodes[nodei].distance + 1
                    heapq.heappush(queue, (nodes[neighbour].distance, neighbour))


def get_node(x: int, y: int) -> Node:
    global nodes
    for node in nodes:
        if node.x == x and node.y == y:
            return node


def get_node_pos(x: int, y: int) -> int:
    global nodes
    for i in range(len(nodes)):
        if nodes[i].x == x and nodes[i].y == y:
            return i


def main():
    global nodes
    global max_x
    global max_y
    heightmap = []

    with open("input.txt") as f:
        for line in f.readlines():
            heightmap.append(line.strip())

    max_x = len(heightmap)
    max_y = len(heightmap[0])

    for line_n in range(len(heightmap)):
        for cell in range(len(line)):
            nodes.append(Node(line_n, cell, ord(heightmap[line_n][cell])))

    start_pos = 0

    for i in range(len(nodes)):
        if nodes[i].height == ord("S"):
            nodes[i].height = ord("a") - 1
            nodes[i].distance = 0
            start_pos = i
        if nodes[i].height == ord("E"):
            nodes[i].height = ord("z") + 1

    dijkstra(start_pos)

    for node in nodes:
        if node.height == ord("z") + 1:
            print(f"Length of the shortest path from S to E: {node.distance}")
            break


if __name__ == "__main__":
    main()
