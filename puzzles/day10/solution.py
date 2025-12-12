"""Solution for day 10 of Advent of Code 2025."""

import re
from heapq import heappop, heappush

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle10(Puzzle):
    """
    Solution for day 10 of Advent of Code 2025.
    """

    day = 10

    def parse_input(self, file) -> list[tuple[list[bool], list[list[int]], list[int]]]:
        problems = []
        for line in file.readlines():
            m = re.fullmatch(r"\[([.#]+)\] ((?:\(\d+(?:,\d+)*\) )+)\{(\d+(?:,\d+)*)\}\n", line)
            if not m:
                raise ValueError("Line did not match pattern.")
            lights = [light == "#" for light in m.group(1)]
            buttons = [
                [int(light) for light in button[1:-1].split(",")] for button in m.group(2).split()
            ]
            joltages = [int(joltage) for joltage in m.group(3).split(",")]
            problems.append((lights, buttons, joltages))
        return problems

    def solve_part_one(
        self, puzzle_input: list[tuple[list[bool], list[list[int]], list[int]]]
    ) -> int:
        total = 0
        for lights, buttons, _ in puzzle_input:
            queue: list[tuple[int, list[bool]]] = []
            visited = {tuple([False] * len(lights))}
            heappush(queue, (0, [False] * len(lights)))
            found = False
            while not found:
                presses, current = heappop(queue)
                for button in buttons:
                    new_lights = [
                        not light if i in button else light for i, light in enumerate(current)
                    ]
                    if tuple(new_lights) in visited:
                        continue
                    visited.add(tuple(new_lights))
                    if lights == new_lights:
                        total += presses + 1
                        found = True
                        break
                    heappush(
                        queue,
                        (presses + 1, new_lights),
                    )
        return total

    def solve_part_two(
        self, puzzle_input: list[tuple[list[bool], list[list[int]], list[int]]]
    ) -> int:
        # TODO: too slow, find a better solution
        total = 0
        for _, buttons, joltages in puzzle_input:
            print(buttons, joltages)
            queue: list[tuple[int, list[int]]] = []
            visited = {tuple([0] * len(joltages))}
            heappush(queue, (0, [0] * len(joltages)))
            found = False
            while not found:
                presses, current = heappop(queue)
                for button in buttons:
                    new = current.copy()
                    for joltage in button:
                        new[joltage] += 1
                    if tuple(new) in visited:
                        continue
                    visited.add(tuple(new))
                    if any(new_joltage > joltage for new_joltage, joltage in zip(new, joltages)):
                        continue
                    if new == joltages:
                        total += presses + 1
                        found = True
                        break
                    heappush(
                        queue,
                        (presses + 1, new),
                    )
        return total


if __name__ == "__main__":
    Puzzle10().print_solutions()
