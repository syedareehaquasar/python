from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    This program is for Karel to climb stairs and go inside the room by picking beeper which is a key and then plac it into red box.
    """
    turn_left()
    while front_is_clear():
        climb()
    descend()
    turn_right()
    move()
    pick_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()

def climb():
    while right_is_blocked():
        move()
    turn_right()
    move()
    turn_left()

def descend():
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
