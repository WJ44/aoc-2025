"""Tests for Day 11 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay11Part1(puzzle.BasePuzzleTest):
    """Test Day 11: Example test case for part 1."""

    day = 11
    expected_part_one = 5
    expected_part_two = None


class TestDay11Part2(puzzle.BasePuzzleTest):
    """Test Day 11: Example test case for part 2."""

    day = 11
    expected_part_one = None
    expected_part_two = 2
    test_file = "test2.txt"


if __name__ == "__main__":
    import unittest

    unittest.main()
