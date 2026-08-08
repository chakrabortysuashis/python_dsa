def find_min_max_of_array(arr):
    """
    This function takes an array as input and returns the minimum and maximum elements in the array.
    The time complexity of this function is O(n), where n is the number of elements in the array. The space complexity is O(1) since we are not using any additional data structures.
    
    Parameters:
    arr (list): A list of numerical values.
    
    Returns:
    tuple: A tuple containing the minimum and maximum values in the array.
    """
    if not arr:
        return None, None  # Return None for both if the array is empty
    
    min_element = arr[0]
    max_element = arr[0]
    
    for num in arr:
        if num < min_element:
            min_element = num
        elif num > max_element:
            max_element = num
            
    return min_element, max_element