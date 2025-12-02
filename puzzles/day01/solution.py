"""Solution for day 1 of Advent of Code 2025."""

from puzzles.puzzle import Puzzle

DAY = 1

class Puzzle1(Puzzle):
    """
    Solution for day 1 of Advent of Code 2025.
    """
    day = DAY

    def parse_input(self, file) -> list[int]:
        lines = file.readlines()
        puzzle_input = [(-1 if line[0] == "L" else 1) * int(line[1:]) for line in lines]
        return puzzle_input

    def solve_part_one(self, puzzle_input: list[int]) -> int:
        position = 50
        zero_count = 0
        for rotation in puzzle_input:
            position = (position + rotation) % 100
            if position == 0:
                zero_count += 1
        return zero_count

    def solve_part_two(self, puzzle_input: list[int]) -> int:
        position = 50
        zero_count = 0
        for rotation in puzzle_input:
            if rotation < 0:
                zero_count += ((100 - position) % 100 - rotation) // 100
            else:
                zero_count += (position + rotation) // 100
            position = (position + rotation) % 100
        return zero_count

if __name__ == "__main__":
    Puzzle1().print_solutions()
