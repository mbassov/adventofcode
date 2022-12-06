import collections
from itertools import islice

class Radio:
    
    def run_part_one(self, filename: str) -> int:
        return self.find_nth(filename, 4)

    def run_part_two(self, filename: str) -> int:
        return self.find_nth(filename, 14)

    def find_nth(self, filename: str, n: int) -> int:
        input = open(filename, "r").readline()
        count = 0
        for group in self.sliding_window(input, n):
            st = set(list(group))
            if len(st) == len(group):
                return count + n
            
            count +=1

        return None
    
    # credit https://docs.python.org/3/library/itertools.html
    def sliding_window(self, iterable, n):
        # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
        it = iter(iterable)
        window = collections.deque(islice(it, n), maxlen=n)
        if len(window) == n:
            yield tuple(window)
        for x in it:
            window.append(x)
            yield tuple(window)

if __name__=="__main__":
    #elf = Radio().run_part_one("test.txt")
    #elf = Radio().run_part_two("test.txt")
    #elf = Radio().run_part_one("input.txt")
    elf = Radio().run_part_two("input.txt")
    print(elf)