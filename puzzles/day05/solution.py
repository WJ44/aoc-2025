"""Solution for day 5 of Advent of Code 2025."""

from bisect import bisect_right
from typing import Any

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle5(Puzzle):
    """
    Solution for day 5 of Advent of Code 2025.
    """

    day = 5

    def parse_input(self, file) -> tuple[list[tuple[int, int]], list[int]]:
        ranges, ingredients = file.read().split("\n\n")
        ranges = [range.split("-") for range in ranges.split("\n")]
        ranges = [(int(range[0]), int(range[1])) for range in ranges]
        ingredients = [
            int(ingredient) for ingredient in ingredients.strip().split("\n")
        ]
        ranges = sorted(ranges)
        return ranges, ingredients

    def solve_part_one(
        self, puzzle_input: tuple[list[tuple[int, int]], list[int]]
    ) -> int:
        ranges, ingredients = puzzle_input
        count = 0
        for ingredient in ingredients:
            i = bisect_right(ranges, (ingredient, float("inf")))
            while i > 0:
                i -= 1
                _, right = ranges[i]
                if right >= ingredient:
                    count += 1
                    break
        return count

    def solve_part_two(self, puzzle_input: Any) -> int:
        ranges, _ = puzzle_input
        count = 0
        previous_left, previous_right = None, None
        for left, right in ranges:
            if previous_right:
                if right <= previous_left:
                    continue
                if left <= previous_right:
                    left = previous_right + 1
                    if left > right:
                        continue
            count += right - left + 1
            previous_left = left
            previous_right = right
        return count


if __name__ == "__main__":
    Puzzle5().print_solutions()
