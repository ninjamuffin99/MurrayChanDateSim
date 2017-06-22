# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define J = Character("Jacob")
define M = Character("Maggie")
define Mu = Character("Murray-Chan")
define L = Character("Levi")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Character Select"
    menu:
        "Jacob":
            jump: jacobStory
        "Cameron":
            jump: cameronStory
        "Maggie":
            jump: maggieStory
        "Levi":
            jump LeviStory
    label jacobStory:
        
        "Jacob's story"

    label maggieStory:
        "there is nothing"
    label cameronStory:
        "nothin to see"
    label leviStory:
        "levis story"
    # This ends the game.

    return
