# --- Day 13: Distress Signal ---
import functools


def compare_objs(a, b) -> int:
    # print(f"Comparing {a} and {b}")
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
    # print(pair[0])
    # print(pair[1])
    pair_ok = ((compare_objs(pair[0], pair[1])) > 0)
    # print(pair_ok)
    return pair_ok


def main():
    signals = []

    with open("input.txt") as f:
        for line in f.readlines():
            if line == '\n':
                pass
            else:
                signals.append(eval(line.strip().split()[0]))

    signals.append([[2]])
    signals.append([[6]])

    sorted_signals = sorted(signals, key=functools.cmp_to_key(compare_objs))[::-1]
    # print(signals)
    # print(sorted_signals)
    start_index = 0
    stop_index = 0
    for i in range(len(sorted_signals)):
        if sorted_signals[i] == [[2]]:
            start_index = i + 1
        if sorted_signals[i] == [[6]]:
            stop_index = i + 1

    decoder_key = start_index * stop_index

    print(f"Decoder key for the distress signal: {decoder_key}")


if __name__ == "__main__":
    main()
