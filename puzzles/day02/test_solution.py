"""Tests for Day 2 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay2(puzzle.BasePuzzleTest):
    """Test Day 2: Example test case."""

    day = 2
    expected_part_one = 1227775554
    expected_part_two = 4174379265


if __name__ == "__main__":
    import unittest

    unittest.main()
