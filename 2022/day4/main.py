class Sections:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        count = 0
        for line in self.get_lines(filename):
            pair = line.split(",")

            one_min_max = pair[0].split("-")
            two_min_max = pair[1].split("-")

            one_min = int(one_min_max[0])
            one_max = int(one_min_max[1])

            two_min = int(two_min_max[0])
            two_max = int(two_min_max[1])

            if ((one_min <= two_min and one_max >= two_max) 
                or (two_min <= one_min and two_max >= one_max)):
                count +=1

        return count

    def run_part_two(self, filename: str) -> None:
        count = 0     
        for line in self.get_lines(filename):
            pair = line.split(",")

            one_min_max = pair[0].split("-")
            two_min_max = pair[1].split("-")

            one_min = int(one_min_max[0])
            one_max = int(one_min_max[1])

            two_min = int(two_min_max[0])
            two_max = int(two_min_max[1])

            if not(one_max < two_min or two_max < one_min):
                count +=1

        return count
            
if __name__=="__main__":
    #elf = Sections().run_part_one("test.txt")
    #elf = Sections().run_part_two("test.txt")
    #elf = Sections().run_part_one("input.txt")
    elf = Sections().run_part_two("input.txt")
    print(elf)