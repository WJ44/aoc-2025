"""Tests for Day 10 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay10(puzzle.BasePuzzleTest):
    """Test Day 10: Example test case."""

    day = 10
    expected_part_one = 7
    expected_part_two = 33


if __name__ == "__main__":
    import unittest

    unittest.main()
