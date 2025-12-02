"""Tests for Day 1 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay1(puzzle.BasePuzzleTest):
    """Test Day 1: Example test case."""
    day = 1
    expected_part_one = 3
    expected_part_two = 6

if __name__ == '__main__':
    import unittest
    unittest.main()
