class TreeHouse:
    field = []

    def get_lines(self, filename: str) -> list[list[int]]:
        text_file = open(filename, "r")
        row = 0
        for line in text_file.readlines():
            self.field.insert(row, list(line.rstrip()))
            row +=1 

    def run_part_one(self, filename: str) -> None:
        self.get_lines(filename)
        
        
        width = len(self.field)
        height = len(self.field[0])

        perimiter = (width * 2) + ((height * 2) - 4)
        count = 0
        for i in range(1, width-1):
            for j in range(1, height-1):
                if self.look(i,j,int(self.field[i][j])):
                    print(self.field[i][j])
                    count +=1

        return count + perimiter

    def look(self, i: int, j: int, me: int) -> bool:
        return  self.left(i,j,me) or self.right(i,j,me) or self.up(i,j,me) or self.down(i,j,me)
        
    def left(self, i: int, j: int, me: int) -> bool:
        for col in range(0,j):
            v = int(self.field[i][col])
            if me <= v:
                return False
        return True
    
    def right(self, i: int, j: int, me: int) -> int:
        for col in range(j+1, len(self.field)):
            v = int(self.field[i][col])
            if me <= v:
                return False
        return True

    def up(self, i: int, j: int, me: int) -> int:
        for row in range(0, i):
            v = int(self.field[row][j])
            if me <= v:
                return False
        return True

    def down(self, i: int, j: int, me: int) -> int:
        for row in range(i+1, len(self.field[0])):
            v = int(self.field[row][j])
            if me <= v:
                return False
        return True
    
    def look2(self, i: int, j: int, me: int) -> bool:
        return self.left2(i,j,me) * self.right2(i,j,me) * self.up2(i,j,me) * self.down2(i,j,me)
        
    def left2(self, i: int, j: int, me: int) -> bool:
        count = 0
        for col in reversed(range(0,j)):
            v = int(self.field[i][col])
            if me <= v:
                count +=1
                return count
            count +=1
        return count
    
    def right2(self, i: int, j: int, me: int) -> int:
        count = 0
        for col in range(j+1, len(self.field)):
            v = int(self.field[i][col])
            if me <= v:
                count +=1
                return count
            count +=1
        return count

    def up2(self, i: int, j: int, me: int) -> int:
        count = 0
        for row in reversed(range(0, i)):
            v = int(self.field[row][j])
            if me <= v:
                count +=1
                return count
            count +=1
        return count

    def down2(self, i: int, j: int, me: int) -> int:
        count = 0
        for row in range(i+1, len(self.field[0])):
            v = int(self.field[row][j])
            if me <= v:
                count +=1
                return count
            count +=1
        return count

    def run_part_two(self, filename: str) -> None:
        self.get_lines(filename)
        
        
        width = len(self.field)
        height = len(self.field[0])

        max = 0
        for i in range(1, width-1):
            for j in range(1, height-1):
                current = self.look2(i,j,int(self.field[i][j]))
                if max < current:
                    max = current

        return max 
            
if __name__=="__main__":
    #elf = TreeHouse().run_part_one("/Users/michael/code/adventofcode/2022/day8/test.txt")
    #elf = TreeHouse().run_part_two("/Users/michael/code/adventofcode/2022/day8/test.txt")
    #elf = TreeHouse().run_part_one("/Users/michael/code/adventofcode/2022/day8/input.txt")
    elf = TreeHouse().run_part_two("/Users/michael/code/adventofcode/2022/day8/input.txt")
    print(elf)