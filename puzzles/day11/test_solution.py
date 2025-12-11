"""Tests for Day 11 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay11(puzzle.BasePuzzleTest):
    """Test Day 11: Example test case."""

    day = 11
    expected_part_one = 5
    expected_part_two = None


if __name__ == "__main__":
    import unittest

    unittest.main()
