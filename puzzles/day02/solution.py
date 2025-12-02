"""Solution for day 2 of Advent of Code 2025."""

from math import ceil, floor, log

from puzzles.puzzle import Puzzle

DAY = 2

class Puzzle2(Puzzle):
    """Solution for day 2 of Advent of Code 2025."""
    day = DAY

    def parse_input(self, file) -> list[tuple[int, int]]:
        puzzle_input = [
            (int(range.split("-")[0]), int(range.split("-")[1]))
            for range in file.read().split(",")
        ]
        return puzzle_input

    def solve_part_one(self, puzzle_input: list[tuple[int, int]]) -> int:
        invalid_sum = 0
        for lower, upper in puzzle_input:
            for n in range(floor(log(lower, 10)), ceil(log(upper, 10))):
                if n % 2 == 0:
                    continue
                n = (n - 1) // 2
                for i in range(
                    max(pow(10, n), ceil(lower / (pow(10, n + 1) + 1))),
                    min(pow(10, n + 1) - 1, floor(upper / (pow(10, n + 1) + 1))) + 1,
                ):
                    invalid_sum += i * (pow(10, n + 1) + 1)
        return invalid_sum

    def solve_part_two(self, puzzle_input: list[tuple[int, int]]) -> int:
        invalid_sum = 0
        for lower, upper in puzzle_input:
            invalid_ids = set()
            for n in range(floor(log(lower, 10)), ceil(log(upper, 10))):
                factors = [list(range(i, n + 1, i + 1)) for i in range(0, n // 2 + 1)]
                for exponents in factors:
                    if len(exponents) < 2:
                        continue
                    if exponents[-1] != n:
                        continue
                    factor = sum(pow(10, exponent - exponents[0]) for exponent in exponents)
                    for i in range(
                        max(pow(10, exponents[0]), ceil(lower / factor)),
                        min(pow(10, exponents[0] + 1) - 1, floor(upper / factor)) + 1,
                    ):
                        invalid_ids.add(i * factor)
            invalid_sum += sum(invalid_ids)
        return invalid_sum


if __name__ == "__main__":
    Puzzle2().print_solutions()
