def generate_sorted_array(size):
    """
    Generate a sorted array for testing.

    Parameters:
    - size: The size of the array to generate.

    Returns:
    - sorted_array: A sorted list of integers.
    """
    return list(range(1, size + 1))


def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Parameters:
    - arr: A sorted list of elements.
    - target: The element to search for.

    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found in the array


def binary_search_count(arr, target):
    """
    Perform binary search and count occurrences in an array.

    Parameters:
    - arr: A sorted or unsorted list of elements.
    - target: The element to search for.

    Returns:
    - count: The count of occurrences of the target element in the array.
    """
    count = 0
    index = binary_search(arr, target)

    while index != -1:
        count += 1
        index = binary_search(arr[index + 1:], target)

    return count


# Example usage:
size_of_array = 20
sorted_array = generate_sorted_array(size_of_array)
target_element = 7

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")

occurrences = binary_search_count(sorted_array, target_element)
print(f"Number of occurrences of {target_element}: {occurrences}")
