import sys

class Beacon:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        count = 1
        min_x = 1
        max_x = 1
        max_d = -1
        beacons = set()
        sensors = set()
        for line in self.get_lines(filename):
            s_part, b_part = line.split(":")
            s_coords = s_part.strip().split(" ")
            b_coords = b_part.strip().split(" ")
            s_x = int(s_coords[2].split("=")[1][:-1])
            s_y = int(s_coords[3].split("=")[1])

            b_x = int(b_coords[4].split("=")[1][:-1])
            b_y = int(b_coords[5].split("=")[1])

            dist = int(abs(s_x - b_x) + abs(s_y - b_y))
            sensors.add((s_x, s_y, dist))
            beacons.add((b_x, b_y))

            if s_x < min_x:
                min_x = s_x
            if s_x > max_x:
                max_x = s_x
            if max_d < dist:
                max_d = dist

        print("done creating")
        sol = set()
        for i in range(min_x - max_d - 1, max_x + max_d + 1):
            line = (i, 2000000)
            if i % 100000 == 0:
                print(i)
            for s in sensors:
                current_d = abs(line[0] - s[0]) + abs(line[1] - s[1])
                if current_d <= s[2] and line not in beacons:
                    count = count + 1 
                    sol.add((line))
                
        return len(sol)


    def run_part_two(self, filename: str) -> None:
        beacons = set()
        sensors = set()
        for line in self.get_lines(filename):
            s_part, b_part = line.split(":")
            s_coords = s_part.strip().split(" ")
            b_coords = b_part.strip().split(" ")
            s_x = int(s_coords[2].split("=")[1][:-1])
            s_y = int(s_coords[3].split("=")[1])

            b_x = int(b_coords[4].split("=")[1][:-1])
            b_y = int(b_coords[5].split("=")[1])

            dist = int(abs(s_x - b_x) + abs(s_y - b_y))
            sensors.add((s_x, s_y, dist))
            beacons.add((b_x, b_y))
        
        for s in sensors:
            print(s)
            perim = self.perim(s)
            for p in perim: # for every point on perimiter 
                belongs = False
                for s in sensors: # check distance to each s and see if d < that associated with that sensor
                    current_d = abs(p[0] - s[0]) + abs(p[1] - s[1])
                    if current_d <= s[2] and p not in beacons and p not in sensors:
                        belongs = True
                if not belongs:
                    print("found")
                    return (p[0]*4000000) + p[1]

        
            
        #walk the perimiter of each diamond
        #for s in sensors:

    #[x, y, distance to beacon] <- s
    def perim(self, s):
        # 4 sides
        side_len = s[2] + 1
        p = s[0]
        perimiter = set()

        left = (s[0] -side_len, s[1]) 
        top = (s[0], s[1] -side_len)
        right = (s[0] +side_len, s[1])
        bot = (s[0], s[1] + side_len)
        hypo = int(abs(left[0] - top[0]) + abs(left[1] -top[1]))
        next = left
        perimiter.add(self.in_limit(left))
        
        for i in range(int(hypo / 2)):
            next_up = (next[0], next[1] - 1)
            next_right = (next_up[0] +1, next_up[1])
            next = next_right
            
            perimiter.add(self.in_limit(next_up))
            perimiter.add(self.in_limit(next_right))

        next = top
        perimiter.add(self.in_limit(top))
        for i in range(int(hypo / 2)):
            next_right = (next[0] + 1, next[1])
            next_down = (next_right[0], next_right[1] + 1)
            next = next_down
            perimiter.add(self.in_limit(next_down))
            perimiter.add(self.in_limit(next_right))

        next = right
        perimiter.add(self.in_limit(right))
        for i in range(int(hypo / 2)):
            next_down = (next[0], next[1] + 1)
            next_left = (next_down[0] -1 , next_down[1])
            next = next_left
            perimiter.add(self.in_limit(next_down))
            perimiter.add(self.in_limit(next_left))

        next = bot
        perimiter.add(self.in_limit(bot))
        for i in range(int(hypo / 2)):
            next_left = (next[0] -1 , next[1])
            next_up = (next_left[0], next_left[1] - 1)
            
            next = next_up
            perimiter.add(self.in_limit(next_left))
            perimiter.add(self.in_limit(next_up))

        return perimiter
        
    def in_limit(self,p):
        if 0<p[0] and p[0] < 4000000 and 0<p[1] and p[1] < 4000000:
            return p
        else: return (-1,-1)
            
if __name__=="__main__":
    #elf = Beacon().run_part_one("/Users/michael/code/adventofcode/2022/day15/test.txt")
    #elf = Beacon().run_part_two("/Users/michael/code/adventofcode/2022/day15/test.txt")
    #elf = Beacon().run_part_one("input.txt")
    elf = Beacon().run_part_two("input.txt")
    print(elf)