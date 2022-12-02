class RockPaperScissors:
    _scores = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    # X --> rock
    # Y --> paper
    # Z --> scissors
    def round_score(self, left: str, right: str) -> int:
        if left == "A" and right == "X": # rock and rock
            return 3
        if left == "A" and right == "Y": # rock and paper
            return 6
        if left == "A" and right == "Z": # rock and scissors
            return 0
        if left == "B" and right == "X": # paper and rock
            return 0
        if left == "B" and right == "Y": # paper and paper
            return 3
        if left == "B" and right == "Z": # paper and scissors
            return 6
        if left == "C" and right == "X": # scissors and rock
            return 6
        if left == "C" and right == "Y": # scissors and paper
            return 0
        if left == "C" and right == "Z": # scissors and scissors
            return 3
        
        return None

    # X --> lose
    # Y --> draw
    # Z --> win
    def determine_action(self, left: str, right: str) -> str:
        if left == "A" and right == "X": # rock and lose
            return "Z" # scissors
        if left == "A" and right == "Y": # rock and draw
            return "X" # rock
        if left == "A" and right == "Z": # rock and win
            return "Y" # paper
        if left == "B" and right == "X": # paper and lose
            return "X"
        if left == "B" and right == "Y": # paper and draw
            return "Y"
        if left == "B" and right == "Z": # paper and win
            return "Z"
        if left == "C" and right == "X": # scissors and lose
            return "Y"
        if left == "C" and right == "Y": # scissors and draw
            return "Z"
        if left == "C" and right == "Z": # scissors and win
            return "X"
        
        return None
        
    def run(self, filename: str) -> None:
        text_file = open(filename, "r")
        lines = text_file.readlines()

        score = 0
        for line in lines:
            moves = line.split(" ")
            left = moves[0].rstrip()
            right = moves[1].rstrip()
            # solution for part 1
            #round_score = self.round_score(left, right) + self._scores.get(right)

            # solution for part 2
            action = self.determine_action(left, right)
            round_score = self.round_score(left, action) + self._scores.get(action)
            score += round_score
        
        return score
if __name__=="__main__":
    #elf = RockPaperScissors().run("test.txt")
    elf = RockPaperScissors().run("input.txt")
    print(elf)