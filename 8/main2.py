# --- Day 8: Treetop Tree House ---
forest = []


def get_vs(row: int, col: int) -> int:
    global forest
    vis_from_top = 0
    vis_from_bottom = 0

    # check if border
    max_row = len(forest) - 1
    max_col = len(forest) - 1
    if row == 0:
        return 0
    if row >= max_row:
        return 0
    if col == 0:
        return 0
    if col >= max_col:
        return 0

    clt_top = 0
    clt_btm = max_row
    clt_lft = 0
    clt_rt = max_col

    # check from top
    for i in range(row - 1, -1, -1):
        if forest[row][col] <= forest[i][col]:
            clt_top = i
            break

    # check from bottom
    for i in range(row + 1, max_row + 1):
        if forest[row][col] <= forest[i][col]:
            clt_btm = i
            break

    vis_from_left = 0
    vis_from_right = 0
    # check from left
    for i in range(col - 1, -1, -1):
        if forest[row][col] <= forest[row][i]:
            clt_lft = i
            break
    # check from right
    for i in range(col + 1, max_col + 1):
        if forest[row][col] <= forest[row][i]:
            clt_rt = i
            break

    vis_from_top = row - clt_top
    vis_from_bottom = clt_btm - row
    vis_from_left = col - clt_lft
    vis_from_right = clt_rt - col

    vis = vis_from_top * vis_from_bottom * vis_from_left * vis_from_right
    return vis


def main():
    global forest

    with open("input.txt") as f:
        for line in f.readlines():
            forest.append(line)

    best_visible_score = 0
    max_row = len(forest)
    max_col = len(forest)
    for i in range(0, max_row):
        for j in range(0, max_col):
            if i == 3 and j == 2:
                pass
            score = get_vs(i, j)
            if score > best_visible_score:
                best_visible_score = score

    print(f"Best visibility score: {best_visible_score}")


if __name__ == "__main__":
    main()
