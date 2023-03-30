# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("eileen")
define s = Character("Samantha")
define p = Character("Pedro")
define l = Character("Laplace")
define pai = Character ("Pai")

image fundo = "images/quarto.jpg"
image pai = "images/pai.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fundo:
        zoom 3.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pai:
        zoom 1.5

    # These display lines of dialogue.

    pai "Eu sou o seu pai"

    pai "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
