"""Solution for day 6 of Advent of Code 2025."""

from collections.abc import Callable
from functools import reduce
from operator import add, mul

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle6(Puzzle):
    """
    Solution for day 6 of Advent of Code 2025.
    """

    day = 6

    def parse_input(
        self, file
    ) -> list[tuple[Callable[[int, int], int], list[tuple[str]]]]:
        lines = file.readlines()
        operations = [add if c == "+" else mul for c in lines.pop().split()]
        columns = list(zip(*lines))
        problems = []
        i = 0
        problem: list[tuple[str]] = []
        for column in columns:
            if all(c in [" ", "\n"] for c in column):
                problems.append((operations[i], problem))
                i += 1
                problem = []
                continue
            problem.append(column)
        return problems

    def solve_part_one(
        self, puzzle_input: list[tuple[Callable[[int, int], int], list[tuple[str]]]]
    ) -> int:
        total = 0
        for operation, columns in puzzle_input:
            total += reduce(operation, [int("".join(row)) for row in zip(*columns)])
        return total

    def solve_part_two(
        self, puzzle_input: list[tuple[Callable[[int, int], int], list[tuple[str]]]]
    ) -> int:
        total = 0
        for operation, columns in puzzle_input:
            total += reduce(operation, [int("".join(row)) for row in columns])
        return total


if __name__ == "__main__":
    Puzzle6().print_solutions()
