
def get_player_move():
    move = input("Choose your move: ")
    return move

def check_move_is_valid(move):
    while move.lower().strip() not in ['rock','paper', 'scissors']:#.strip() gets rid of trailing/ leading spaces
        print("Sorry, thats not a valid move. Please choose either rock, paper, or scissors")
        move = get_player_move()
    return move

def check_winner(payer_1_move, payer_2_move):
    if payer_1_move == payer_2_move:
        print("It's a tie!")
    elif payer_1_move == 'rock' and payer_2_move!= 'paper':
        print("Player 1 wins")
    elif payer_1_move == 'paper' and payer_2_move!= 'scissors':
        print("Player 1 wins")
    elif payer_1_move == 'scissors' and payer_2_move!= 'rock':
        print("Player 1 wins")
    else:
        print('Player 2 wins')


def repeat_game():
   if input("\nEnter yes to play again. Or press any other button to exit: ").lower() == 'yes':
       return True

def main():
    play_again = True
    print("Welcome to Rock, Paper, Scissors!")
    while play_again: 
        print("\nOk, lets, play!")
        print("Player 1, you will start first ")
        payer_1_move = get_player_move()
        payer_1_move = check_move_is_valid(payer_1_move)
        print("Player 2, its your turn now")
        player_2_move = get_player_move()
        payer_2_move = check_move_is_valid(player_2_move)
        check_winner(payer_1_move, payer_2_move)
        play_again = repeat_game()
    else:
        print("Ok, thanks for playing. See ya later!")

main()