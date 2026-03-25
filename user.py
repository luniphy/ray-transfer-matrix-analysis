"""
198801 Introduction to Programming: Programming in Python

Final Examination: Ray Transfer Matrix Analysis - user file

:Author: Lukas Niggl
"""

from main import *
import numpy as np


def user_exe():
    """
    Function is focused on getting user inputs without causing errors and then prints the angles.

    :return: None
    """
    print('(1) Do you want to get the outgoing angles from entering an incoming angle value?\n'
          '(2) Or do you want to determine the incoming angle values for a given entered outgoing angle?')

    mode = None
    while mode not in ['1', '2']:
        mode = input('Type 1 or 2: ')
        if mode not in ['1', '2']:
            print('Invalid input!')

    if mode == '1':
        mode = True
    else:
        mode = False

    angle, MIN_ANGLE, MAX_ANGLE, STEPS = None, 0, 90, 0.001
    while angle is None or angle not in np.arange(MIN_ANGLE, MAX_ANGLE + STEPS, STEPS):
        angle = input('Enter angle between [0°, 90°] up to three decimals: ')
        try:
            angle = float(angle)
        except ValueError:
            print('Wrong input type!')
            angle = None
        else:
            if angle not in np.arange(MIN_ANGLE, MAX_ANGLE + STEPS, STEPS):
                print(ANGLE_VALUE_ERROR)

    distance, MIN_DISTANCE = None, 0
    while distance is None or distance < MIN_DISTANCE or distance >= radius:
        distance = input(f'Enter a distance from the optical axis smaller than {radius}m but greater or equal than 0: ')
        try:
            distance = float(distance)
        except ValueError:
            print('Wrong input type!')
            distance = None
        else:
            if distance < MIN_DISTANCE or distance >= radius:
                print(DISTANCE_VALUE_ERROR)

    print()
    print_angles(get_angles(angle, mode, distance))


if __name__ == '__main__':
    user_exe()
