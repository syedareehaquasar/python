from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""

def main():
    while front_is_clear():
        move()
        clean_beeper()

def clean_beeper():
    if beepers_present():
      pick_beeper()

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
