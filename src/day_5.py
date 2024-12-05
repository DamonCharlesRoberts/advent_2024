# Day 5 solutions.
import re

def solution(input:str="./inputs/day_5.txt"):
    """Solutions for day 5 puzzle.

    Args:
        input(str): String to input path.

    Returns:

    """
    # Read in the data.
    with open(input) as f:
        data = [i.strip() for i in f]
    ordering = [
        [
            int(j) for j in i.split("|")
        ] for i in data if '|' in i and i != ''
    ]
    prints = [
        [
            int(j) for j in i.split(",")
        ] for i in data if ',' in i and i != ''
    ]
