# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bunny", color="#E8EBED")
define a = Character("Alice", color="#C8D4E5")
define c = Character("Cheshire Cat", color="#8089D2")
define q = Character("Queen of Hearts", color="#A5231C")
define g = Character("Guard", color="#3D312E")
define m = Character("Mad Hatter", color="#2C3F70")

image bg_bedrm = "bedroom.png"
image bubble = "bubble.png"
image bg_field = "field.png"
image bunny eating = "bunny_eating.png"
image bunny stare = "bunny_stare.png"
image bunny turn = "bunny_turn.png"
image bunny run = "bunny_run.png"
image carrot = "carrot.png"
# The game starts here.
transform topLeftToCenterZoom:
        xalign 0.0
        yalign 0.0
        linear 1.5 xalign 0.5 yalign 0.5 zoom 2.0
    
label start:
    scene bg_bedrm
    show bubble at topleft
    with dissolve
    pause 1.0
    show bubble at topLeftToCenterZoom
    scene bg_field
    show bunny eating at center
    show carrot at center
    with dissolve
    b "munch munch munch..."
    show bunny stare
    pause 0.5
    show bunny turn
    pause 0.15
    show bunny run
    menu:
        "run after the bunny":
            scene black with fade
        "do nothing":
            pass
    return