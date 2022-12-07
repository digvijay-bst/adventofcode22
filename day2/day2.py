import os.path

from adventofcode22.dataparser import parseFromFileWithoutDoubleLine


class Day2:
    def getInput(self):
        currDir = os.getcwd()
        inputFile = f"{currDir}/input.txt"
        return parseFromFileWithoutDoubleLine(inputFile)

    def calculateScore(self, argList):
        winningCases = ['A Y', 'B Z', 'C X']
        drawCases = ['A X', 'B Y', 'C Z']
        vals = {'X': 1, 'Y': 2, 'Z': 3}
        output = []
        for arg in argList:
            sum = vals[arg[2]]
            if arg in winningCases:
                sum = sum + 6

            elif arg in drawCases:
                sum = sum + 3

            output.append(sum)
        return output

    def convertData(self, argList):
        output = []
        player1 = ['A', 'C', 'B']
        player2 = ['X', 'Z', 'Y']
        for arg in argList:
            if arg[2] == 'Z':
                output.append(f"{arg[0]} {player2[(player1.index(arg[0]) - 1) % 3]}")
            elif arg[2] == 'Y':
                output.append(f"{arg[0]} {player2[player1.index(arg[0])]}")
            else:
                output.append(f"{arg[0]} {player2[(player1.index(arg[0]) + 1) % 3]}")
        return output

    def part1(self):
        data = self.getInput()
        result = self.calculateScore(data)
        return sum(result)

    def part2(self):
        data = self.getInput()
        data = self.convertData(data)
        return sum(self.calculateScore(data))


if __name__ == "__main__":
    code = Day2()
    print(f"Part 1 solution: {code.part1()}")
    print(f"Part 2 solution: {code.part2()}")
