import random 
import math


def victory(player, rival):
    if (player == 'r' and rival == 's') or (player == 's' and rival == 'p') or (player == 'p' and rival == 'r'):
        return True
    return False


def play():

    user = input("Press 'r' for Rock, 'p' for Paper or 's' for Scissors\n")
    user = user.lower()

    computer = random.choice(['r','p', 's'])

    if user == computer:
        return (0, user, computer)

    if victory(user, computer):
        return (1, user, computer)

    return (-1, user, computer)



def best_of(n):
    player_victories = 0
    computer_victories = 0
    necessary_wins = math.ceil(n/2) 
    while player_victories < necessary_wins and computer_victories < necessary_wins:
        result, user, computer = play()

        if result ==0:
            print ("I'd call it a tie! You and the rival picked {}. \n".format(user))

        elif result == 1:
            player_victories += 1
            print("You picked {} and the rival {}. You win!\n".format(user, computer))
        else:
            computer_victories += 1
            print ("You picked {} and the rival {}. You suck!\n".format(user, computer))
        print ('\n')

    if player_victories > computer_victories:
        print ("Congratz, you won the best of {} games. All girls will chase you ;)".format(n))
    else:
        print("The computer won the best of {} of games. You should be ashamed :(".format(n))
        

if __name__ == '__main__':
    best_of(3)
