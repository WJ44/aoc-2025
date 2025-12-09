"""Tests for Day 9 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay9(puzzle.BasePuzzleTest):
    """Test Day 9: Example test case."""

    day = 9
    expected_part_one = 50
    expected_part_two = 24


class TestDay9Variation1(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 30
    test_file = "test2.txt"


class TestDay9Variation2(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 30
    test_file = "test3.txt"


class TestDay9Variation3(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 30
    test_file = "test4.txt"


class TestDay9Variation4(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 30
    test_file = "test5.txt"


class TestDay9Variation5(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 49
    test_file = "test6.txt"


class TestDay9Variation6(puzzle.BasePuzzleTest):
    """Test Day 9: Other test case."""

    day = 9
    expected_part_two = 16
    test_file = "test7.txt"


if __name__ == "__main__":
    import unittest

    unittest.main()
