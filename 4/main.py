# --- Day 4: Camp Cleanup ---


def main():
    pairs = []

    with open("input.txt") as f:
        pair = []
        for line in f.readlines():
            elfs = line.strip().split(",")
            pair.append((int(elfs[0].split("-")[0]), int(elfs[0].split("-")[1])))
            pair.append((int(elfs[1].split("-")[0]), int(elfs[1].split("-")[1])))
            pairs.append(pair)
            pair = []

    number_of_useless_pairs = 0
    for pair in pairs:
        if pair[0][0] <= pair[1][0]:
            if pair[0][1] >= pair[1][1]:
                number_of_useless_pairs += 1
                continue
        if pair[0][0] >= pair[1][0]:
            if pair[0][1] <= pair[1][1]:
                number_of_useless_pairs += 1
                continue

    print(f"Number of bad pairs: {number_of_useless_pairs}")


if __name__ == "__main__":
    main()
