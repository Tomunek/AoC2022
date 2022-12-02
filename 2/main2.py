# --- Day 2: Rock Paper Scissors ---

def round_score(one_round: [int]) -> int:
    score = 0

    # i must loose
    if one_round[1] == "X":
        score += 0
        if one_round[0] == "B":
            score += 1
        elif one_round[0] == "A":
            score += 3
        elif one_round[0] == "C":
            score += 2
    # i must draw
    elif one_round[1] == "Y":
        score += 3
        if one_round[0] == "C":
            score += 3
        elif one_round[0] == "B":
            score += 2
        elif one_round[0] == "A":
            score += 1
    # i must win
    elif one_round[1] == "Z":
        score += 6
        if one_round[0] == "A":
            score += 2
        elif one_round[0] == "C":
            score += 1
        elif one_round[0] == "B":
            score += 3

    return score


def main():
    rounds = []

    with open("input.txt") as f:
        one_round = []
        for line in f.readlines():
            one_round = line.split(" ")[0].strip(), line.split(" ")[1].strip()
            rounds.append(one_round)

    total_score = 0
    for r in rounds:
        total_score += round_score(r)

    print(f"Total score (with full strategy): {total_score}")


if __name__ == "__main__":
    main()
