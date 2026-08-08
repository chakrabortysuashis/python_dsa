def reverse_array_two_pointers(arr):
    """
    Reverses an array in place using the two-pointer technique.
    The time complexity of this function is O(n), where n is the number of elements in the array. The space complexity is O(1) since we are not using any additional data structures.

    Parameters:
    arr (list): The array to be reversed.

    Returns:
    list: The reversed array.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers towards the center
        left += 1
        right -= 1

    return arr

def reverse_array_single_pointer(arr):
    """
    Reverses an array in place using a single pointer technique.
    The time complexity of this function is O(n), where n is the number of elements in the array. The space complexity is O(1) since we are not using any additional data structures.

    Parameters:
    arr (list): The array to be reversed.

    Returns:
    list: The reversed array.
    """
    n = len(arr)
    for i in range(n // 2):
        # Swap the elements at the current index and its corresponding index from the end
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

    return arr


arr=[1,5,3,4,8]
print("Original array:", arr)
print("Reversed array using two pointers:", reverse_array_two_pointers(arr.copy()))
print("Reversed array using single pointer:", reverse_array_single_pointer(arr.copy()))