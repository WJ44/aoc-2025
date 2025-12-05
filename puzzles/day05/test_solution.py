"""Tests for Day 5 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay5(puzzle.BasePuzzleTest):
    """Test Day 5: Example test case."""

    day = 5
    expected_part_one = 3
    expected_part_two = 14


class TestDay5EdgeCases(puzzle.BasePuzzleTest):
    """Test Day 5: Test case focussing on edge cases."""

    day = 5
    expected_part_one = 19
    expected_part_two = 100
    test_file = "test2.txt"


if __name__ == "__main__":
    import unittest

    unittest.main()
