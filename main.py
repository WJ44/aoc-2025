"""
Main module to run all puzzles and print their solutions.
"""

from dotenv import load_dotenv

from downloader import download
from puzzles.puzzle import Puzzle


def main():
    """
    Run all puzzles, download input if necessary, and print their solutions.
    """
    for day, puzzle in Puzzle.puzzles.items():
        download(day)
        puzzle.print_solutions()

if __name__ == "__main__":
    load_dotenv()
    load_dotenv(".env.local", override=True)
    main()
