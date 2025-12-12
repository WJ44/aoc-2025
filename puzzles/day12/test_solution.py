"""Tests for Day 12 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay12(puzzle.BasePuzzleTest):
    """Test Day 12: Example test case."""

    day = 12
    expected_part_one = None
    expected_part_two = None


if __name__ == "__main__":
    import unittest

    unittest.main()
