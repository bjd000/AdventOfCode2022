"""Same outcome as the first pass on Day 2 Part 2.  Just organized into functions.
"""

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    token_points: int = 0
    game_points: int = 0
    toal_points: int = 0


def decode_game_input(game_values: tuple) -> tuple:

    DECODER_VALUES: dict[str, str] = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
    }

    decoded_values: tuple = (
        DECODER_VALUES[game_values[0]],  # ELF Token (rock, paper, scissors)
        DECODER_VALUES[game_values[1]],  # P2 Strategy (lose, draw, win)
    )

    return decoded_values


def determine_game_move(game_values_decoded: tuple) -> str:

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

    p2_game_move: str = "".join(game_values_decoded)
    return GAME_MOVE[p2_game_move]


def tally_token_points(p1: Player, p2: Player, p1_token: str, p2_token: str) -> None:

    TOKEN_VALUES: dict[str, int] = {
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
    }

    p1.token_points += TOKEN_VALUES[p1_token]
    p2.token_points += TOKEN_VALUES[p2_token]
    return


def tally_game_points(p1: Player, p2: Player, game_outcome) -> None:

    OUTCOME_VALUES: dict[str, dict[str, int]] = {
        "LOSE": {"p1": 6, "p2": 0},
        "DRAW": {"p1": 3, "p2": 3},
        "WIN": {"p1": 0, "p2": 6},
    }

    p1.game_points += OUTCOME_VALUES[game_outcome]["p1"]
    p2.game_points += OUTCOME_VALUES[game_outcome]["p2"]
    return


def tally_total_points(p1: Player, p2: Player) -> None:
    p1.toal_points = p1.token_points + p1.game_points
    p2.toal_points = p2.token_points + p2.game_points
    return


def main(file: str, player_1: str, player_2: str) -> None:

    with open(file, "r") as f:
        game_results: list[str] = f.read().split("\n")

    p1 = Player(player_1)  # Elf
    p2 = Player(player_2)  # Me

    for game in game_results:
        game_values: tuple = game.split(" ")

        # Decode game values (Elf's Token, Expected Game Outcome)
        game_values_decoded: tuple = decode_game_input(game_values)
        print(f"{game_values}: {game_values_decoded}: ", end="")

        # Determine player two move to meet desired gaem outcome
        p2_move_token: str = determine_game_move(game_values_decoded)

        # Tally the players token, game and total points
        tally_token_points(p1, p2, game_values_decoded[0], p2_move_token)
        tally_game_points(p1, p2, game_values_decoded[1])
        tally_total_points(p1, p2)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main("input.txt", "Elf", "Brian")
