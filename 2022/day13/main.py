from functools import cmp_to_key
class Distress:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.read()

    def run_part_one(self, filename: str) -> None:
        idx = 0
        count = 0
        lines = self.get_lines(filename).split('\n\n')
        for line in lines:
            pair = line.split('\n')
            left = eval(pair[0])
            right = eval(pair[1])
            res = self.compare(left,right)
            idx += 1
            print(str(idx) + " : " + str(res))
            if (res > 0):
                count += idx

        return count

    def compare(self, left: str, right: str):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
            else: return 0
        if isinstance(left, int) and isinstance(right, list):
            return self.compare([left], right)
        if isinstance(right, int) and isinstance(left, list):
            return self.compare(left, [right])
        if isinstance(left, list) and isinstance(right, list):
            for i in range(0, min(len(left), len(right))):
                cmp = self.compare(left[0], right[0])
                if cmp == 1:
                    return 1
                elif cmp == -1:
                    return -1
                else: 
                    return self.compare(left[1:], right[1:])
        if len(left) < len(right):
            return 1
        if len(left) > len(right):
            return -1
        if len(left) == len(right):
            return 0
        raise Exception("missing case")

    def run_part_two(self, filename: str) -> None:
        count = 0
        data = [[[2]], [[6]]]
        lines = self.get_lines(filename).split('\n\n')
        for line in lines:
            pair = line.split('\n')
            left = eval(pair[0])
            right = eval(pair[1])
            data.append(left)
            data.append(right)

        data_sorted = sorted(data, key=cmp_to_key(self.compare), reverse=True)

        two_i = -1
        six_i = -1

        
        for i, v in enumerate(data_sorted):
            if v == [[2]]:
                two_i = i + 1

            if v == [[6]]:
                six_i = i + 1
        
        print(data_sorted)
        return two_i * six_i

        
if __name__=="__main__":
    #elf = Distress().run_part_one("/Users/michael/code/adventofcode/2022/day13/test.txt")
    #elf = Distress().run_part_two("/Users/michael/code/adventofcode/2022/day13/test.txt")
    #elf = Distress().run_part_one("/Users/michael/code/adventofcode/2022/day13/input.txt")
    elf = Distress().run_part_two("input.txt")
    print(elf)