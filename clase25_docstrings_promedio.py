def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The average of the numbers in the list.
    
    Raises:
    ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    return sum(numbers) / len(numbers)

#imprimiendo resultado de la funcion
print(calculate_average([10, 20, 30, 40, 50]))  # Example usage