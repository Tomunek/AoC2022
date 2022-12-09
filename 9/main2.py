# --- Day 9: Rope Bridge ---
from math import sqrt


def draw(t):
    screen = ""
    for i in range(10, -10, -1):
        for j in range(-10, 10):
            d = False
            if t[0][0] == j and t[0][1] == i:
                screen += 'H'
                d = True
                continue
            for k in range(1, len(t)):
                if t[k][0] == j and t[k][1] == i:
                    screen += str(k)
                    d = True
                    break

            if not d:
                screen += "."
        screen += "\n"
    print(screen)


def sign(i):
    if i > 0:
        return 1
    if i < 0:
        return -1
    return 0


def main():
    moves = []
    visited_by_tail = []

    with open("input.txt") as f:
        for line in f.readlines():
            moves.append((line.split(' ')[0], int(line.split(' ')[1].strip())))

    # head_position = [0, 0] replaced by tail[0]
    tails_positions = [[0, 0] for i in range(10)]
    tails_positions_prev = [[0, 0] for i in range(10)]

    for move in moves:
        print(move)
        for i in range(move[1]):
            if (tails_positions[9][0], tails_positions[9][1]) not in visited_by_tail:
                visited_by_tail.append((tails_positions[9][0], tails_positions[9][1]))
            for n in range(len(tails_positions)):
                tails_positions_prev[n] = tails_positions[n].copy()
            # move head
            if move[0] == "R":
                tails_positions[0][0] += 1
            if move[0] == "L":
                tails_positions[0][0] -= 1
            if move[0] == "U":
                tails_positions[0][1] += 1
            if move[0] == "D":
                tails_positions[0][1] -= 1
            # move tails
            for nn in range(1, len(tails_positions)):
                ht_distance = sqrt(
                    (float(tails_positions[nn - 1][0] - tails_positions[nn][0])) ** 2 + float(
                        (tails_positions[nn - 1][1] - tails_positions[nn][1])) ** 2)
                if ht_distance >= 1.5:
                    # direct
                    if abs(tails_positions[nn][0] - tails_positions[nn - 1][0]) == 2 or \
                            abs(tails_positions[nn][1] - tails_positions[nn - 1][1]) == 2:
                        if tails_positions[nn][0] == tails_positions[nn - 1][0]:
                            tails_positions[nn][1] += sign(tails_positions[nn - 1][1] - tails_positions[nn][1])
                            continue
                        if tails_positions[nn][1] == tails_positions[nn - 1][1]:
                            tails_positions[nn][0] += sign(tails_positions[nn - 1][0] - tails_positions[nn][0])
                            continue

                    # diagonal
                    tails_positions[nn][0] += sign(tails_positions[nn - 1][0] - tails_positions[nn][0])
                    tails_positions[nn][1] += sign(tails_positions[nn - 1][1] - tails_positions[nn][1])

                    # print(f"moving {nn} to {tails_positions[nn]}")
            # draw(tails_positions)

    if (tails_positions[9][0], tails_positions[9][1]) not in visited_by_tail:
        visited_by_tail.append((tails_positions[9][0], tails_positions[9][1]))

    # print(tails_positions)
    print(f"Number of spaces visited by tail: {len(visited_by_tail)}")


if __name__ == "__main__":
    main()
