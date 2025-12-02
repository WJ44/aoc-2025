"""Puzzles package for Advent of Code 2025."""

import importlib
from pathlib import Path

from . import puzzle

puzzles_folder = Path(__file__).parent
for day_folder in puzzles_folder.glob('day*'):
    if day_folder.is_dir() and (day_folder / 'solution.py').exists():
        day = day_folder.name
        importlib.import_module(f'.{day}.solution', package='puzzles')


__all__ = ['puzzle']
