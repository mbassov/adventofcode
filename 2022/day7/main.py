class Node(object):
    def __init__(self, parent, name, value, kind):
        self.name = name
        self.value = value
        self.kind = kind
        self.parent = parent
        self.children = {}

class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, parent, name, value, kind):
        item = Node(parent, name, value, kind)          
        parent.children[name] = item

class Filesystem:
    root = Node(None, "root", 0, "dir")
    tree = Tree(root)

    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> int:
        self.make_tree(filename)
        self.compute_sizes(self.tree.root, sum)
        
        res = self.find_answer(self.tree.root)
        return res
    
    def find_answer(self, node: Node) -> int:
        queue = [node]
        sum = 0
        while len(queue) != 0:
            item = queue.pop()
            if item.value < 100000:
                sum += item.value
            for k, v in item.children.items():
                if v.kind == "dir":
                    queue.append(v)
        return sum

    def compute_sizes(self, node) -> int: 
        if node == None: return 0
        if node.kind == "dir":
            count = 0
            for k, v in node.children.items():
                res = self.compute_sizes(v)
                count += res
            node.value = count
            return count

        if node.kind == "file":
            return node.value

    def make_tree(self, filename: str) -> None:
        lines = self.get_lines(filename)
        i = 1 # skip the `cd /` command
        current = self.tree.root
        while i < len(lines):
            line = lines[i].rstrip()
            if line == "$ ls": # listing of a directory
                i = self.process_ls(lines, i + 1, current)
                continue
            if line.startswith("$ cd"):
                dir = line.split(" ")[2].rstrip()
                if dir == "..":
                    current = current.parent
                else: 
                    current = current.children.get(dir)
                i += 1
                continue
        return 

    def process_ls(self, lines: list[str], i: int, current: Node) -> None:
        line = lines[i]
        while not line.startswith("$"):
            listing = line.split(" ")
            if line.startswith("dir"):
                self.tree.insert(current, listing[1].rstrip(), 0, "dir")
            else: 
                self.tree.insert(current, listing[1].rstrip(), int(listing[0].rstrip()), "file")
            i += 1
            if i == len(lines):
                return i
            line = lines[i]
        return i

    def run_part_two(self, filename: str) -> None:
        # 48690120
        # remaining 21309880
        self.make_tree(filename)
        self.compute_sizes(self.tree.root)
        needed = 30000000 - (70000000 - self.tree.root.value)
        res = self.find_answer_2(self.tree.root, needed)  
        return res

    def find_answer_2(self, node: Node, needed) -> int:
        queue = [node]
        sizes = []
        while len(queue) != 0:
            item = queue.pop()
            sizes.append(item.value)
            for k, v in item.children.items():
                if v.kind == "dir":
                    queue.append(v)
        
        sizes.sort()

        for size in sizes:
            if size >= needed:
                return size



if __name__=="__main__":
    #elf = Filesystem().run_part_one("/Users/michael/code/adventofcode/2022/day7/test.txt")
    #elf = Filesystem().run_part_two("/Users/michael/code/adventofcode/2022/day7/test.txt")
    #elf = Filesystem().run_part_one("/Users/michael/code/adventofcode/2022/day7/input.txt")
    elf = Filesystem().run_part_two("/Users/michael/code/adventofcode/2022/day7/input.txt")
    print(elf)

