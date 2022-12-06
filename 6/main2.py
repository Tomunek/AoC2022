# --- Day 6: Tuning Trouble ---

def start_m(sig: str, cc: str) -> bool:
    packet = sig[cc - 14:cc]
    for i in range(13):
        for j in range(i + 1, 14):
            if packet[i] == packet[j]:
                return False
    return True


def detect_start_m(sig: str) -> int:
    current_char = 14

    while not start_m(sig, current_char):
        current_char += 1

    return current_char


def main():
    signal = ""

    with open("input.txt") as f:
        signal = f.readline()

    start_message = detect_start_m(signal)
    print(f"Message start packet occurs after {start_message} characters")


if __name__ == "__main__":
    main()
