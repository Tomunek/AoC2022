# --- Day 8: Treetop Tree House ---
forest = []


def is_visible(row: int, col: int) -> bool:
    global forest
    is_vis = False
    is_vis_from_top = True
    is_vis_from_bottom = True

    # check if border
    max_row = len(forest) - 1
    max_col = len(forest) - 1
    if row == 0 or col == 0 or row >= max_row or col >= max_col:
        return True

    # check from top
    for i in range(row):
        if forest[row][col] <= forest[i][col]:
            is_vis_from_top = False
    # check from bottom
    for i in range(row + 1, max_row + 1):
        if forest[row][col] <= forest[i][col]:
            is_vis_from_bottom = False

    is_vis_from_left = True
    is_vis_from_right = True
    # check from left
    for i in range(col):
        if forest[row][col] <= forest[row][i]:
            is_vis_from_left = False
    # check from right
    for i in range(col + 1, max_col + 1):
        if forest[row][col] <= forest[row][i]:
            is_vis_from_right = False

    is_vis = is_vis_from_top or is_vis_from_bottom or is_vis_from_left or is_vis_from_right
    return is_vis


def main():
    global forest

    with open("input.txt") as f:
        for line in f.readlines():
            forest.append(line)

    visible_count = 0
    max_row = len(forest)
    max_col = len(forest)
    for i in range(0, max_row):
        for j in range(0, max_col):
            if is_visible(i, j):
                visible_count += 1

    print(f"Number of visible trees: {visible_count}")


if __name__ == "__main__":
    main()
