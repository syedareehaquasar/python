from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    # pick beeper and place it inside the room 
    move()
    move()
    pick_beeper() #reached beeper
    move()
    turn_left()
    move()
    move()
    put_beeper() #place beeper
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
