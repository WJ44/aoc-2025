"""Solution for day 4 of Advent of Code 2025."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


def get_accesible(puzzle_input: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Function to get the positions of accessible roles given a grid of rolls.

    Args:
        puzzle_input: A list of rolls
    """
    kernel = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    accesible = set()
    for y, x in puzzle_input:
        neighbours = set((y + offset_y, x + offset_x) for offset_y, offset_x in kernel)
        count_neighbours = len(neighbours.intersection(puzzle_input))
        if count_neighbours < 4:
            accesible.add((y, x))
    return accesible


class Puzzle4(Puzzle):
    """
    Solution for day 4 of Advent of Code 2025.
    """

    day = 4

    def parse_input(self, file) -> set[tuple[int, int]]:
        puzzle_input = set()
        grid = [[c == "@" for c in line.strip()] for line in file.readlines()]
        for y, line in enumerate(grid):
            for x, item in enumerate(line):
                if item:
                    puzzle_input.add((y, x))
        return puzzle_input

    def solve_part_one(self, puzzle_input: set[tuple[int, int]]) -> int:
        count_accesible = len(get_accesible(puzzle_input))
        return count_accesible

    def solve_part_two(self, puzzle_input: set[tuple[int, int]]) -> int:
        current = puzzle_input.copy()
        count_removed = 0
        while accesible := get_accesible(current):
            count_removed += len(accesible)
            current = current - accesible
        return count_removed


if __name__ == "__main__":
    Puzzle4().print_solutions()
