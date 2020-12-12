import random
list1 = ["S", "W", "G"]
sets = 1
comp = 0
user = input("Enter Your Name")
uscore = 0
while sets!=11:
    cchoice = random.choice(list1)
    uchoice = input("Enter S for snake\n Enter W for water\n Enter G for gun ")
    if cchoice == uchoice:
        print("This set is a DRAW!")
    elif (uchoice == "S" and cchoice == "W") or (uchoice == "W" and cchoice == "G") or (uchoice == "G" and cchoice == "S"):
        print("You Win The Set!!!")
        uscore += 1
        print("The Current score is: ", comp, ":", uscore)
    else:
        print("Computer Wins this set!!!")
        comp += 1
        print("The Current score is: ", comp, ":", uscore)
    sets += 1
if uscore > comp:
    print("Final Score : ", comp, ":", uscore)
    print("CONGRATULATIONS %s WINS!!!!!"%user)
elif uscore < comp:
    print("Final Score : ", comp, ":", uscore)
    print("Computer WINS!!!! Try Again Later")
else:
    print("Final Score : ", comp, ":", uscore)
    print("ITS a DRAW!!!!, Try Harder Next Time")