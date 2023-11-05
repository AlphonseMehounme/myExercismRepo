"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#Defining 'EXPECTED_BAKE_TIME' and 'PREPARATION_TIME constants.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#Defining 'bake_time_remaining()' function.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#Defining 'preparation_time_in_minutes()' function.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - Number of layers to add to the lasagna
    :return: int - Preparation time

    Function that takes the number of layers to add to the lasagna and return the time of
    preparation
    """

    return number_of_layers * PREPARATION_TIME

#Defining 'elapsed_time_in_minutes()' function.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return (40 - bake_time_remaining(elapsed_bake_time)) + preparation_time_in_minutes(number_of_layers)
