class RockPaperScissors:
    _scores = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    _positions = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "X" : 0,
        "Y" : 1,
        "Z" : 2
    }

    _round_scores = [
        [3,6,0],
        [0,3,6],
        [6,0,3]
    ]

    _actions = [
        ["Z","X", "Y"],
        ["X","Y", "Z"],
        ["Y","Z", "X"]
    ]
    
    def round_score(self, left: str, right: str) -> int:
        return self._round_scores[self._positions.get(left)][self._positions.get(right)]

    def determine_action(self, left: str, right: str) -> str:
        return self._actions[self._positions.get(left)][self._positions.get(right)]
        
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