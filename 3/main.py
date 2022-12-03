# --- Day 3: Rucksack Reorganization ---

def get_priority(item) -> int:
    if "a" <= item <= "z":
        return ord(item) - 96
    if "A" <= item <= "Z":
        return ord(item) - 64 + 26
    return -1


def main():
    rucksacks = []

    with open("input.txt") as f:
        rucksack = []
        for line in f.readlines():
            rucksack.append(line[0:int(len(line) / 2)])
            rucksack.append(line[int(len(line) / 2):].strip())
            rucksacks.append(rucksack)
            rucksack = []

    bad_placed_items = []
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                bad_placed_items.append(item)
                break

    print(f"Misplaced items: {bad_placed_items}")

    priority_sum = 0
    for item in bad_placed_items:
        priority_sum += get_priority(item)

    print(f"Sum of priorities of misplaced items: {priority_sum}")


if __name__ == "__main__":
    main()
