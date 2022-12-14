class Reservoir:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        count = 0
        map = self.make_map(filename)
        max_y = self.get_limits(map)
        # falling sand
        count = 0
        while True:
            count += 1
            location = self.next_fall(map, (500,0), max_y)
            if not location:
                return count -1 
            print(location)
            map[location] = "o"

    def get_limits(self, map):
        max_y = -1
        for k in map.keys():
            if max_y < k[1]:
                max_y = k[1]

        return max_y


    def next_fall(self, map, current, max_y):
        if current[1] > max_y:
            return None
        # try fall down
        if (current[0], current[1] + 1) not in map: 
            return self.next_fall(map, (current[0], current[1] + 1), max_y)
        # try fall left
        if (current[0]-1, current[1] + 1) not in map: 
            return self.next_fall(map, (current[0]-1, current[1] + 1), max_y)
        #try fall right
        if (current[0]+1, current[1] + 1) not in map: 
            return self.next_fall(map, (current[0]+1, current[1] + 1), max_y)
        return current

    def make_map(self, filename) -> dict:
        map = {}
        for line in self.get_lines(filename):
            parts = line.split("->")
            start_x, start_y = [int(v) for v in parts[0].strip().split(",")]
            for p in parts[1:]:
                next_x, next_y = [int(v) for v in p.strip().split(",")]
                if start_x == next_x: # draw vertical
                    length = abs(start_y - next_y) + 1
                    s = min(start_y, next_y)
                    for i in range(length):
                        map[(start_x, s+i)] = '#'
                else: #draw horizontal
                    length = abs(start_x - next_x) + 1
                    s = min(start_x, next_x)
                    for i in range(length):
                        map[(s+i, start_y)] = '#'

                start_x = next_x
                start_y = next_y
        return map

    def run_part_two(self, filename: str) -> None:
        count = 0
        map = self.make_map(filename)
        max_y = self.get_limits(map)

        for i in range(0,1000):
            map[(i, max_y + 2)] = '#'

        # falling sand
        count = 0
        while True:
            count += 1
            location = self.next_fall(map, (500,0), max_y + 2)
            if not location or location == (500,0): 
                return count
            print(location)
            map[location] = "o"

            
if __name__=="__main__":
    #elf = Reservoir().run_part_one("/Users/michael/code/adventofcode/2022/day14/test.txt")
    #elf = Reservoir().run_part_two("/Users/michael/code/adventofcode/2022/day14/test.txt")
    #elf = Reservoir().run_part_one("input.txt")
    elf = Reservoir().run_part_two("input.txt")
    print(elf)