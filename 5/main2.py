# --- Day 5: Supply Stacks ---

stacks = []


def execute(command: str):
    global stacks
    move_number = int(command.split(" ")[1])
    move_from = int(command.split(" ")[3]) - 1
    move_to = int(command.split(" ")[5]) - 1
    crane = []
    elements_to_remove = []
    for i in range(-move_number, 0, 1):
        crane.append(stacks[move_from][i])
        elements_to_remove.append(i)
    for i in elements_to_remove:
        stacks[move_from].pop(i)
    stacks[move_to] += crane


def main():
    global stacks
    stack_count = 0
    stack_lines = []
    commands = []

    with open("input.txt") as f:
        for line in f.readlines():
            if "move" in line:
                commands.append(line.strip())
            elif line != "\n":
                if ' 1 ' in line:
                    stack_count = len(line.split("   "))
                else:
                    stack_line = [line[i:i + 4] for i in range(0, len(line), 4)]
                    stack_lines.append(stack_line)

    stacks = [[] for i in range(stack_count)]

    for row_num in range(len(stack_lines) - 1, -1, -1):
        for stack_num in range(stack_count):
            if stack_lines[row_num][stack_num] != '    ':
                if stack_lines[row_num][stack_num] != '   \n':
                    stacks[stack_num].append(stack_lines[row_num][stack_num].strip().replace("[", "").replace("]", ""))

    for command in commands:
        execute(command)

    message = ""
    for stack in stacks:
        message += stack[-1]

    print(f"Containers on top: {message}")


if __name__ == "__main__":
    main()
