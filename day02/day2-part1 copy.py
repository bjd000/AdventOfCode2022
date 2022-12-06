""" Part one effort.  It worked for the Part one answer.
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
    GAME_OUTCOMES: dict[str, dict[str, str]] = {
        "ROCKROCK": {"p1": "DRAW", "p2": "DRAW"},
        "ROCKPAPER": {"p1": "LOSE", "p2": "WIN"},
        "ROCKSCISSORS": {"p1": "WIN", "p2": "LOSE"},
        "PAPERROCK": {"p1": "WIN", "p2": "LOSE"},
        "PAPERPAPER": {"p1": "DRAW", "p2": "DRAW"},
        "PAPERSCISSORS": {"p1": "LOSE", "p2": "WIN"},
        "SCISSORSROCK": {"p1": "LOSE", "p2": "WIN"},
        "SCISSORSPAPER": {"p1": "WIN", "p2": "LOSE"},
        "SCISSORSSCISSORS": {"p1": "DRAW", "p2": "DRAW"},
    }
    OUTCOME_VALUES: dict[str, int] = {
        "LOSE": 0,
        "DRAW": 3,
        "WIN": 6,
    }

    DECODER_VALUES: dict[str, str] = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS",
    }

    for game in game_results:
        game_tokens: tuple = game.split(" ")

        game_tokens_decoded: tuple = (
            DECODER_VALUES[game_tokens[0]],
            DECODER_VALUES[game_tokens[1]],
        )
        # print(f"{game_tokens}: {game_tokens_decoded}: ", end="")

        # add the players token points
        p1.token_points += TOKEN_VALUES[game_tokens_decoded[0]]
        p2.token_points += TOKEN_VALUES[game_tokens_decoded[1]]
        # print(f"{p1.name} Token points={p1.token_points}, ", end="")

        # game outcome
        game_outcome: str = "".join(game_tokens_decoded)
        # print(game_outcome)
        p1.game_points += OUTCOME_VALUES[GAME_OUTCOMES[game_outcome]["p1"]]
        p2.game_points += OUTCOME_VALUES[GAME_OUTCOMES[game_outcome]["p2"]]
        # print(f"Game points={p1.game_points}")

    p1.toal_points = p1.token_points + p1.game_points
    p2.toal_points = p2.token_points + p2.game_points
    print(p1)
    print(p2)


if __name__ == "__main__":
    main("input.txt", "Elf", "Brian")
