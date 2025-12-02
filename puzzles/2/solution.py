"""Solution for day 2 of Advent of Code 2025."""

from math import ceil, floor, log
from typing import List, Tuple

INPUT_FILE = "./puzzles/2/input.txt"


def parse_input(file_path=INPUT_FILE) -> List[Tuple[int, int]]:
    """Reads the input file and parses it into a usable format."""

    with open(file_path, "r", encoding="utf-8") as file:
        puzzle_input = [
            (int(range.split("-")[0]), int(range.split("-")[1]))
            for range in file.read().split(",")
        ]
    return puzzle_input


def solve_part_one(
    puzzle_input: List[Tuple[int, int]] = parse_input(INPUT_FILE),
) -> int:
    """Solves part one of the day."""
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


def solve_part_two(puzzle_input: List[Tuple[int, int]] = parse_input(INPUT_FILE)):
    """Solves part two of the day."""
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


def main():
    """Prints the solutions of the day."""
    puzzle_input = parse_input(INPUT_FILE)
    part_one = solve_part_one(puzzle_input)
    part_two = solve_part_two(puzzle_input)

    print(f"Solution to part one: \n {part_one}")
    print("\n")
    print(f"Solution to part two: \n {part_two}")


if __name__ == "__main__":
    main()
