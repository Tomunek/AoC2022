# --- Day 15: Beacon Exclusion Zone ---
sensors = []


class Sensor:
    def __init__(self, x, y, brange, bx, by):
        self.x = x
        self.y = y
        self.brange = brange
        self.bx = bx
        self.by = by


def main():
    global sensors

    with open("input.txt") as f:
        for input_line in f.readlines():
            line_split_on_equals = input_line.strip().split("=")
            x = int(line_split_on_equals[1].split(",")[0])
            y = int(line_split_on_equals[2].split(":")[0])
            bx = int(line_split_on_equals[3].split(",")[0])
            by = int(line_split_on_equals[4])
            r = abs(x - bx) + abs(y - by)
            sensors.append(Sensor(x, y, r, bx, by))

    for sensor in sensors:
        print(f"{sensor.x},{sensor.y} -> {sensor.bx},{sensor.by} ({sensor.brange})")

    selected_y = 2000000
    selected_y_clear = [0 for i in range(selected_y * 4)]
    offset = selected_y
    for sensor in sensors:
        if sensor.y + sensor.brange < selected_y or sensor.y - sensor.brange > selected_y:
            continue
        for i in range(sensor.x - sensor.brange, sensor.x + sensor.brange + 1):
            if abs(sensor.x - i) + abs(sensor.y - selected_y) <= sensor.brange:
                selected_y_clear[i + offset] = 1

    for sensor in sensors:
        if sensor.by == selected_y:
            selected_y_clear[sensor.bx + offset] = 2

    selected = 0
    for y in selected_y_clear:
        if y == 1:
            selected += 1

    print(f"Number of beaconless squares in y {selected_y}: {selected}")


if __name__ == "__main__":
    main()
