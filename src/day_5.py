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
    prints_filtered = []
    prints_sorted = prints.copy()
    # For each list in prints, sort the list.
    # For each row in print command,
    for row in prints:
        needs_sorting = False
        # and for each page listed in the print command,
        for first, second in zip(row[0::1], row[1::1]):
            # look through each pair,
            for pair in ordering:
                # and determine whether the page is in the pair.
                if first in pair:
                    if second in pair:
                        if first != pair[0]:
                            needs_sorting = True
                            #prints_sorted[first], prints_sorted[second] = prints[second], prints[first]
        if not needs_sorting:
            prints_filtered.append(row)
    # Of the lists in the correct order, sum the middle page number for the job.
    solution = sum([
        sum([
            prints_filtered[i][j] for j in range(len(prints_filtered[i])) if j == int((len(prints_filtered[i])-1)/2)
        ]) for i in range(len(prints_filtered))
    ])
    # Return the solution.
    return solution

try:
    assert solution(input="./inputs/test_input.txt")==143
    print("Test solution for Part A is correct.")
    print(f"Solution for Part A is:{solution()}")
except AssertionError:
    print("Test solution for Part A is incorrect.")
    print(f"Test returned {solution(input='./inputs/test_input.txt')} but should have returned 143.")
