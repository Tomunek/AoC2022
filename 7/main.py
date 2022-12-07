# --- Day 7: No Space Left On Device ---


class Directory:

    def __init__(self, _name, _parent):
        self.name = _name
        self.parent = _parent
        self.sub_dirs = {}
        self.sub_files = []

    def get_size(self) -> int:
        size = 0
        for key in self.sub_dirs.keys():
            size += self.sub_dirs[key].get_size()
        for sub_file in self.sub_files:
            size += int(sub_file.split(" ")[0].strip())
        return size

    def add_item(self, item):
        type_size = item.split(" ")[0]
        name = item.split(" ")[1].strip()
        if type_size == "dir":
            if name not in self.sub_dirs:
                new_dir = Directory(name, self)
                self.sub_dirs.update({name: new_dir})
        else:
            self.sub_files.append(item)

    def get_parent(self):
        return self.parent


exec_target = 0


def execute(inst):
    global exec_target
    if "$ cd /" in inst:
        new_dir = Directory("/", 0)
        exec_target = new_dir
        return new_dir

    if "$ " in inst:
        if " cd " in inst:
            inst_name = inst.split(" ")[2].strip()
            if inst_name == "..":
                exec_target = exec_target.get_parent()
            else:
                exec_target = exec_target.sub_dirs[inst_name]
        if " ls " in inst:
            pass
    else:
        exec_target.add_item(inst)

    return 0


def size_all(root):
    sizes = []
    for dir in root.sub_dirs.values():
        sizes.append(dir.get_size())
        sizes += size_all(dir)
    return sizes


def main():
    term = ""

    with open("input.txt") as f:
        term = f.readlines()

    root_dir = 0
    for i in term:
        a = execute(i)
        if a != 0:
            root_dir = a

    sizes = size_all(root_dir)
    small_sizes_sum = 0
    for size in sizes:
        if size <= 100000:
            small_sizes_sum += size

    print(f"Sum of sizes of all small directories: {small_sizes_sum}")


if __name__ == "__main__":
    main()
