import random
def rock_paper_scissors():
    def win():
        if (player_choice == 'r' and computer_choice == 'p') or (player_choice == 's' and computer_choice == 'r') or (player_choice == 'p' and computer_choice == 's'):
            return 'player'
        elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p'):
            return 'computer'
        else:
            return 'No Winner'

    print("Welcome to the rock, paper scissors game.")
    player = input("Enter your name: ")
    print(f"You have to choose between rock, paper and scissors, {player}\nEnter 'r' for rock, 's; for scissors and 'p' for paper\n")
    
    player_score = 0
    computer_score = 0

    while (player_score != 5) or (computer_score != 5):
        player_choice = input(f"\nEnter your choice, {player}: ").lower()
        while player_choice not in ["r", "p", "s"]:
            player_choice = input("Invalid attempt, Enter your choice again: ").lower()
        computer_choice = random.choice(["r", "p", "s"])
        print(f"Computer chose {computer_choice}")
        winner = win()
        if winner == "computer":
            print("-"*25+"Computer wins this round."+"-"*25)
            computer_score += 1
        if winner == "player":
            print("-"*25+f"You win this round, {player}"+"-"*25)   
            player_score += 1
        if winner == "No Winner":
             print("-"*31+"It's a draw"+"-"*31)
        print(f"Current Score: \n   Score of {player}: {player_score}\n   Score of Computer: {computer_score}")
        if player_score == 5:
            print("-"*25+f"You won the game, {player}"+"-"*25)
            break
        if computer_score == 5:
            print("-"*25+"\nThe computer won the game.\n"+"-"*25)
            break
rock_paper_scissors()