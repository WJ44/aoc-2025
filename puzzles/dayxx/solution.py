"""Solution for day x of Advent of Code 2025."""

from typing import Any

if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))



from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class PuzzleX(Puzzle):
    """
    Solution for day x of Advent of Code 2025.
    """
    day = 0

    def parse_input(self, file) -> Any:
        puzzle_input = None
        return puzzle_input

    def solve_part_one(self, puzzle_input: Any) -> int:
        return 0

    def solve_part_two(self, puzzle_input: Any) -> int:
        return 0

if __name__ == "__main__":
    PuzzleX().print_solutions()
