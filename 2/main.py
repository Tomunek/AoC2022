# --- Day 2: Rock Paper Scissors ---

def round_score(one_round: [int]) -> int:
    score = 0

    # i have rock
    if one_round[1] == "X":
        score += 1
        if one_round[0] == "B":
            pass
        elif one_round[0] == "A":
            score += 3
        elif one_round[0] == "C":
            score += 6
    # i have paper
    elif one_round[1] == "Y":
        score += 2
        if one_round[0] == "C":
            pass
        elif one_round[0] == "B":
            score += 3
        elif one_round[0] == "A":
            score += 6
    # i have scissors
    elif one_round[1] == "Z":
        score += 3
        if one_round[0] == "A":
            pass
        elif one_round[0] == "C":
            score += 3
        elif one_round[0] == "B":
            score += 6

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

    print(f"Total score: {total_score}")


if __name__ == "__main__":
    main()
