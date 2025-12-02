"""
Download input for a given day of Advent of Code 2025.
"""

import argparse
import os

import requests
from dotenv import load_dotenv


def download(day: int, overwrite: bool = False) -> None:
    """
    Download input for the given day and save it to a file.
    
    :param day: Day of the advent calendar.
    :type day: int
    :param overwrite: Whether to overwrite existing input file.
    :type overwrite: bool
    """

    url = f"https://adventofcode.com/2025/day/{day}/input"
    session_token = os.getenv("SESSION", "")
    response = requests.get(url, headers={"User-Agent": "github.com/WJ44/aoc-2025 by git@wjoosten.nl"},
                            cookies={"session": session_token},
                            timeout=10)
    response.raise_for_status()

    os.makedirs(f"puzzles/day{day:02d}", exist_ok=True)

    file_path = f"puzzles/day{day:02d}/input.txt"
    if not overwrite and os.path.exists(file_path):
        print(f"Input for day {day} already exists. Use --overwrite to replace it.")
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)


def main() -> None:
    """
    Main function to parse arguments and download input.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Day of the advent calendar")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing input file if it exists",
    )
    args = parser.parse_args()
    day = args.day
    overwrite = args.overwrite


    download(day, overwrite)


if __name__ == "__main__":
    load_dotenv()
    load_dotenv(".env.local", override=True)

    main()
