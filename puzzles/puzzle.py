"""Abstraction for Advent of Code puzzles."""

import unittest
from abc import ABC, abstractmethod
from contextlib import contextmanager
from io import TextIOWrapper
from pathlib import Path
from time import time
from typing import Any, Optional


class Puzzle(ABC):
    """
    Abstraction for Advent of Code puzzles.
    """

    puzzles: dict[int, "Puzzle"] = {}
    day: int

    @classmethod
    def register_puzzle(cls, puzzle: "Puzzle"):
        """
        Register a puzzle.

        Args:
            puzzle: The puzzle instance to register.
        """
        if puzzle.day > 0:
            cls.puzzles[puzzle.day] = puzzle

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.register_puzzle(cls())

    @contextmanager
    def open_input_file(
        self, file_name: Optional[str] = None, file_path: Optional[Path] = None
    ):
        """
        Context manager to open the input file.

        Args:
            file_name: The name of the input file. Defaults to "input.txt".
            file_path: The path to the input file. Defaults to "./puzzles/{day}/input.txt".

        Raises:
            ValueError: If both file_name and file_path are provided.
        """
        if file_name and file_path:
            raise ValueError("Specify either file_name or file_path, not both.")

        if file_name is None:
            file_name = "input.txt"

        if file_path is None:
            file_path = Path(f"./puzzles/day{self.day:02d}/{file_name}")

        with open(file_path, "r", encoding="utf-8") as file:
            yield file

    @abstractmethod
    def parse_input(self, file: TextIOWrapper) -> Any:
        """
        Parse the input file.

        Args:
            file: The input file object.
        """

    @abstractmethod
    def solve_part_one(self, puzzle_input: Any) -> int:
        """
        Solve part one of the day.

        Args:
            puzzle_input: The parsed input for the puzzle.
        """

    @abstractmethod
    def solve_part_two(self, puzzle_input: Any) -> int:
        """
        Solve part two of the day.

        Args:
            puzzle_input: The parsed input for the puzzle.
        """

    def print_solutions(
        self, file_name: Optional[str] = None, file_path: Optional[Path] = None
    ) -> None:
        """
        Print the solutions for both parts of the puzzle.

        Args:
            file_name: The name of the input file.
            file_path: The path to the input file.
        """
        with self.open_input_file(file_name=file_name, file_path=file_path) as file:
            start_time = time()
            puzzle_input = self.parse_input(file)
            parse_time = time()
            part_one = self.solve_part_one(puzzle_input)
            part_one_time = time()
            part_two = self.solve_part_two(puzzle_input)
            part_two_time = time()

            print(f"Day {self.day} solutions:")
            print(f"Solution to part one: \n {part_one}")
            print(f"Solution to part two: \n {part_two}")
            print(
                f"Parsing took: {parse_time - start_time}, part one took:"
                f"{part_one_time - parse_time} and part two took: {part_two_time - part_one_time}"
            )
            print("")


class BasePuzzleTest(unittest.TestCase):
    """
    Base test class for testing Advent of Code puzzles.
    """

    day: int
    expected_part_one: Optional[int] = None
    expected_part_two: Optional[int] = None
    test_file: str = "test1.txt"

    def setUp(self):
        """Set up the test by loading the puzzle and parsing test input."""
        if not hasattr(self, "day"):
            self.skipTest("Day not specified in test class")

        self.puzzle = Puzzle.puzzles[self.day]
        with self.puzzle.open_input_file(file_name=self.test_file) as file:
            self.puzzle_input = self.puzzle.parse_input(file)

    def test_part_one(self):
        """Test part one solution with example input."""
        if self.expected_part_one is None:
            self.skipTest("Expected result for part one not set")

        result = self.puzzle.solve_part_one(self.puzzle_input)
        self.assertEqual(result, self.expected_part_one)

    def test_part_two(self):
        """Test part two solution with example input."""
        if self.expected_part_two is None:
            self.skipTest("Expected result for part two not set")

        result = self.puzzle.solve_part_two(self.puzzle_input)
        self.assertEqual(result, self.expected_part_two)
