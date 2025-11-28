"""Download input for a given day of Advent of Code 2025."""

import argparse
import os

import requests
from dotenv import load_dotenv


def download(day: int) -> None:
    """Download input for the given day and save it to a file."""

    url = f"https://adventofcode.com/2025/day/{day}/input"
    session_token = os.getenv("SESSION", "")
    response = requests.get(url, cookies={"session": session_token}, timeout=10)
    response.raise_for_status()

    os.makedirs(f"puzzles/{day}", exist_ok=True)

    with open(f"puzzles/{day}/input.txt", "w", encoding="utf-8") as f:
        f.write(response.text)


def main() -> None:
    """Main function to parse arguments and download input."""

    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Day of the advent calendar")
    args = parser.parse_args()
    day = args.day

    load_dotenv()
    load_dotenv(".env.local", override=True)

    download(day)


if __name__ == "__main__":
    main()
