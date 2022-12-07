from itertools import islice
from typing import Tuple

from more_itertools import batched

class Supplies:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> str:
        (stacks, moves) = self.split_data(filename)
        stacks = self.make_stacks(stacks)
        tops = self.make_moves(stacks, moves)
                
        return tops

    def split_data(self, filename: str) -> Tuple[list[str], list[str]]:
        stacks = []
        moves = []
        take_stacks = True
        for line in self.get_lines(filename):
            if line == "\n":
                take_stacks = False
                continue
            if take_stacks: 
                stacks.append(line)
            else:
                moves.append(line)
        return (stacks, moves)

    def make_stacks(self, stack_lines: list[str]):
        # read the 1 2 3 ... line and get the last value
        num_stacks = int(stack_lines[-1].rstrip().split(" ")[-1])
        stacks = {}
        for i in range(num_stacks):
            stacks[i+1] = [] # input is 1 based
        values = stack_lines[:-1]
        values.reverse() # so we can read it backwards to load the stack
        
        for row in values:
            # handle the empty values on the row by taking 4 chars at a time
            for i, one in enumerate(batched(list(row), 4)):
                if one[1] == ' ':
                    continue
                stacks[i+1].append(one[1])

        return stacks
    
    def make_moves(self, stacks: list[str], moves: list[str]):
        for move in moves:
            line = move.rstrip().split(" ")
            # perform the move operation i many times and just copy from stack to stack
            for i in range(int(line[1])):
                item = stacks.get(int(line[3])).pop()
                stacks.get(int(line[5])).append(item)
        
        # build the result by taking the top item from each stack
        result = ""
        for k,v in stacks.items():
            result += v.pop()
        return result

    def run_part_two(self, filename: str) -> None:
        (stacks, moves) = self.split_data(filename)
        stacks = self.make_stacks(stacks)
        tops = self.make_moves_9001(stacks, moves)
                
        return tops
    
    def make_moves_9001(self, stacks: list[str], moves: list[str]):
        for move in moves:
            line = move.rstrip().split(" ")
            tmp = []
            for i in range(int(line[1])):
                item = stacks.get(int(line[3])).pop()
                # instead of writing directly to the destination stack,
                # first write to a temp stack and then copy from there
                # just to keep the order
                tmp.append(item)
            
            for i in range(int(line[1])):
                stacks.get(int(line[5])).append(tmp.pop())
        
        # build the result by taking the top item from each stack
        result = ""
        for k,v in stacks.items():
            result += v.pop()
        return result
        
if __name__=="__main__":
    #elf = Supplies().run_part_one("/Users/michael/code/adventofcode/2022/day5/test.txt")
    #elf = Supplies().run_part_two("/Users/michael/code/adventofcode/2022/day5/test.txt")
    #elf = Supplies().run_part_one("/Users/michael/code/adventofcode/2022/day5/input.txt")
    elf = Supplies().run_part_two("input.txt")
    print(elf)