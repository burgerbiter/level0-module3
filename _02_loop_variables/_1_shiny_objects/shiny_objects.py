from tkinter import simpledialog, Tk


can_play_sounds = False


def play_mister_zee():
    print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    ok = simpledialog.askinteger(title="1",prompt="How many shiny objects do you want?")
    # TODO 3) Play the sound that many times
    for i in range(ok):
        play_mister_zee()
    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
