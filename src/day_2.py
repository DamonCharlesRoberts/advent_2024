# Day 2 Solutions

# Import dependencies.
from utils.input import rectangular

def day_2(input:str="./inputs/day_2.txt") -> int:
    """Function for day 2 solutions.

    Args:
        input(str): The path to the input data.

    Returns:
        int: The solution.
    """
    # Load the inputted data.
    data = rectangular(input=input)
    # Determine the difference between each report element in each report.
    diff = {i:[(data.get(i)[j+1] - data.get(i)[j]) for j in range(len(data.get(i))-1)] for i in data}
    # Determine whether that difference is within acceptable limits for each report.
    acceptable = {
        i: [
            (True if all(x > 0 for x in diff.get(i)) else True if all(x < 0 for x in diff.get(i)) else False),
            (True if all(1 <= abs(x) <= 3 for x in diff.get(i)) else False)
        ] for i in diff
    }
    safe = [
        i for i in acceptable if acceptable[i].count(True) == 2
    ]
    # Determine the number of reports that are safe.
    num_safe = len(safe)
    # Return the number of safe reports.
    return num_safe


try:
    # Test the solution for a.
    assert day_2(input='./inputs/test_input.txt') == 2
    print(f"Test solution for part a is: {day_2(input='./inputs/test_input.txt')}")
    # Compute the solution for a.
    print(f"Solution for part a is: {day_2()}")
except:
    print("Part A solution is incorrect.")
