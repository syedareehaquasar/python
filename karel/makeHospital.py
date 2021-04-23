from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_and_build()
    
def move_and_build():
    while no_beepers_present():
        move()
    make_hospital()

def make_hospital():
    turn_left()
    for i in range(2):
        move_and_putBeeper()
    turn_right()
    move_and_putBeeper()
    turn_right()
    while front_is_clear():
        move_and_putBeeper()
    turn_left()
    if front_is_clear():
        move()

def move_and_putBeeper():
    move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('HospitalKarel.w')
