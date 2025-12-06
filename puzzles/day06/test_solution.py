"""Tests for Day 6 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay6(puzzle.BasePuzzleTest):
    """Test Day 6: Example test case."""

    day = 6
    expected_part_one = 4277556
    expected_part_two = 3263827


if __name__ == "__main__":
    import unittest

    unittest.main()
