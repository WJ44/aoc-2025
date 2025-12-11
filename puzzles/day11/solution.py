"""Solution for day 11 of Advent of Code 2025."""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


def find_paths(
    device: str,
    goal: str,
    puzzle_input: dict[str, list[str]],
    visited: dict[str, int] | None = None,
    path: set[str] | None = None,
):
    """
    Finds the number of paths from device to goal.

    Args:
        device: The current device.
        goal: The device to find
        puzzle_input: The mapping of devices to outputs.
        found: The devices we have already found and how often they lead to the goal.
        path: The path so far.
    """
    if visited is None:
        visited = {}
    if path is None:
        path = set()
    if device in visited:
        for i in path:
            visited[i] += visited[device]
        return 0
    path.add(device)
    visited[device] = 0
    if device == goal:
        for i in path:
            visited[i] += 1
        return 0
    if device == "out":
        return 0
    for next_device in puzzle_input[device]:
        find_paths(next_device, goal, puzzle_input, visited, path.copy())
    return visited[device]


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
        return find_paths("you", "out", puzzle_input)

    def solve_part_two(self, puzzle_input: dict[str, list[str]]) -> int:
        return find_paths("svr", "dac", puzzle_input) * find_paths(
            "dac", "fft", puzzle_input
        ) * find_paths("fft", "out", puzzle_input) + find_paths(
            "svr", "fft", puzzle_input
        ) * find_paths(
            "fft", "dac", puzzle_input
        ) * find_paths(
            "dac", "out", puzzle_input
        )


if __name__ == "__main__":
    Puzzle11().print_solutions()
