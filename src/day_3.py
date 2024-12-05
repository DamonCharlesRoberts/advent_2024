# Day 3

import re
import math

def solution(input="./inputs/day_3.txt", part_a:bool=True) -> int:
    """Day 3 solutions.

    Args:
        input(str): The input.
        part_a(bool): Whether this is for part a or not.

    Returns:
        int: The sum of the products.
    """
    # Load the data.
    data = open(input, "r").read()
    # Perform a regex to extract anything that meets the following pattern:
        # mul(#,#)
    if part_a:
        matched = [
            [int(j) for j in re.findall(r"\d+", i)] for i in re.findall(r"mul\(\d+,\d+\)", data)
        ]
        # Multiply the extracted integers and get sum.
        result = sum([
            math.prod(i) for i in matched
        ])
    else:
        data = "do()"+ data
        dos = [i.split("don't()")[0] for i in data.split("do()")]
        matched = [
            [[int(x) for x in re.findall(r"\d+",j)] for j in re.findall(r"mul\(\d+,\d+\)", i)] for i in dos
        ]
        # Multiply the extracted integers and get sum.
        result = sum([sum(x) for x in
            [[math.prod(j) for j in i] for i in matched]
        ])
    # Return the result.
    return result

try:
    assert solution(input="./inputs/test_input.txt") == 161
    print(f"The solution to part a is: {solution()}")
except:
    print("The test for part a failed.")

try:
    assert solution(input="./inputs/test_input.txt",part_a=False) == 48
    print(f"The solution to part b is: {solution(part_a=False)}")
except:
    print("The test for part b failed.")
