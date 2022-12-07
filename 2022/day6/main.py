from more_itertools import sliding_window

class Radio:
    
    def run_part_one(self, filename: str) -> int:
        return self.find_nth(filename, 4)

    def run_part_two(self, filename: str) -> int:
        return self.find_nth(filename, 14)

    def find_nth(self, filename: str, n: int) -> int:
        input = open(filename, "r").readline()
        count = 0
        for group in sliding_window(input, n):
            st = set(list(group))
            if len(st) == len(group):
                return count + n
            
            count +=1

        return None

if __name__=="__main__":
    #elf = Radio().run_part_one("test.txt")
    #elf = Radio().run_part_two("test.txt")
    #elf = Radio().run_part_one("input.txt")
    elf = Radio().run_part_two("input.txt")
    print(elf)