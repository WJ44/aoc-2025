"""Solution for day 9 of Advent of Code 2025."""

from itertools import combinations

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle9(Puzzle):
    """
    Solution for day 9 of Advent of Code 2025.
    """

    day = 9

    def parse_input(self, file) -> list[tuple[int, int]]:
        lines = [line.strip().split(",") for line in file.readlines()]
        puzzle_input = [(int(line[0]), int(line[1])) for line in lines]
        return puzzle_input

    def solve_part_one(self, puzzle_input: list[tuple[int, int]]) -> int:
        areas = {
            (abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)
            for ((x_1, y_1), (x_2, y_2)) in combinations(puzzle_input, 2)
        }
        return max(areas)

    def solve_part_two(self, puzzle_input: list[tuple[int, int]]) -> int:
        lines = []
        for i, tile_1 in enumerate(puzzle_input):
            tile_2 = puzzle_input[(i + 1) % len(puzzle_input)]
            direction = (
                -1 if tile_1[0] > tile_2[0] else 1 if tile_1[0] < tile_2[0] else 0,
                -1 if tile_1[1] > tile_2[1] else 1 if tile_1[1] < tile_2[1] else 0,
            )
            lines.append((tuple(sorted([tile_1, tile_2])), direction))
        areas = sorted(
            [
                ((abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1), ((x_1, y_1), (x_2, y_2)))
                for ((x_1, y_1), (x_2, y_2)) in combinations(puzzle_input, 2)
            ],
            reverse=True,
        )
        for area, (r1, r2) in areas:
            r1, r2 = (
                (min(r1[0], r2[0]), min(r1[1], r2[1])),
                (max(r1[0], r2[0]), max(r1[1], r2[1])),
            )
            for (a, b), direction in lines:
                if direction == (1, 0):
                    if r1[1] < a[1] <= r2[1] and a[0] < r2[0] and b[0] > r1[0]:
                        break
                if direction == (-1, 0):
                    if r1[1] <= a[1] < r2[1] and a[0] < r2[0] and b[0] > r1[0]:
                        break
            else:
                return area
        return 0


if __name__ == "__main__":
    Puzzle9().print_solutions()
