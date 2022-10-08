from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    dow = Tk()
    dow.withdraw()
    q1 = simpledialog.askstring(title="1",prompt="You find yourself in the middle of a swamp. Do you eat, drink, or find a way out?")
    if q1 == "eat":
        print("you got poisoned and died")
        exit()
    elif q1 == "drink":
        print("You drank the dirty water.")
    elif q1 == "way out":
        print("you look for a way out")
    else:
        print("died of improper answer")
        exit()
    q2 = simpledialog.askstring(title="2",prompt="You have three paths: one covered in trees and swampland, one full of mud and puddles, and one full of alligators. Which way do you go?")
    if q2 == "alligators":
        print("You got eaten by an alligator")
        exit()
    elif q2 == "trees":
        print("You went deeper into the swamp forest")
        q3a = simpledialog.askstring(title="3",prompt="You feel tired, hungry, and thirsty. Do you eat, drink, sleep, or keep going?")
        if q3a == "drink":
            print("You drank some swamp water")
        elif q3a == "nothing":
            print("You died of overexertion")
            exit()
        elif q3a == "eat":
            print("you ate some bugs")
        elif q3a == "sleep":
            print("you slept for a while")
        else:
            print("died of improper answer")
            exit()
        if q1 == "drink":
            print("you died of poisoning from the water you drank")
            exit()
        print("You finally find a rescue helicopter. It brings you back to civilization...")
        if q3a == "drink":
            print("but you died of poisoning from the water")

    elif q2 == "mud":
        print("You waded further into the mud")
        q3b = simpledialog.askstring(title="3",prompt="You feel tired, hungry, and thirsty. Do you eat, drink, sleep, or keep going?")
        if q3b == "drink":
            print("You drank some swamp water")
        elif q3b == "nothing":
            print("You died of overexertion")
            exit()
        elif q3b == "eat":
            print("You ate some mud and died of poisoning")
            exit()
        elif q3b == "sleep":
            print("You slept for a while")
        else:
            print("died of improper answer")
            exit()
        if q1 == "drink":
            print("you died of poisoning from the water you drank")
            exit()
        print("As you slog through the mud, you realize your decision was wrong. There is nothing in this mud: no sustinence, no water, nothing. You die in the mud and never make it back to civilization")
    else:
        print("died of improper answer")
        exit()
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
