from enum import Enum

class Position:
    def __init__(self,x: int, y:int):
        self.x = x
        self.y = y
    
    def coordinate(self) -> tuple[int,int]:
        return (self.x, self.y)

    def move(self, dir: str, step:int) -> None:
        if dir == 'L': self.left(step)
        elif dir == 'R': self.right(step)
        elif dir == 'U': self.up(step)
        elif dir == 'D': self.down(step)
        else: raise Exception("Wrong move")
    
    def move_diag(self, dir: str, step: int) -> None:
        if dir == 'NW': 
            self.left(step) 
            self.up(step)
        elif dir == 'NE': 
            self.right(step)
            self.up(step)
        elif dir ==  'SW': 
            self.down(step) 
            self.left(step)
        elif dir == 'SE': 
            self.down(step) 
            self.right(step)
        else: raise Exception("Wrong diag")
    
    def left(self, step:int):
        self.x = self.x-step

    def right(self, step:int):
        self.x = self.x+step

    def up(self, step:int):
        self.y = self.y+step
    
    def down(self, step:int):
        self.y = self.y-step

    def same_x(self, other: 'Position') -> bool:
        return self.x == other.x
    
    def same_y(self, other: 'Position') -> bool:
        return self.y == other.y

    def isTouching(self, other: 'Position') -> bool:
        return ((self.x == other.x and self.y == other.y) or
        (abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1) or 
        (abs(self.x - other.x) == 1 and self.y == other.y) or 
        (abs(self.y - other.y) == 1 and self.x == other.x)) 

    def get_obj_class(self) -> type:
        return self.o.__class__

    def str(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Bridge:
    def get_lines(self, filename: str) -> list:
        text_file = open(filename, "r")
        return text_file.readlines()

    def run_part_one(self, filename: str) -> None:
        return self.run(filename, 2)

    def run_part_two(self, filename: str) -> None:
        return self.run(filename, 10)

    def run(self, filename:str, rope_len:int) -> int:
        tail_seen = {}
        tail_seen[Position(0,0).coordinate()] = 1
        rope = []
        for k in range(rope_len):
            rope.append(Position(0,0))
        for move_head in self.get_lines(filename):
            direction, steps = move_head.rstrip().split(" ")
            for j in range(int(steps)):
                rope[0].move(direction, 1)
                for i in range(len(rope) - 1):
                    self.move_tail(rope, i, direction, tail_seen)
                    #print(rope[0].str() + " : " + rope[len(rope)-1].str())
                tail = rope[len(rope)-1]
                #self.print_rope(rope)
                #print(tail.str())
                # if tail.x == 2 and tail.y == 2:
                #     print(tail.str())
                tail_seen[tail.coordinate()] = 1

        return len(tail_seen.keys())
    def print_rope(self,rope: list['Position']):
        res = ""
        for i in range(len(rope)):
            res = res + rope[i].str() + ", "
        print(res)

    def move_tail(self, rope: list['Position'], position: int, direction: str, seen: list[tuple[int,int]]) -> None :
        head = rope[position]
        tail = rope[position+1]
        if head.isTouching(tail): 
            return
        if head.same_x(tail):
            if head.y > tail.y:
                tail.y = tail.y + 1
            else:
                tail.y = tail.y -1
                
        elif head.same_y(tail):
            if head.x > tail.x:
                tail.x = tail.x + 1
            else:
                tail.x = tail.x - 1 
            
        # move diagonal
        elif head.x > tail.x and head.y > tail.y:
            tail.move_diag("NE", 1)
        elif head.x > tail.x and head.y < tail.y:
            tail.move_diag("SE", 1)
        elif head.x < tail.x and head.y < tail.y:
            tail.move_diag("SW", 1)
        elif head.x < tail.x and head.y > tail.y:
            tail.move_diag("NW", 1)
        else:
            raise Exception("diagonal logic broken")
        
        return 


if __name__=="__main__":
    #elf = Bridge().run_part_one("/Users/michael/code/adventofcode/2022/day9/test.txt")
    #elf = Bridge().run_part_two("/Users/michael/code/adventofcode/2022/day9/test2.txt")
    #elf = Bridge().run_part_one("/Users/michael/code/adventofcode/2022/day9/input.txt")
    #elf = Bridge().run_part_two("/Users/michael/code/adventofcode/2022/day9/input.txt")
    print(elf)