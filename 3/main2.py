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
        for line in f.readlines():
            rucksacks.append(line.strip())

    badges = []

    for i in range(0, len(rucksacks), 3):
        for item in rucksacks[i]:
            if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
                badges.append(item)
                break

    print(f"Badges: {badges}")

    priority_sum = 0
    for item in badges:
        priority_sum += get_priority(item)

    print(f"Sum of priority of all badges: {priority_sum}")


if __name__ == "__main__":
    main()
