num = 19
guess = 9
f=0
for i in range(9):
    ug = int(input("Enter the number as your guess: "))
    if ug == num and i<=8:
        print("Congratulations You won!!!\n The number is: ", num)
        f = 1
        break
    elif ug > num and i < 8:
        print("Your Guess is Bigger, Try again with something smaller")
        print("Guesses Left: ", 9-(i+1))
        f = 0
    elif ug < num and i<8:
        print("Your Guess is Smaller. Try again with Bigger Numbers.")
        print("Guesses Left: ", 9 - (i+1))
        f = 0
if f == 1:
    print("The Number of Guesses taken: ", i+1)
else:
    print("You couldn't guess with in the Guess limit")
    print("-----------GAME OVER--------------")