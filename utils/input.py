# Utility functions.

def two_lists(input:str="./inputs/day_1.txt") -> tuple[list,list]:
    """Load the txt data and return two lists.

    Args:
        input(str): The file path.

    Returns:
        tuple[list, list]: Return two lists.
    """
    #1. Open the file.
    with open(input) as file:
            # 2. Create a list for each line in the file.
            line = [line.rstrip() for line in file]
            # 3. Split each line and extract the first element and put in list  1.
            list_one = [int(i.split("   ")[0]) for i in line]
            # 4. Split each line and extract the first element and put in list  2.
            list_two = [int(i.split("   ")[1]) for i in line]
    # 5. Return the lists.
    return list_one, list_two

def rectangular(input:str = "./inputs/day_1.txt") -> dict[str, list[int]]:
    """Load a rectangular input line by line.

    Args:
        input(str): The txt file containing the input.

    Returns:
        dict: A dictionary of reports
    """
    # 1. Open the file.
    with open(input) as file:
        # 2. Read the contents of the file line by line.
        input_dict = {i:[int(j) for j in i.rstrip().split(" ")] for i in file}
    # 2. Return the result.
    return input_dict
