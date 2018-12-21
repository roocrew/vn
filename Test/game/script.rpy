# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gordon")

image gordon happy = "/gordon/1.png"
image gordon sad = "/gordon/2.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show gordon happy

    # These display lines of dialogue.

    g "Sup, I'm jared, im 19 and i never fucking learned how to read."

    g "BBBBBBBBBBBBBBBBBBBBBBBBBBB"

    show gordon sad

    g "Wii fit trainer isn't top tier"

    # This ends the game.

    return
