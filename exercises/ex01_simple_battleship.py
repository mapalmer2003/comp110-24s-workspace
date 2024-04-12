"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730477576"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
battlefield: str = ""
player_1_choice: int = int(input("pick a secret boat location between 1 and 4: ")) 
if player_1_choice < 1:
    print("Error! " + str(player_1_choice) + " too low!")
    exit()
elif player_1_choice > 4:
    print("Error! " + str(player_1_choice) + " too high!")
    exit()
else:
    player_2_choice: int = int(input("Guess a number between 1 and 4: ")) 
    if player_2_choice < 0:
        print("Error! " + str(player_2_choice) + " too low!")
        exit()
    elif player_2_choice > 5:
        print("Error! " + str(player_1_choice) + " too high!")
        exit()
    else:
        if player_2_choice != player_1_choice:
            result = WHITE_BOX
            if player_2_choice == 1:
                battlefield = battlefield + result
            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 2:
                battlefield = battlefield + result

            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 3:
                battlefield = battlefield + result
            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 4:
                battlefield = battlefield + BLUE_BOX
            else:
                battlefield += BLUE_BOX
            print(battlefield)
            print("Incorrect! You missed the ship.")       
        else:
            result = RED_BOX
            if player_2_choice == 1:
                battlefield = battlefield + result
            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 2:
                battlefield += result
            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 3:
                battlefield = battlefield + result
            else:
                battlefield = battlefield + BLUE_BOX
            if player_2_choice == 4:
                battlefield = battlefield + result
            else:
                battlefield = battlefield + BLUE_BOX
            print(battlefield)
            print("Correct! You hit the ship.")