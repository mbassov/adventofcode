
import sys

from max_heap import Max_Heap

class CalorieCounting:
    def run(self, filename: str) -> None:
        text_file = open(filename, "r")
        lines = text_file.readlines()

        calories = 0
        maxHeap = Max_Heap()

        for line in lines:
            if line == "\n":
                maxHeap.push(calories)
                calories = 0
            else: 
                calories += int(line)
        
        return maxHeap.pop() + maxHeap.pop() + maxHeap.pop()


if __name__=="__main__":
    #elf = CalorieCounting().run("test.txt")
    elf = CalorieCounting().run("input.txt")
    print(elf)
