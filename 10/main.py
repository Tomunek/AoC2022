# --- Day 10: Cathode-Ray Tube ---

def sig_str(cc: int, x: int) -> int:
    if cc in [i for i in range(20, 221, 40)]:
        return cc * x
    return 0


def main():
    instructions = []

    with open("input.txt") as f:
        for line in f.readlines():
            instruction = (line[0:4])
            if instruction == "noop":
                instructions.append(("noop", 0))
            else:
                instructions.append((line.split(' ')[0], int(line.split(' ')[1].strip())))

    x = 1
    signal_strengths = 0
    cc = 0
    ic = 0
    while ic < len(instructions):
        if instructions[ic][0] == "noop":
            cc += 1
            signal_strengths += sig_str(cc, x)
        else:
            cc += 1
            signal_strengths += sig_str(cc, x)
            cc += 1
            signal_strengths += sig_str(cc, x)
            x += instructions[ic][1]
        ic += 1

    print(f"Sum of signal strengths: {signal_strengths}")


if __name__ == "__main__":
    main()
