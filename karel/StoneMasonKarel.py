from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    # lets fix this building!! 
    turn_left()
    while right_is_clear():
        linear_beeper_place()
        next_pillar()
    linear_beeper_place()

def linear_beeper_place():
    put_beeper_ifEmpty()
    while front_is_clear():
        move()
        put_beeper_ifEmpty()

def put_beeper_ifEmpty():
    if beepers_present():
        pass
    else:
        put_beeper()

def next_pillar():
    turn_around()
    while front_is_clear():
        move()
    travel_next()

def travel_next():
    turn_left()
    for i in range(4):
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
