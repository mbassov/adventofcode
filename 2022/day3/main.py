from itertools import islice
import string

from more_itertools import batched

class Sack:
    _priorities =  string.ascii_lowercase + string.ascii_uppercase

    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        count = 0
        for line in self.get_lines(filename):
            lst = list(line.rstrip())
            middle = int(len(lst)/2)
            one = set(lst[:middle])
            two = set(lst[middle:])
            common = one.intersection(two)
            count += self.get_priority(common.pop())

        return count

    def run_part_two(self, filename: str) -> None:
        count = 0     
        for line in batched(self.get_lines(filename), 3):
            one = set(list(line[0].rstrip()))
            two = set(list(line[1].rstrip()))
            three = set(list(line[2].rstrip()))         
            common = one.intersection(two).intersection(three)     
            count += self.get_priority(common.pop())

        return count

    def get_priority(self, char: str) -> int:
        return self._priorities.index(char) + 1 # 1 base
            
if __name__=="__main__":
    #elf = Sack().run_part_one("test.txt")
    #elf = Sack().run_part_two("test.txt")
    #elf = Sack().run_part_one("input.txt")
    elf = Sack().run_part_two("input.txt")
    print(elf)