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

    # must have x and y coordinates between 0 and 4.000.000
    max_coord = 4000000
    distress_x = 0
    distress_y = 0

    possible_spaces = []
    sensor_num = 1

    for sensor in sensors:
        print(f"Processing sensor {sensor_num}")
        sensor_num += 1
        x = sensor.x
        for y in range(sensor.y - sensor.brange - 1, sensor.y):
            if y > max_coord or x > max_coord:
                break
            possible_spaces.append((x, y))
            x += 1
        x = sensor.x + sensor.brange + 1
        for y in range(sensor.y, sensor.y + sensor.brange + 1):
            if y > max_coord or x < 0:
                break
            possible_spaces.append((x, y))
            x -= 1
        x = sensor.x
        for y in range(sensor.y + sensor.brange + 1, sensor.y, -1):
            if y < 0 or x < 0:
                break
            possible_spaces.append((x, y))
            x -= 1
        x = sensor.x - sensor.brange - 1
        for y in range(sensor.y, sensor.y - sensor.brange - 1, -1):
            if y < 0 or x > max_coord:
                break
            possible_spaces.append((x, y))
            x += 1

    print(f"Spaces to consider: {len(possible_spaces)}")

    for i in range(len(possible_spaces)):
        if possible_spaces[i][0] < 0 or \
                possible_spaces[i][0] > max_coord or \
                possible_spaces[i][1] < 0 or \
                possible_spaces[i][1] > max_coord:
            possible_spaces[i] = (-1, -1)
    possible_spaces = list(filter((-1, -1).__ne__, possible_spaces))
    print(f"Spaces to consider after trimming: {len(possible_spaces)}")

    for i in range(len(possible_spaces)):
        for sensor in sensors:
            if abs(sensor.x - possible_spaces[i][0]) + abs(sensor.y - possible_spaces[i][1]) <= sensor.brange:
                possible_spaces[i] = (-1, -1)
                break
    possible_spaces = list(filter((-1, -1).__ne__, possible_spaces))
    print(f"Spaces to consider after sensoring: {len(possible_spaces)}")

    for i in range(len(possible_spaces)):
        for sensor in sensors:
            if possible_spaces[i] == (sensor.x, sensor.y) or possible_spaces == (sensor.bx, sensor.by):
                possible_spaces[i] = (-1, -1)
    possible_spaces = list(filter((-1, -1).__ne__, possible_spaces))

    distress_x = possible_spaces[0][0]
    distress_y = possible_spaces[0][1]
    tuning_freq = distress_x * 4000000 + distress_y
    print(f"{distress_x}:{distress_y}")
    print(f"Distress beacons tuning frequency: {tuning_freq}")


if __name__ == "__main__":
    main()
