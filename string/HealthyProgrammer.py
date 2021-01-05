from pygame import mixer
from datetime import datetime
from time import time
def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_saving(msg):
    with open("programmerlog.txt","a") as f:
        f.write(f"{msg} at {datetime.now()}\n")


if __name__ == '__main__':
    water = time()
    eyes = time()
    exercise = time()
    waterspan = 30*60
    exspan = 40*60
    eyespan = 45*60
    while True:
        if time() - water > waterspan:
            print("Please Drink Water...... \n type 'drank' to stop the alarm")
            music("pour_me_a_drink.mp3", "drank")
            log_saving("Drank Water ")
            water = time()
            if input("Enter Q to quit the program") == "Q":
                break

        if time() - exercise > exspan:
            print("Please perform some Exercise for your health...... \n type 'done' to stop the alarm")
            music("Workout.mp3", "done")
            log_saving("Done Exercise ")
            exspan = time()
            if input("Enter Q to quit the program") == "Q":
                break

        if time() - eyes > eyespan:
            print("Please have some eye rest for your  eye health...... \n type 'rested' to stop the alarm")
            music("ex.mp3", "rested")
            log_saving("Eye rest done ")
            eyespan = time()
            if input("Enter Q to quit the program") == "Q":
                break


