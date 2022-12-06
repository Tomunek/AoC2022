# --- Day 6: Tuning Trouble ---

def start(sig: str, cc: str) -> bool:
    packet = sig[cc - 4:cc]
    if packet[0] == packet[1] or packet[0] == packet[2] or packet[0] == packet[3]:
        return False
    if packet[1] == packet[2] or packet[1] == packet[3]:
        return False
    if packet[2] == packet[3]:
        return False
    return True


def detect_start(sig: str) -> int:
    current_char = 4

    while not start(sig, current_char):
        current_char += 1

    return current_char


def main():
    signal = ""

    with open("input.txt") as f:
        signal = f.readline()

    start_packet = detect_start(signal)
    print(f"Start packet occurs after {start_packet} characters")


if __name__ == "__main__":
    main()
