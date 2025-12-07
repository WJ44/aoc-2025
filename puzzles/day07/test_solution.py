"""Tests for Day 7 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay7(puzzle.BasePuzzleTest):
    """Test Day 7: Example test case."""

    day = 7
    expected_part_one = 21
    expected_part_two = 40


if __name__ == "__main__":
    import unittest

    unittest.main()
