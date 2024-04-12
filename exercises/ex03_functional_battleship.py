"""ex_03 A Structure Battleship."""

__author__ = "730477576"
import random


def input_guess(grid_size: int, user_choice: str) -> int:
    """Prompt user for guess."""
    assert user_choice == "row" or user_choice == "column"
    player_guess = int(input(f"Guess a {user_choice}: "))
    while player_guess > grid_size or player_guess <= 0:
        new_guess: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        player_guess = new_guess
    return player_guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, hit: bool) -> None:
    """Forms grid relating to user guess."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = ""
    row_ctr: int = 1
    column_ctr: int = 1
    row: str = ""
    if hit:
        result_box = RED_BOX
        while row_ctr <= grid_size:
            while column_ctr <= grid_size:
                if column_guess == column_ctr and row_guess == row_ctr:
                    row += result_box
                else:
                    row += BLUE_BOX
                column_ctr += 1
            print(row)
            row = ""
            row_ctr += 1
            column_ctr = 1
    else:
        result_box = WHITE_BOX
        while row_ctr <= grid_size:
            while column_ctr <= grid_size:
                if column_guess == column_ctr and row_guess == row_ctr:
                    row += result_box
                else:
                    row += BLUE_BOX
                column_ctr += 1
            print(row)
            row = ""
            row_ctr += 1
            column_ctr = 1


def correct_guess(secret_row: int, secret_column: int, user_row: int, user_column: int) -> bool:
    """Checks if user guess is correct."""
    if secret_column == user_column and secret_row == user_row:
        return (True)
    else:
        return (False)


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """The whole game."""
    num_turns: int = 5
    user_turn: int = 1
    while user_turn <= num_turns:
        print(f"=== Turn {user_turn}/{num_turns} ===")
        user_row: int = input_guess(grid_size, "row")
        user_column: int = input_guess(grid_size, "column")
        hit_or_not: bool = correct_guess(secret_row, secret_column, user_column, user_row)
        print_grid(grid_size, user_row, user_column, hit_or_not)
        if hit_or_not:
            print("Hit!")
            print(f"You won in {user_turn}/{num_turns} turns!")
            user_turn = num_turns + 1
        elif user_turn == num_turns and not hit_or_not:
            print("Miss!")
            print("X/5 - Better luck next time!")
            user_turn += 1
        else:
            print("Miss!")
            user_turn += 1
    

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))