# Day 4 solution.

def solution(input: str = "./inputs/day_4.txt") -> tuple:
    """Solution for Day 4.

    Args:
        input(str): The file path to the input file.

    Returns:
        int: Number of times the word "XMAS" appears in the grid.
        list[list[str]]: A list of list of strings with
        the matched characters.
    """
    # Load the data.
    with open(input) as f:
        data = [[j for j in i.rstrip()] for i in f]

    # Initialize the objects.
    words_found = 0
    len_y = len(data)
    len_x = len(data[0])
    debug_matrix = [['' for _ in range(len_x)] for _ in range(len_y)]

    # Iterate over the grid to check for the word "XMAS" in all directions.
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Left to Right.
            if x <= len_x - 4 and data[y][x] == 'X' and data[y][x+1] == 'M' and data[y][x+2] == 'A' and data[y][x+3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y][x+1] = 'M'
                debug_matrix[y][x+2] = 'A'
                debug_matrix[y][x+3] = 'S'

            # Right to Left.
            if x >= 3 and data[y][x] == 'X' and data[y][x-1] == 'M' and data[y][x-2] == 'A' and data[y][x-3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y][x-1] = 'M'
                debug_matrix[y][x-2] = 'A'
                debug_matrix[y][x-3] = 'S'

            # Up to Down.
            if y <= len_y - 4 and data[y][x] == 'X' and data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y+1][x] = 'M'
                debug_matrix[y+2][x] = 'A'
                debug_matrix[y+3][x] = 'S'

            # Down to Up.
            if y >= 3 and data[y][x] == 'X' and data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y-1][x] = 'M'
                debug_matrix[y-2][x] = 'A'
                debug_matrix[y-3][x] = 'S'

            # Diagonal Down and Right.
            if y <= len_y - 4 and x <= len_x - 4 and data[y][x] == 'X' and data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y+1][x+1] = 'M'
                debug_matrix[y+2][x+2] = 'A'
                debug_matrix[y+3][x+3] = 'S'

            # Diagonal Up and Right:
            if y >= 3 and x <= len_x - 4 and data[y][x] == 'X' and data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y-1][x+1] = 'M'
                debug_matrix[y-2][x+2] = 'A'
                debug_matrix[y-3][x+3] = 'S'

            # Diagonal Down and Left.
            if y <= len_y - 4 and x >= 3 and data[y][x] == 'X' and data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y+1][x-1] = 'M'
                debug_matrix[y+2][x-2] = 'A'
                debug_matrix[y+3][x-3] = 'S'

            # Diagonal Up and Left.
            if y >= 3 and x >= 3 and data[y][x] == 'X' and data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
                words_found += 1
                debug_matrix[y][x] = 'X'
                debug_matrix[y-1][x-1] = 'M'
                debug_matrix[y-2][x-2] = 'A'
                debug_matrix[y-3][x-3] = 'S'

    return words_found, debug_matrix


try:
    assert solution(input='./inputs/test_input.txt')[0]== 18
    print(f"Solution for test of Part a: {solution(input='./inputs/test_input.txt')[0]}")
    print(f"Solution to Part a: {solution()[0]}")
except AssertionError:
    print(f"Test input did not return the correct answer for part a: {solution(input='./inputs/test_input.txt')[0]}")
    # Print the debug_matrix if there is a problem.
    for i in solution(input='./inputs/test_input.txt')[1]:
        print(i)
