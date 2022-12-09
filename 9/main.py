# --- Day 9: Rope Bridge ---
from math import sqrt


def draw(h, t):
    screen = ""
    for i in range(10, -10, -1):
        for j in range(-10, 10):
            if (h[1] == i and h[0] == j):
                screen += 'H'
            elif (t[1] == i and t[0] == j):
                screen += 'T'
            else:
                screen += "."
        screen += "\n"
    print(screen)


def main():
    moves = []
    visited_by_tail = []

    with open("input.txt") as f:
        for line in f.readlines():
            moves.append((line.split(' ')[0], int(line.split(' ')[1].strip())))

    head_position = [0, 0]
    tail_position = [0, 0]
    head_prev = [0, 0]

    for move in moves:
        print(move)
        for i in range(move[1]):
            if (tail_position[0], tail_position[1]) not in visited_by_tail:
                visited_by_tail.append((tail_position[0], tail_position[1]))
            head_prev = head_position.copy()
            # move head
            if move[0] == "R":
                head_position[0] += 1
            if move[0] == "L":
                head_position[0] -= 1
            if move[0] == "U":
                head_position[1] += 1
            if move[0] == "D":
                head_position[1] -= 1
            # move tail
            ht_distance = sqrt(
                (float(tail_position[0] - head_position[0])) ** 2 + float((tail_position[1] - head_position[1])) ** 2)
            if ht_distance >= 1.5:
                tail_position = head_prev.copy()

    if (tail_position[0], tail_position[1]) not in visited_by_tail:
        visited_by_tail.append((tail_position[0], tail_position[1]))

    print(f"Number of spaces visited by tail: {len(visited_by_tail)}")


if __name__ == "__main__":
    main()
