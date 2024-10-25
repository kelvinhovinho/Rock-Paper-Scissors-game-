import random

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player=None

    while player not in choices:
        player =input("rock, paper or scissors?: ").lower()


    if player == computer:
        print(f'computer,{computer}')
        print(f'player, {player}')
        print("Tie!")

    elif player == 'rock':
        if computer == 'paper':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You LOSE!")
    
        if computer == 'scissors':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You WIN!")

    elif player == 'scissors':
        if computer == 'rock':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You LOSE!")
    
        if computer == 'paper':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You WIN!")

    elif player == 'paper':
        if computer == 'scissors':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You LOSE!")
    
        if computer == 'rock':
            print(f'computer,{computer}')
            print(f'player, {player}')
            print("You WIN!")

    play_again = input("Play again? yes/no ").lower()

    if play_again != "yes":
        break

print("BYE!!")