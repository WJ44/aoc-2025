"""Solution for day 3 of Advent of Code 2025."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle3(Puzzle):
    """
    Solution for day 3 of Advent of Code 2025.
    """

    day = 3

    def parse_input(self, file) -> list[list[int]]:
        puzzle_input = [[int(c) for c in line.strip()] for line in file.readlines()]
        return puzzle_input

    def solve_part_one(self, puzzle_input: list[list[int]]):
        total_joltage = 0
        for bank in puzzle_input:
            i, highest = max(enumerate(bank[:-1]), key=lambda x: (x[1], -x[0]))
            second = max(bank[i + 1 :])
            joltage = highest * 10 + second
            total_joltage += joltage
        return total_joltage

    def solve_part_two(self, puzzle_input: list[list[int]]):
        total_joltage = 0
        for bank in puzzle_input:
            joltage = 0
            pos = 0
            for n in range(12):
                i, highest = max(
                    enumerate(bank[pos : -(12 - n - 1) or None]),
                    key=lambda x: (x[1], -x[0]),
                )
                joltage += highest * pow(10, 12 - n - 1)
                pos += i + 1
            total_joltage += joltage
        return total_joltage


if __name__ == "__main__":
    Puzzle3().print_solutions()
