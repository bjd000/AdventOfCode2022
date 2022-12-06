"""Part two inssturctions changes the understanding of the game.
Required changing the logic a bit from part one.
Right answered achieved.
"""

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    token_points: int = 0
    game_points: int = 0
    toal_points: int = 0


def main(file: str, player_1: str, player_2: str) -> None:

    with open(file, "r") as f:
        game_results: list[str] = f.read().split("\n")

    p1 = Player(player_1)
    p2 = Player(player_2)

    TOKEN_VALUES: dict[str, int] = {
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
    }

    GAME_MOVE: dict[str, str] = {
        "ROCKLOSE": "SCISSORS",
        "ROCKDRAW": "ROCK",
        "ROCKWIN": "PAPER",
        "PAPERLOSE": "ROCK",
        "PAPERDRAW": "PAPER",
        "PAPERWIN": "SCISSORS",
        "SCISSORSLOSE": "PAPER",
        "SCISSORSDRAW": "SCISSORS",
        "SCISSORSWIN": "ROCK",
    }

    OUTCOME_VALUES: dict[str, dict[str, int]] = {
        "LOSE": {"p1": 6, "p2": 0},
        "DRAW": {"p1": 3, "p2": 3},
        "WIN": {"p1": 0, "p2": 6},
    }

    DECODER_VALUES: dict[str, str] = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
    }

    for game in game_results:
        game_values: tuple = game.split(" ")

        # Decode game values
        game_values_decoded: tuple = (
            DECODER_VALUES[game_values[0]],  # ELF Token (rock, paper, scissors)
            DECODER_VALUES[game_values[1]],  # P2 Strategy (lose, draw, win)
        )
        print(f"{game_values}: {game_values_decoded}: ", end="")

        # Determine player two move to meet strategy
        p2_game_move: str = "".join(game_values_decoded)
        p2_move_token: str = GAME_MOVE[p2_game_move]

        # add the players token points
        p1.token_points += TOKEN_VALUES[game_values_decoded[0]]
        p2.token_points += TOKEN_VALUES[p2_move_token]
        print(
            f"[{p1.name} Token points={p1.token_points}, {p2.name} Token points={p2.token_points}], ",
            end="",
        )

        # game outcome
        p1.game_points += OUTCOME_VALUES[game_values_decoded[1]]["p1"]
        p2.game_points += OUTCOME_VALUES[game_values_decoded[1]]["p2"]
        print(f"Game points={p1.game_points}, {p2.game_points}")

    p1.toal_points = p1.token_points + p1.game_points
    p2.toal_points = p2.token_points + p2.game_points
    print(p1)
    print(p2)

    # Correct outcome
    # Player(name='Elf', token_points=5651, game_points=6588, toal_points=12239)
    # Player(name='Brian', token_points=4719, game_points=8412, toal_points=13131)


if __name__ == "__main__":
    main("input.txt", "Elf", "Brian")
