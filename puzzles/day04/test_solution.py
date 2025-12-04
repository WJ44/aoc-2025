"""Tests for Day 4 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDayx(puzzle.BasePuzzleTest):
    """Test Day 4: Example test case."""

    day = 4
    expected_part_one = 13
    expected_part_two = 43


if __name__ == "__main__":
    import unittest

    unittest.main()
