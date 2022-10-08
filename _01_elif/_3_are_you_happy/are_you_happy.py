from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    window = Tk()

    window.withdraw()

    q1 = simpledialog.askstring(title="Happy", prompt="Are you happy?")
    if q1 == "yes":
        print("Keep doing what you're doing.")

    elif q1 == "no":
        q2 = simpledialog.askstring(title="Happy", prompt="Do you want to be happy?")
        if q2 == "yes":
            print("Change something.")
        elif q2 == "no":
            print("Keep doing what you're doing.")


    pass
