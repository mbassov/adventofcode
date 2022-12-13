from math import inf
import sys
sys.setrecursionlimit(3000)

class Sections:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        grid = self.populate(filename)
        start = self.find(grid, "S")
        end = self.find(grid, "E")

        grid[end[0]][end[1]] = "z"
        grid[start[0]][start[1]] = "a"

        #934
        results = self.run(grid, end, start)
        return results[end[0]][end[1]]

    
    def run(self, grid:list[list[str]], start: tuple[int], end: tuple[int]):
        results = []
        
        for i in range(len(grid)):
            inner2 = []
            for j in range(len(grid[0])):
                inner2.append(inf)
            results.append(inner2)
        self.run_rec(grid, results, 0, start, end)
        return results

    
    def run_rec(self, grid, results, count, start, end):
        if results[start[0]][start[1]] <= count:
            return

        results[start[0]][start[1]] = count

        if start[0] == end[0] and start[1]==end[1]:
            return

        #print (grid[start[0]][start[1]] + "(" + str(start[0]) + ", "+ str(start[1])+ ")") 
        
        # if current[0] == 23 and current[1] == 147:
        #     print (grid[current[0]][current[1]])

        moves = self.get_moves(grid, start)

        for move in moves:
            self.run_rec(grid, results, count + 1, move, end)
            # if move[0] == 27 and move[1] == 128:
                #     print (grid[move[0]][move[1]])
    
    
    def get_moves(self, grid:list[list[str]], pos: tuple[int]):
        moves = []
        current = ord(grid[pos[0]][pos[1]])
        if pos[0] + 1 < len(grid) and current - ord(grid[pos[0] + 1][pos[1]])  <= 1 :
            moves.append((pos[0] + 1, pos[1]))
        if pos[0] - 1 >= 0 and  current - ord(grid[pos[0] - 1][pos[1]]) <= 1 :
            moves.append((pos[0] - 1, pos[1]))
        if pos[1] + 1 < len(grid[0]) and current - ord(grid[pos[0]][pos[1] + 1]) <=1 :
            moves.append((pos[0], pos[1] + 1))
        if pos[1] - 1 >= 0 and current - ord(grid[pos[0]][pos[1] - 1])<= 1:
            moves.append((pos[0], pos[1] - 1))

        return moves

    def find(self, grid: list[list[str]], el:str) -> tuple[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == el:
                    return (i, j)
        
        raise Exception("not found")
    
    def populate(self, filename) -> list[list[str]]:
        result = []
        for line in self.get_lines(filename):
            result.append(list(line.strip()))
        
        return result

    def run_part_two(self, filename: str) -> None:
        grid = self.populate(filename)
        start = self.find(grid, "S")
        end = self.find(grid, "E")

        grid[end[0]][end[1]] = "z"
        grid[start[0]][start[1]] = "a"

        #934
        results = self.run(grid, end, start)
        min = inf
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'a':
                    if results[i][j] < min:
                        min = results[i][j]
        return min
            
if __name__=="__main__":
    #elf = Sections().run_part_one("/Users/michael/code/adventofcode/2022/day12/test.txt")
    #elf = Sections().run_part_two("test.txt")
    #elf = Sections().run_part_one("/Users/michael/code/adventofcode/2022/day12/input.txt")
    elf = Sections().run_part_two("input.txt")
    print(elf)