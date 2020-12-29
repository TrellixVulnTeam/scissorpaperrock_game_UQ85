# scissor paper rock game
import random
import time

def gamewin(computer, human):
    if computer == human:
        return None
    elif computer == 's':
        if human == 'p':
            return False
        elif human == 'r':
            return True
    elif computer == 'p':
        if human == 'r':
            return False
        elif human == 's':
            return True
    elif computer == 'r':
        if human == 's':
            return False
        elif human == 'p':
            return True


print("Computer's turn: Scissor(s) Paper(p) Rock(r) ?")
randommove: int = random.randint(1, 3)
if randommove == 1:
    computer = 's'
elif randommove == 2:
    computer = 'p'
elif randommove == 3:
    computer = 'r'

from time import sleep
sleep(1)
print("Choosed by computer...")
human = input("Human's turn: Scissor(s) Paper(p) Rock(r) ?")
result = gamewin(computer, human)
if result == None:
    print("Tie")
elif result:
    print("You Win!")
else:
    print("You Lose!")

print(f"{computer} was choosed by Computer")
