# Day 1 solutions.

# Import dependencies.
from utils.input import two_lists

# Define function.
def day_1_solution(input:str ="./inputs/day_1.txt", part_a:bool = True) -> int:
    """Function for the day 1 solution.

    Args:
        input(str): The input txt file.
<<<<<<< HEAD
        part_a(bool): Is this for Part A?
=======
>>>>>>> a5a7d9d (Day 1.)

    Returns:
        int: The sum of the differences between the two lists.
    """
    # 1. Open the input file.
    list_one, list_two = two_lists(input=input)
    # 5. Solve the puzzle for part_a.
    if part_a:
        # a. Order the two lists.
        list_one.sort()
        list_two.sort()
        # b. Subtract the two lists and get the absolute value of the   difference.
        diff = [abs(i-j) for i, j in zip(list_one, list_two)]
        # c. Sum the lists.
        solution = sum(diff)
    else:
        # a. count the number of times each element in the first list
        # appears in the second list.
        matched_values = dict((i, list_two.count(i)) for i in set(list_one))
        # b. Compute the similarity score.
        score = [(i * matched_values[i]) for i in list_one]
        # c. Get the sum of the similarity score.
        solution = sum(score)
    # 6. Return the total difference between the lists.
    return solution



try:
    # Test the solution for a.
    assert day_1_solution(input='./inputs/test_input.txt') == 11
    print(f"Test solution for part a is: {day_1_solution    (input='./inputs/test_input.txt')}")
    # Compute the solution for a.
    print(f"Solution for part a is: {day_1_solution()}")
except:
    print("Part A solution is incorrect.")

try:
    # Test the solution for b.
    assert day_1_solution(input='./inputs/test_input.txt', part_a = False) == 31
    print(f"Test solution for part b is: {day_1_solution(input='./inputs/test_input.txt', part_a=False)}")
    # Compute the solution for b.
    print(f"Solution for part b is: {day_1_solution(part_a=False)}")
except:
    print("Part B solution is incorrect.")
