"""Tests for Day 8 solution."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from puzzles import puzzle  # pylint: disable=wrong-import-position


class TestDay8(puzzle.BasePuzzleTest):
    """Test Day 8: Example test case."""

    day = 8
    expected_part_one = 40
    expected_part_two = 25272

    def setUp(self):
        super().setUp()
        self.puzzle.pairs_to_connect = 10


if __name__ == "__main__":
    import unittest

    unittest.main()
