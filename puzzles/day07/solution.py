"""Solution for day 7 of Advent of Code 2025."""

from collections import defaultdict

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle7(Puzzle):
    """
    Solution for day 7 of Advent of Code 2025.
    """

    day = 7

    def parse_input(self, file) -> tuple[tuple[int, int], set[tuple[int, int]], tuple[int, int]]:
        splitters = set()
        start = (0, 0)
        bounds = (0, 0)
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                bounds  = (y, x)
                if c == "^":
                    splitters.add((y, x))
                    continue
                elif c == "S":
                    start = (y, x)
        return start, splitters, bounds

    def solve_part_one(self,
                       puzzle_input: tuple[tuple[int, int], set[tuple[int, int]], tuple[int, int]])\
                        -> int:
        start, splitters, bounds = puzzle_input
        splitters = splitters.copy()
        y, x = start
        max_y, max_x = bounds
        beams = {x}
        split_count = 0
        while y < max_y:
            new_beams = set()
            y += 1
            for x in beams:
                if (y, x) in splitters:
                    split_count += 1
                    splitters.remove((y, x))
                    if x >= 0:
                        new_beams.add(x - 1)
                    if x <= max_x:
                        new_beams.add(x + 1)
                else:
                    new_beams.add(x)
            beams = new_beams
        return split_count

    def solve_part_two(self,
                       puzzle_input: tuple[tuple[int, int], set[tuple[int, int]], tuple[int, int]])\
                        -> int:
        start, splitters, bounds = puzzle_input
        splitters = splitters.copy()
        y, x = start
        max_y, max_x = bounds
        beams = {x: 1}
        while y < max_y:
            new_beams: defaultdict[int, int] = defaultdict(int)
            y += 1
            for x, count in beams.items():
                if (y, x) in splitters:
                    if x >= 0:
                        new_beams[x - 1] += count
                    if x <= max_x:
                        new_beams[x + 1] += count
                else:
                    new_beams[x] += count
            beams = new_beams
        return sum(beams.values())


if __name__ == "__main__":
    Puzzle7().print_solutions()
