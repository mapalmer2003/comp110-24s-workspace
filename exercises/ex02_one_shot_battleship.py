"""Ex01 - One shot battleship."""

__author__ = "730477576"

grid: int = 4
secret_column: int = 2
secret_row: int = 3
row_ctr: int = 1
column_ctr: int = 1
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result_box: str = ""
row: str = ""
Player_1_row: int = int(input("Guess a row: "))

while Player_1_row > grid or Player_1_row < 1:
    new_guess_row: int = int(input(f"The grid is only {grid} by {grid}. Try again: "))
    Player_1_row = new_guess_row
Player_1_column: int = int(input("Guess a column: "))
while Player_1_column > grid or Player_1_column < 1:
    new_guess_column: int = int(input(f"The grid is only {grid} by {grid}. Try again: "))
    Player_1_column = new_guess_column

if Player_1_column == secret_column and Player_1_row == secret_row:
    result_box = RED_BOX
    while row_ctr <= grid:
        while column_ctr <= grid:
            if Player_1_column == column_ctr and Player_1_row == row_ctr:
                row += result_box
            else:
                row += BLUE_BOX
            column_ctr += 1
        print(row)
        row = ""
        row_ctr += 1
        column_ctr = 1
    print("Hit!")

else:
    if Player_1_column != secret_column or Player_1_row != secret_row:
        result_box = WHITE_BOX
        while row_ctr <= grid:
            while column_ctr <= grid:
                if Player_1_column == column_ctr and Player_1_row == row_ctr:
                    row += result_box
                else:
                    row += BLUE_BOX
                column_ctr += 1
            print(row)
            row = ""
            row_ctr += 1
            column_ctr = 1
    if Player_1_column == secret_column and Player_1_row != secret_row:
        print("Close! Correct column, wrong row.")
    elif Player_1_column != secret_column and Player_1_row == secret_row:
        print("Close! Correct row, wrong column.")
    else:
        print("Miss!")