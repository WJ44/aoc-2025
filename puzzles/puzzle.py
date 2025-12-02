"""Abstraction for Advent of Code puzzles."""

from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import Optional


class Puzzle(ABC):
    """
    Abstraction for Advent of Code puzzles.
    """

    puzzles: dict[int, 'Puzzle'] = {}
    day: int

    @classmethod
    def register_puzzle(cls, puzzle: 'Puzzle'):
        """
        Register a puzzle.
        
        :param puzzle: The puzzle instance to register.
        """
        cls.puzzles[puzzle.day] = puzzle

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.register_puzzle(cls())

    @contextmanager
    def open_input_file(self, file_name: Optional[str] = None, file_path: Optional[Path] = None):
        """
        Context manager to open the input file.
        
        :param file_name: The name of the input file. Defaults to "input.txt".
        :param file_path: The path to the input file. Defaults to "./puzzles/{day}/input.txt".
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
    def parse_input(self, file):
        """
        Parse the input file.
        
        :param file: The input file object.
        """

    @abstractmethod
    def solve_part_one(self, puzzle_input) -> int:
        """
        Solve part one of the day.
        
        :param puzzle_input: The parsed input for the puzzle.
        """

    @abstractmethod
    def solve_part_two(self, puzzle_input) -> int:
        """
        Solve part two of the day.
        
        :param puzzle_input: The parsed input for the puzzle.
        """

    def print_solutions(self, file_name: Optional[str] = None,
                        file_path: Optional[Path] = None) -> None:
        """
        Print the solutions for both parts of the puzzle.
        
        :param file_name: The name of the input file.
        :param file_path: The path to the input file.
        """
        with self.open_input_file(file_name=file_name, file_path=file_path) as file:
            puzzle_input = self.parse_input(file)
            part_one = self.solve_part_one(puzzle_input)
            part_two = self.solve_part_two(puzzle_input)

            print(f"Day {self.day} solutions:")
            print(f"Solution to part one: \n {part_one}")
            print(f"Solution to part two: \n {part_two}")
            print("")
