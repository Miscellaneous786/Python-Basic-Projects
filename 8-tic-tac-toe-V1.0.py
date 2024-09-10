import random
def tic_tac_toe():
    def win():
        if   ((board[34]) == (board[44]) == (board[54]) == "X") or ((board[122]) == (board[132]) == (board[142]) == "X") or ((board[210]) == (board[220]) == (board[230]) == "X"):
                return p1
        elif ((board[34]) == (board[122]) == (board[210]) == "X") or ((board[44]) == (board[132]) == (board[220]) == "X") or ((board[54]) == (board[142]) == (board[230]) == "X"):
                return p1
        elif ((board[34]) == (board[132]) == (board[230]) == "X") or ((board[54]) == (board[132]) == (board[210]) == "X"):
                return p1
        if   ((board[34]) == (board[44]) == (board[54]) == "O") or ((board[122]) == (board[132]) == (board[142]) == "O") or ((board[210]) == (board[220]) == (board[230]) == "O"):
                return p2
        elif ((board[34]) == (board[122]) == (board[210]) == "O") or ((board[44]) == (board[132]) == (board[220]) == "O") or ((board[54]) == (board[142]) == (board[230]) == "O"):
                return p2
        elif ((board[34]) == (board[132]) == (board[230]) == "O") or ((board[54]) == (board[132]) == (board[210]) == "O"):
                return p2
        else:
                return None
    
    board = '''
             |         |
        a    |    b    |    c
    _________|_________|________
             |         |
        d    |    e    |    f
    _________|_________|________
             |         |
        g    |    h    |    i
             |         |
    '''
    a = (board.find("a"))
    print(f"Position of a is {a}")
    print("Welcome to the game.")
    play = (input("Enter 1 to play with the computer and 2 to play with a friend: "))
    while play not in (["1", "2"]):
        play = (input("Invalid Response. Enter 1 to play with the computer and 2 to play with a friend: "))
    if play == "1":
        p1 = input("Enter your name, player 1: ")
        p2 = "computer"
    elif play ==  "2":
        p1 = input("Enter your name, player 1: ")
        p2 = input("Enter your name, player 2: ")     
                
    print(board)

    choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    turns = 3

    while turns >= 0:
        turns -= 1
        p1_choice = input(f"Enter your choice, {p1}: ").lower()
        while p1_choice not in choices:
            p1_choice = input(f"Invalid choice, {p1}. Please enter a valid choice: ").lower()
        choices.remove(p1_choice)    
        board = board.replace(p1_choice, "X")
        print(board)
        winner = win()
        if winner == p1:
            print("-"*25+f"You Win, {p1}"+"-"*25)
            break
        
        if p2 == "computer":
            p2_choice = random.choice(choices)
            print(f"Computer chose {p2_choice}")
            choices.remove(p2_choice)    
            board = board.replace(p2_choice, "O")
            print(board)
            winner = win()
            if winner == p2:
                print("-"*25+"The computer wins the game."+"-"*25)
                break
        else:
            p2_choice = input(f"Enter your choice, {p2}: ")
            while p2_choice not in choices:
                p2_choice = input(f"Invalid choice, {p2}. Please enter a valid choice: ")
            choices.remove(p2_choice)    
            board = board.replace(p2_choice, "O")
            print(board) 
            winner = win()
            if winner == p2:
                print("-"*25+f"You Win, {p2}"+"-"*25)
                break
    else:
        p1_choice = input(f"Enter your choice, {p1}: ")
        while p1_choice not in choices:
            p1_choice = input(f"Invalid choice, {p1}. Please enter a valid choice: ")
        choices.remove(p1_choice)    
        board = board.replace(p1_choice, "X")
        print(board)
        winner = win()
        if winner == p1:
            print("-"*25+f"You Win, {p1}"+"-"*25)

        elif winner == None:
            print("-"*25+f"It's a Tie."+"-"*25)
            
tic_tac_toe()