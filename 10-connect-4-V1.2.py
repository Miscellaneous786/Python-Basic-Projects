import random
def connect_four():
    list_of_entrances = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    def print_board():
        board = f'''
     _______________________________________________________________
    |       |       |       |       |       |       |       |       |
    |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[56]}   |   {list_of_entrances[57]}   |   {list_of_entrances[58]}   |   {list_of_entrances[59]}   |   {list_of_entrances[60]}   |   {list_of_entrances[61]}   |   {list_of_entrances[62]}   |   {list_of_entrances[63]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[48]}   |   {list_of_entrances[49]}   |   {list_of_entrances[50]}   |   {list_of_entrances[51]}   |   {list_of_entrances[52]}   |   {list_of_entrances[53]}   |   {list_of_entrances[54]}   |   {list_of_entrances[55]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[40]}   |   {list_of_entrances[41]}   |   {list_of_entrances[42]}   |   {list_of_entrances[43]}   |   {list_of_entrances[44]}   |   {list_of_entrances[45]}   |   {list_of_entrances[46]}   |   {list_of_entrances[47]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[32]}   |   {list_of_entrances[33]}   |   {list_of_entrances[34]}   |   {list_of_entrances[35]}   |   {list_of_entrances[36]}   |   {list_of_entrances[37]}   |   {list_of_entrances[38]}   |   {list_of_entrances[39]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[24]}   |   {list_of_entrances[25]}   |   {list_of_entrances[26]}   |   {list_of_entrances[27]}   |   {list_of_entrances[28]}   |   {list_of_entrances[29]}   |   {list_of_entrances[30]}   |   {list_of_entrances[31]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[16]}   |   {list_of_entrances[17]}   |   {list_of_entrances[18]}   |   {list_of_entrances[19]}   |   {list_of_entrances[20]}   |   {list_of_entrances[21]}   |   {list_of_entrances[22]}   |   {list_of_entrances[23]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[8]}   |   {list_of_entrances[9]}   |   {list_of_entrances[10]}   |   {list_of_entrances[11]}   |   {list_of_entrances[12]}   |   {list_of_entrances[13]}   |   {list_of_entrances[14]}   |   {list_of_entrances[15]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    |       |       |       |       |       |       |       |       |
    |   {list_of_entrances[0]}   |   {list_of_entrances[1]}   |   {list_of_entrances[2]}   |   {list_of_entrances[3]}   |   {list_of_entrances[4]}   |   {list_of_entrances[5]}   |   {list_of_entrances[6]}   |   {list_of_entrances[7]}   |
    |_______|_______|_______|_______|_______|_______|_______|_______|
    '''
        print(board)

    def choice(player, alternative):
        player_choice = input(f"Enter the column, {player}: ")
        while player_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                player_choice = input(f"Invalid choice. Enter the column, {player}: ")
    
        enter_choice(player, player_choice, alternative)
        return player_choice

    def enter_choice(player, player_choice, alternative):
        entrances = [-1, 7, 15, 23, 31, 39, 47]
        for i in entrances:
            if list_of_entrances[int(player_choice) - 1] in [" "]:
                list_of_entrances[int(player_choice) - 1] = alternative 
            elif list_of_entrances[int(player_choice) + i] in ["X", "O"] and list_of_entrances[int(player_choice) + (i+8)] in [" "]:
                list_of_entrances[int(player_choice) + (i+8)] = alternative
                break
            elif list_of_entrances[int(player_choice) + 55] in ["X", "O"]:
                print(f"This column is full, {player}. Choose another column.")
                return choice(player, alternative) 
        
    def game():
        print("----------------------Welcome to the game.----------------------")
        players = input("Enter 'a' to play with computer and 'b' to play with a friend: ").lower()
        while players not in ["a", "b"]:
            players = input("Invalid Input. Enter 'a' to play with computer and 'b' to play with a friend: ").lower()

        if players == "a":
            player_one = input("Enter your name, player one: ")
            while player_one in [""]:
                player_one = input("Invalid Input, Enter your name, player one: ")
            player_two = "Computer"

        elif players == "b":
            player_one = input("Enter your name, player one: ")
            while player_one in [""]:
                player_one = input("Invalid Input, Enter your name, player one: ")
            player_two = input("Enter your name, player two: ")
            while player_two in ["", "Computer"]:
                player_two = input("Invalid Input, Enter your name, player two: ")
        tie = ""
        print("\n",f"{player_one}, your sign is 'X'")    
        print(f" {player_two}, your sign is 'O'")    
        print_board()

        attempts = 0
        while attempts >= 0:
            attempts += 1
            if attempts % 2 != 0:
                player_choice = choice(player_one, "X")
                print_board()
                winner = determine_winner(player_one, tie, "X")
                if winner == player_one:
                    print(f"-----------------------------You win, {player_one}-----------------------------")
                    break
            if attempts % 2 == 0:
                if player_two in ["Computer"]:
                    player_two_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                    print(f"Computer chose {player_two_choice}")
                    enter_choice(player_two, player_two_choice,  "O")
                elif player_two not in ["Computer"]:
                    player_choice = choice(player_two, "O")
                print_board()
                winner = determine_winner(player_two, tie, "O")
                if winner == player_two:
                    if player_two in ["Computer"]:
                        print(f"-----------------------------The computer wins.-----------------------------")           
                    if player_two not in ["Computer"]:
                        print(f"-----------------------------You win, {player_two}-----------------------------")
                    break
                if winner == tie:
                    print("-----------------------------Its a draw.-----------------------------")
                    break
    
    def determine_winner(player, tie, alternative):
    #   winner condition for horizontal rows
        for i in [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45]:
            if   list_of_entrances[i-1:i+3] == [alternative, alternative, alternative, alternative]:
                return player
    #   winner condition for vertical rows
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]:
            if   [list_of_entrances[i], list_of_entrances[i+8], list_of_entrances[i+16], list_of_entrances[i+24]] == [alternative, alternative, alternative, alternative]:
                return player
    #   winner condition for right diagonal
        for i in [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 25, 26, 27, 28, 29, 33, 34, 35, 36]:
            if   [list_of_entrances[i], list_of_entrances[i+9], list_of_entrances[i+18], list_of_entrances[i+27]] == [alternative, alternative, alternative, alternative]:
                return player
    #   winner condition for left diagonal
        for i in [3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 35, 36, 37, 38, 39]:
            if   [list_of_entrances[i], list_of_entrances[i+7], list_of_entrances[i+14], list_of_entrances[i+21]] == [alternative, alternative, alternative, alternative]:
                return player
    #   tie condition
        while " " not in list_of_entrances:
            return tie
    game()
    
connect_four()
