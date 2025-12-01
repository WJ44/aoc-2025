"""Solution for day 1 of Advent of Code 2025."""

from typing import List

INPUT_FILE = "./puzzles/1/input.txt"


def parse_input(file_path=INPUT_FILE) -> List[int]:
    """Reads the input file and parses it into a usable format."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        puzzle_input = [(-1 if line[0] == "L" else 1) * int(line[1:]) for line in lines]
    return puzzle_input


def solve_part_one(rotations: List[int] = parse_input(INPUT_FILE)):
    """Solves part one of the day."""
    position = 50
    zero_count = 0
    for rotation in rotations:
        position = (position + rotation) % 100
        if position == 0:
            zero_count += 1
    return zero_count


def solve_part_two(rotations: List[int] = parse_input(INPUT_FILE)):
    """Solves part two of the day."""
    position = 50
    zero_count = 0
    for rotation in rotations:
        if rotation < 0:
            zero_count += ((100 - position) % 100 - rotation) // 100
        else:
            zero_count += (position + rotation) // 100
        position = (position + rotation) % 100
    return zero_count


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
