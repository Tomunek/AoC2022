# --- Day 10: Cathode-Ray Tube ---

def handle_crt(cc: int, x: int) -> str:
    ret = ""

    h_pos = cc % 40
    if h_pos == x - 1 or h_pos == x or h_pos == x + 1:
        ret += "#"
    else:
        ret += "."

    if cc in [i for i in range(39, 240, 40)]:
        ret += "\n"

    return ret


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
    crt = ""
    cc = 0
    ic = 0
    while ic < len(instructions):
        if instructions[ic][0] == "noop":
            cc += 1
            crt += handle_crt(cc - 1, x)
        else:
            cc += 1
            crt += handle_crt(cc - 1, x)
            cc += 1
            crt += handle_crt(cc - 1, x)
            x += instructions[ic][1]
        ic += 1

    print(crt)


if __name__ == "__main__":
    main()
