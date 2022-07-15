import random
randno = random.randint(1, 100)
print(randno)
guess = 0
ans = 'y'
while ans == 'y':
    userGuess = int(input("Enter your guess.."))
    if userGuess == randno:
        print("Perfect Guess!!! :)")
        ans = input("do you want to guess again? y|n")
        guess = guess+1
    elif userGuess > randno:
        print("Too High")
        guess = guess+1
        ans = input("do you want to guess again? y|n")
    else:
        print("Too Low")
        guess = guess+1
        ans = input("do you want to guess again? y|n")
print("No. of Guesses took", guess)
with open("highScore.txt", "r") as f:
    highScore = int(f.read())
if(guess < highScore):
    print("You have just broken the highest score!! :))")
    with open("highScore.txt", "w") as f:
        f.write(str(guess))
