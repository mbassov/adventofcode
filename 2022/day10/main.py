class Sections:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        lines = self.get_lines(filename)
        cycle = 1
        X = 1 
        i = 0
        count = 0
        busy_count = 0
        to_add = 0
        while True:
            # done when finished all input
            if len(lines) == i:
                break

            if busy_count == 0:
                instruction = lines[i].rstrip()

                if instruction == "noop":
                    i = i + 1
                    busy_count = 1
                else:
                    op, val = instruction.split(" ")
                    to_add =  int(val)
                    i = i + 1
                    busy_count = 2
            
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle== 180 or cycle == 220 or cycle == 260:
                print(X)
                count = count + (cycle * X)
            
            cycle = cycle + 1
            busy_count = busy_count - 1

            if busy_count == 0:
                X = X + to_add
                to_add = 0

        return count

    def run_part_two(self, filename: str) -> None:
        lines = self.get_lines(filename)
        cycle = 1
        X = 1 
        i = 0
        count = 0
        busy_count = 0
        to_add = 0
        crt_position = 0 
        
        while True:
            # done when finished all input
            if len(lines) == i:
                break

            if busy_count == 0:
                instruction = lines[i].rstrip()

                if instruction == "noop":
                    i = i + 1
                    busy_count = 1
                else:
                    op, val = instruction.split(" ")
                    to_add =  int(val)
                    i = i + 1
                    busy_count = 2
            
            
                
            if crt_position == X or crt_position == X +1 or crt_position == X -1:
                print("#", end="")
            else: 
                print(" ", end="")
            
            crt_position = crt_position + 1
            if cycle % 40 == 0:
                print("\n")
                crt_position = 0 
            
            

            cycle = cycle + 1
            busy_count = busy_count - 1

            if busy_count == 0:
                X = X + to_add
                to_add = 0

        return count
            
if __name__=="__main__":
    #elf = Sections().run_part_one("/Users/michael/code/adventofcode/2022/day10/test.txt")
    #elf = Sections().run_part_two("/Users/michael/code/adventofcode/2022/day10/test.txt")
    #elf = Sections().run_part_one("/Users/michael/code/adventofcode/2022/day10/input.txt")
    elf = Sections().run_part_two("/Users/michael/code/adventofcode/2022/day10/input.txt")
    print(elf)