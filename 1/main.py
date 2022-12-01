# --- Day 1: Calorie Counting ---

def main():
    calories_by_elf = []

    with open("input.txt") as f:
        cals = []
        for line in f.readlines():
            if line == "\n":
                calories_by_elf.append(cals)
                cals = []
            else:
                cals.append(int(line))
        calories_by_elf.append(cals)

    total_calories_by_elf = []
    for i in range(len(calories_by_elf)):
        elf_sum = 0
        for meal in calories_by_elf[i]:
            elf_sum += meal
        total_calories_by_elf.append(elf_sum)

    most_calories = 0
    for elf in total_calories_by_elf:
        if elf > most_calories:
            most_calories = elf

    print(f"Most calories carried by one elf: {most_calories}")


if __name__ == "__main__":
    main()
