"""Solution for day 11 of Advent of Code 2025."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


def follow_path(device, path, puzzle_input, found):
    if device in found:
        found = found.union(path)
        return 1
    if path and device == "out":
        found = found.union(path)
        return 1
    paths = 0
    for next_device in puzzle_input[device]:
        new_path = path.copy()
        new_path.add(next_device)
        paths += follow_path(next_device, new_path, puzzle_input, found)
    return paths


class Puzzle11(Puzzle):
    """
    Solution for day 11 of Advent of Code 2025.
    """

    day = 11

    def parse_input(self, file) -> dict[str, list[str]]:
        puzzle_input = {}
        for line in file.readlines():
            split_colon = line.split(":")
            device = split_colon[0]
            outputs = split_colon[1].split()
            puzzle_input[device] = outputs
        return puzzle_input

    def solve_part_one(self, puzzle_input: dict[str, list[str]]) -> int:
        total = 0
        found = set()
        total += follow_path("you", {"you"}, puzzle_input, found)
        return total

    def solve_part_two(self, puzzle_input: dict[str, list[str]]) -> int:
        return 0


if __name__ == "__main__":
    Puzzle11().print_solutions()
