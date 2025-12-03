"""Tests for Day 1 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay3(puzzle.BasePuzzleTest):
    """Test Day 3: Example test case."""

    day = 3
    expected_part_one = 357
    expected_part_two = 3121910778619


if __name__ == "__main__":
    import unittest

    unittest.main()
