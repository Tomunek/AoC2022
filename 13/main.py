# --- Day 13: Distress Signal ---
import copy


def compare_objs(a, b) -> int:
    print(f"Comparing {a} and {b}")
    if isinstance(a, int):
        if isinstance(b, list):
            return compare_objs([a], b)
        if isinstance(b, int):
            return b - a

    if isinstance(a, list):
        if isinstance(b, list):
            min_len = min(len(a), len(b))
            for i in range(min_len):
                cmp_res = compare_objs(a[i], b[i])
                if cmp_res != 0:
                    return cmp_res
            if len(a) > len(b):
                return -1
            if len(a) < len(b):
                return 1
            return 0
        if isinstance(b, int):
            return compare_objs(a, [b])


def eval_pair(pair) -> bool:
    pair_ok = True
    print(pair[0])
    print(pair[1])
    pair_ok = ((compare_objs(pair[0], pair[1])) > 0)
    print(pair_ok)
    return pair_ok


def main():
    pairs = []

    with open("input.txt") as f:
        pair = []
        for line in f.readlines():
            if line == '\n':
                pairs.append(copy.deepcopy(pair))
                pair = []
            else:
                pair.append(eval(line.strip().split()[0]))
    pairs.append(copy.deepcopy(pair))

    sum_of_ok_pair_i = 0
    for i in range(len(pairs)):
        if eval_pair(pairs[i]):
            sum_of_ok_pair_i += i + 1

    print(f"Sum of indices of pairs in order: {sum_of_ok_pair_i}")


if __name__ == "__main__":
    main()
