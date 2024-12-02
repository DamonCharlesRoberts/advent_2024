# Day 2 Solutions

# Import dependencies.
from utils.input import rectangular

def day_2(input:str="./inputs/day_1.txt", part_a:bool=True) -> int:
    """Function for day 2 solutions.

    Args:
        input(str): The path to the input data.
        part_a(bool): Whether this is for Part A.

    Returns:
        int: The solution.
    """
    # Load the inputted data.
    data = rectangular(input=input)

    #
