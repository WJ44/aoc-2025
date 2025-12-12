"""Solution for day 12 of Advent of Code 2025."""

import re

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle12(Puzzle):
    """
    Solution for day 12 of Advent of Code 2025.
    """

    day = 12

    def parse_input(self, file) -> list[tuple[tuple[int, int], tuple[int, ...]]]:
        m = re.fullmatch(r"(?s:.)*?((?:\d+x\d+:(?: \d+)+\n)+)", file.read())
        if not m:
            raise ValueError("File did not match pattern.")
        regions = [region.split() for region in m.group(1).split("\n")[:-1]]
        puzzle_input = [
            (
                (int((sides := region[0][:-1].split("x"))[0]), int(sides[1])),
                tuple(int(count) for count in region[1:]),
            )
            for region in regions
        ]
        return puzzle_input

    def solve_part_one(
        self,
        puzzle_input: list[tuple[tuple[int, int], tuple[int, ...]]],
    ) -> int:
        total = 0
        for (width, height), counts in puzzle_input:
            area = width * height
            if area >= sum(counts) * 9:
                total += 1
        return total

    def solve_part_two(
        self,
        puzzle_input: list[tuple[tuple[int, int], tuple[int, ...]]],
    ) -> int:
        return 0


if __name__ == "__main__":
    Puzzle12().print_solutions()
