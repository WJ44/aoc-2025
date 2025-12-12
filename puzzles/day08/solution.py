"""Solution for day 8 of Advent of Code 2025."""

from itertools import combinations
from typing import Any

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from puzzles.puzzle import Puzzle  # pylint: disable=wrong-import-position


class Puzzle8(Puzzle):
    """
    Solution for day 8 of Advent of Code 2025.
    """

    day = 8

    pairs_to_connect = 1000

    def parse_input(self, file) -> list[tuple[int, int, int]]:
        lines = [line.strip().split(",") for line in file.readlines()]
        puzzle_input = [(int(line[0]), int(line[1]), int(line[2])) for line in lines]
        return puzzle_input

    def solve_part_one(self, puzzle_input: Any) -> int:
        pairs = sorted(
            [
                (
                    (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2,
                    (x_1, y_1, z_1),
                    (x_2, y_2, z_2),
                )
                for (x_1, y_1, z_1), (x_2, y_2, z_2) in combinations(puzzle_input, 2)
            ],
            key=lambda pair: pair[0],
        )
        circuits: list[set[tuple[int, int, int]]] = []
        for _ in range(self.pairs_to_connect):
            _, box_1, box_2 = pairs.pop(0)
            new_circuit = {box_1, box_2}
            joined = []
            for circuit in circuits:
                if box_1 in circuit or box_2 in circuit:
                    joined.append(circuit)
                    new_circuit = new_circuit.union(circuit)
            for x in joined:
                circuits.remove(x)
            circuits.append(new_circuit)
        counts = sorted([len(circuit) for circuit in circuits], reverse=True)
        return counts[0] * counts[1] * counts[2]

    def solve_part_two(self, puzzle_input: list[tuple[int, int, int]]) -> int:
        pairs = sorted(
            [
                (
                    (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2,
                    (x_1, y_1, z_1),
                    (x_2, y_2, z_2),
                )
                for (x_1, y_1, z_1), (x_2, y_2, z_2) in combinations(puzzle_input, 2)
            ],
            key=lambda pair: pair[0],
        )
        circuits: list[set[tuple[int, int, int]]] = []
        while len(circuits) != 1 or sum(len(circuit) for circuit in circuits) < len(puzzle_input):
            _, box_1, box_2 = pairs.pop(0)
            new_circuit = {box_1, box_2}
            joined = []
            for circuit in circuits:
                if box_1 in circuit or box_2 in circuit:
                    joined.append(circuit)
                    new_circuit = new_circuit.union(circuit)
            for x in joined:
                circuits.remove(x)
            circuits.append(new_circuit)
        return box_1[0] * box_2[0]  # pyright: ignore[reportPossiblyUnboundVariable]


if __name__ == "__main__":
    Puzzle8().print_solutions()
