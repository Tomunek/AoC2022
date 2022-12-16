# --- Day 16: Proboscidea Volcanium ---
# I am an idiot. I forgot about cave loops. Distance algorithm needs to be rewritten
valves = []
usable_valves_i = []
total_pressure_leaked = 0


class Valve:
    def __init__(self, name, flow):
        self.name = name
        self.flow = flow
        self.state = False
        self.tunnels = []

    def add_tunel(self, tunnel):
        self.tunnels.append(tunnel)

    def open(self):
        self.state = True


def get_valve_index(name):
    global valves
    for i in range(len(valves)):
        if valves[i].name == name:
            return i


def dst_help(start: int, end: int, distances: [int], parents: [str]):
    if start == end:
        return "end"
    for tunel in valves[start].tunnels:
        if get_valve_index(tunel) != start and distances[get_valve_index(tunel)] == -1:
            distances[get_valve_index(tunel)] = distances[start] + 1
            if dst_help(get_valve_index(tunel), end, distances, parents) != "":
                return tunel
    return ""


def find_distance(start: int, end: int):
    global valves
    distances = [-1 for i in range(len(valves))]
    parents = ["" for i in range(len(valves))]
    distances[start] = 0
    direction = dst_help(start, end, distances, parents)
    return direction, distances[end]


def pass_time(time):
    global valves
    global total_pressure_leaked
    for valve in valves:
        if valve.state:
            total_pressure_leaked += valve.flow * time


def find_best_choice(position, time_left):
    global valves
    best_value = 0
    best_valve = -1
    if len(usable_valves_i) == 0:
        return -1
    for closed_valve in usable_valves_i:
        value = valves[closed_valve].flow * (time_left - (find_distance(get_valve_index(position), closed_valve)[1]-1))
        # value = time_left - find_distance(get_valve_index(position), closed_valve)[1]
        if value > best_value:
            best_value = value
            best_valve = closed_valve
    return best_valve


def main():
    global valves
    global total_pressure_leaked

    with open("example_input.txt") as f:
        for input_line in f.readlines():
            line_split_on_spaces = input_line.strip().split(" ")
            name = line_split_on_spaces[1]
            flow = int(line_split_on_spaces[4].strip("rate=;"))
            tunnels = line_split_on_spaces[9:]
            tunnels = [tunnel.strip(", \n") for tunnel in tunnels]
            v = Valve(name, flow)
            for tunnel in tunnels:
                v.add_tunel(tunnel)
            valves.append(v)

    for i in range(len(valves)):
        if valves[i].flow != 0:
            usable_valves_i.append(i)

    minute = 1
    position = "AA"
    valve_to_open = ""
    while minute < 30:
        print(f"M:{minute} TP:{total_pressure_leaked}")
        if valve_to_open == position:
            valves[get_valve_index(position)].open()
            print(f"Minute {minute}. Opened valve {position}")
            usable_valves_i.remove(get_valve_index(valve_to_open))
            valve_to_open = ""
            pass_time(1)
            minute += 1
            continue

        best_choice = find_best_choice(position, 30 - minute)
        if best_choice >= 0:
            valve_to_open = valves[best_choice].name
            direction, distance = find_distance(get_valve_index(position), get_valve_index(valve_to_open))
            print(f"P:{position} T:{valve_to_open} D:{direction} D:{distance}")
            position = direction
            pass_time(1)
            minute += 1
        else:
            pass_time(1)
            minute += 1

    print(f"Total pressure leaked in {minute} minutes: {total_pressure_leaked}")


if __name__ == "__main__":
    main()
