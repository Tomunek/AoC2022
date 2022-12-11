# --- Day 11: Monkey in the Middle ---
# I HATE MODULO ARITHMETIC
# GET OUT OF MY HEAD
# I HATE MODULO ARITHMETIC
# GET OUT OF MY HEAD
# I HATE MODULO ARITHMETIC
# GET OUT OF MY HEAD
# I HATE MODULO ARITHMETIC
# GET OUT OF MY HEAD

monkes_nww = 1


class Monke:
    global monkes_nww

    def __init__(self, op, test, true_target, false_target):
        self.op = op
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspect_counter = 0

    def test_item(self, item: int):
        self.inspect_counter += 1
        old = item
        new = eval(self.op)
        new_to_ret = new % monkes_nww
        if new % self.test == 0:
            return new_to_ret, self.true_target
        else:
            return new_to_ret, self.false_target


def main():
    monke_items = []
    monkes = []
    global monkes_nww

    with open("input.txt") as f:
        lines = f.readlines()
        for m_lines in range(0, len(lines), 7):
            starting_items = lines[m_lines + 1][17:].strip().split(", ")
            starting_items_as_int = []
            for si in starting_items:
                starting_items_as_int.append(int(si.strip()))
            monke_items.append(starting_items_as_int)
            operation = lines[m_lines + 2][18:].strip()
            test = int(lines[m_lines + 3][20:].strip())
            monkes_nww *= test
            tt = int(lines[m_lines + 4][28:].strip())
            tf = int(lines[m_lines + 5][29:].strip())
            monke = Monke(operation, test, tt, tf)
            monkes.append(monke)

    turns = 10000
    for turn in range(turns):
        for m_num in range(len(monkes)):
            monke = monkes[m_num]
            for i_num in range(len(monke_items[m_num])):
                throw_to = monke.test_item(monke_items[m_num][i_num])
                monke_items[m_num][i_num] = throw_to[0]
                monke_items[throw_to[1]].append(monke_items[m_num][i_num])
                monke_items[m_num][i_num] = -1
            monke_items[m_num][:] = (value for value in monke_items[m_num] if value != -1)

    print(monke_items)
    two_best_monkes = [0, 0]
    for mk in monkes:
        if mk.inspect_counter > two_best_monkes[1]:
            two_best_monkes[0] = two_best_monkes[1]
            two_best_monkes[1] = mk.inspect_counter
        elif mk.inspect_counter > two_best_monkes[0]:
            two_best_monkes[0] = mk.inspect_counter

    print(two_best_monkes)

    print(
        f"Level of monkey business after {turns} rounds (with extra stress): {two_best_monkes[0] * two_best_monkes[1]}")


if __name__ == "__main__":
    main()
