import os.path

from adventofcode22.dataparser import parseFromFile


class Day1:

    def getInput(self):
        currDir = os.getcwd()
        inputFile = f"{currDir}/day1/input.txt"
        return parseFromFile(inputFile)

    def part1(self):
        data = self.getInput()
        maxCal = 0
        for vals in data:
            elfSum = sum(list(map(int, vals)))
            if elfSum > maxCal:
                maxCal = elfSum
        return maxCal

    def part2(self):
        input = self.getInput()
        data = [sum(list(map(int, vals))) for vals in input]
        data.sort(reverse=True)
        return sum(data[0:3])


if __name__ == "__main__":
    code = Day1()
    print(f"Part 1 solution: {code.part1()}")
    print(f"Part 2 solution: {code.part2()}")
