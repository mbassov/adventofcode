import math

class Monkey:
    inspected =0
    def __init__(self, number: int):
        self.num = number
    
    def set_items(self, items: list[int]):
        self.items = items

    def add_item(self, item:int):
        self.items.append(item)
    
    def get_items(self) -> list[int]:
        return self.items

    def set_operation(self, op: str, num: str):
        self.op = op
        self.op_n = num

    def get_operation(self, old: int) -> int:
        op_n = old
        if self.op_n != "old":
            op_n = int(self.op_n)

        if self.op == "*":
            return op_n * old
        if self.op == "+":
            return op_n + old
        raise Exception("wrong op")

    def get_div(self):
        return self.div_by

    def set_test(self, d: int, p:int, n: int) -> None:
        self.div_by = d
        self.positive = p
        self.negative = n

    def get_test(self, level: int) -> int:
        if level % self.div_by == 0:
            return self.positive
        return self.negative

    def set_inspected(self):
        self.inspected = self.inspected +1

    def get_inspected(self):
        return self.inspected

    def get_obj_class(self) -> type:
        return self.o.__class__

class Middle:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        return self.run(filename, 20, 3)

    def run_part_two(self, filename: str) -> None:
        return self.run(filename, 10000, 1)

    def common_mult(self, monkeys):
        comm = 1
        for k,v in monkeys.items():
            comm = comm * v.get_div()

        return comm

    def run(self, filename, rounds, relief):
        monkeys = self.populate(filename)
        self.play(monkeys, rounds, relief)
        counts = {}
        for k,v in monkeys.items():
            counts[k]=v.get_inspected()

        nums = sorted(counts.values())
        return nums[-1]* nums[-2]

    def play(self, monkeys, rounds, relief):
        comm = self.common_mult(monkeys)
        for i in range (rounds):
            for num in monkeys.keys():
                monkey = monkeys[num]
                for item in monkey.get_items():
                    worry = math.floor(monkey.get_operation(item)//relief)
                    worry = worry % comm
                    next_monkey = monkey.get_test(worry)
                    monkeys[next_monkey].add_item(worry)
                    monkey.set_inspected()
                monkey.set_items([])
                
            #self.print_monkeys(monkeys)

    def print_monkeys(self, monkeys):
        for k, v in monkeys.items():
            print("Monkey " + str(k) + " :" , end="")
            print(v.get_items())


    def populate(self, filename: str) -> dict['Monkey']:
        lines = self.get_lines(filename)
        i = 0
        monkeys = {}
        while i < len(lines):
            line = lines[i]
            if line.startswith("Monkey"):
                m, n = line.split(" ")
                num = int(list(n)[0])
                monkey = self.process_monkey(num, lines, i)
                monkeys[num] = monkey
            i = i + 1

        return monkeys

    def process_monkey(self, num: int, lines: list[str], i: int) -> 'Monkey':
        monkey = Monkey(num)
        items = lines[i+1]
        first, second = items.split(":")
        each = [int(i) for i in second.strip().split(",")]
        monkey.set_items(each)

        operation = lines[i+2]
        ops= operation.split(" ")
        monkey.set_operation(ops[6], ops[7].rstrip())

        div = lines[i+3]
        d = int(div.strip().split(" ")[3].strip())
        tr = lines[i+4]
        t = int(tr.strip().split(" ")[5].strip())
        fal = tr = lines[i+5]
        f = int(fal.strip().split(" ")[5].strip())
        monkey.set_test(d, t, f)
        return monkey



            
if __name__=="__main__":
    #elf = Middle().run_part_one("test.txt")
    #elf = Middle().run_part_two("test.txt")
    #elf = Middle().run_part_one("input.txt")
    elf = Middle().run_part_two("input.txt")
    print(elf)