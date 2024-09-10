import random
def tic_tac_toe():
    list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def print_board():
        board = f'''
        
              |       |
          {list[0]}   |   {list[1]}   |   {list[2]}
       _______|_______|______
              |       |
          {list[3]}   |   {list[4]}   |   {list[5]}        
       _______|_______|______
              |       |
          {list[6]}   |   {list[7]}   |   {list[8]}       
              |       |

       '''
        print(board)

    def determine_winner(player_one, player_two, tie):
        if (list[0] == list[1] == list[2] == 'X') or (list[3] == list[4] == list[5] == 'X') or (list[6] == list[7] == list[8] == 'X') or (list[0] == list[3] == list[6] == 'X') or (list[1] == list[4] == list[7] == 'X') or (list[2] == list[5] == list[8] == 'X') or (list[0] == list[4] == list[8] == 'X') or (list[2] == list[4] == list[6] == 'X') :
           return player_one  
        if (list[0] == list[1] == list[2] == 'O') or (list[3] == list[4] == list[5] == 'O') or (list[6] == list[7] == list[8] == 'O') or (list[0] == list[3] == list[6] == 'O') or (list[1] == list[4] == list[7] == 'O') or (list[2] == list[5] == list[8] == 'O') or (list[0] == list[4] == list[8] == 'O') or (list[2] == list[4] == list[6] == 'O') :
          return player_two
        if (list[0] == ("X" or "O")) and (list[1] == ("X" or "O")) and (list[2] == ("X" or "O")) and (list[3] == ("X" or "O")) and (list[4] == ("X" or "O")) and (list[5] == ("X" or "O")) and (list[6] == ("X" or "O")) and (list[7] == ("X" or "O")) and (list[8] == ("X" or "O")):
           return tie

    def user_input(player):
        player_input = input(f"Enter your choice between 1 and 9, {player}: ")
        while (player_input not in list) or (player_input in ["X", "O"]):
            player_input = input("Invalid input. Enter a number between 1 and 9: ")
        return player_input

    def game():
        attempts = 0
        print("-----------Welcome to the tic tac toe game!-----------")

        players = input("Enter 'a' to play with computer and 'b' to play with a friend: ")
        while players not in ["a", "b"]:
            players = input("Invalid Input. Enter 'a' to play with computer and 'b' to play with a friend: ")

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
        print_board()
    
        while 0 <= attempts:
            if attempts % 2 == 0:
                player_one_choice = user_input(player_one)
                list[int(player_one_choice) - 1] = "X"
            if attempts % 2 != 0:
                if player_two == "Computer":
                    player_two_choice = random.choice(list)
                    while player_two_choice in ["X", "O"]:
                        player_two_choice = random.choice(list)
                    print(f"Computer chose {player_two_choice}")
                    list[int(player_two_choice) - 1] = "O"
                else: 
                    player_two_choice = user_input(player_two)
                    list[int(player_two_choice) - 1] = "O"
            attempts += 1
            print_board()
    
            winner = determine_winner(player_one, player_two, tie)
            if winner == player_one:
                print(f"-----------You Win, {player_one}-----------\n")
                break
            if winner == player_two:
                if player_two == "Computer":
                    print(f"-----------The computer wins the game.-----------\n")
                    break
                else:
                    print(f"-----------You Win, {player_two}-----------\n")
                    break
            if winner == tie:
                print(f"-----------It's a draw.-----------\n")
                break
    game()
tic_tac_toe()