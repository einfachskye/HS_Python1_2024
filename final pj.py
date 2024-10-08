import os

player1_score = 0
player2_score = 0 
choices = ['rock', 'paper', 'scissors']

player1_choice = ""
player2_choice = ""

def decision_loop(player1_choice, player2_choice):
    global player1_score
    global player2_score
    if player1_choice == player2_choice:
            print("It's a tie this round!")
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
        (player1_choice == 'scissors' and player2_choice == 'paper') or \
        (player1_choice == 'paper' and player2_choice == 'rock'):
            print("Player 1 wins this round!")
            player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1


def player_decision_loop(player):
     global player1_choice
     global player2_choice
     if player == 1:
          while True:
            player1_choice = input("Player 1, enter rock, paper, or scissors: ").lower()
            if player1_choice not in choices:
                print("Invalid choice for Player 1! Please enter rock, paper, or scissors.")
            else:
                 break
     elif player == 2:
            while True:
                player2_choice = input("Player 2, enter rock, paper, or scissors: ").lower()
                if player2_choice not in choices:
                    print("Invalid choice for Player 2! Please enter rock, paper, or scissors.")
                else:
                    break
        




def play_game(best_of_n):
    rounds_needed_to_win = (best_of_n // 2) + 1
    
    round_number = 1
    while player1_score < rounds_needed_to_win and player2_score < rounds_needed_to_win:
        print(f"\nRound {round_number}:")


        player_decision_loop(player=1)
        
        os.system("clear")

        player_decision_loop(player=2)
            
        
        
        decision_loop(player1_choice, player2_choice)
        

        round_number += 1

    
    print("\nFinal Score:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    
    if player1_score > player2_score:
        print("Player 1 is the overall winner!")
    else:
        print("Player 2 is the overall winner!")


best_of_n = int(input("Enter the total number of rounds (Best of N): "))
play_game(best_of_n)
