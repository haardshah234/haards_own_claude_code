"""
Binary search implementation in Python.

Provides a function `binary_search(arr, target)` that returns the index of `target`
in a sorted list `arr`, or -1 if the target is not present.

The implementation works for any sequence that supports indexing and has a
length (`len`). It uses an iterative approach to avoid recursion depth limits.
"""

def binary_search(arr, target):
    """Return the index of `target` in sorted sequence `arr` or -1 if not found.

    Parameters
    ----------
    arr : Sequence
        A sorted sequence (list, tuple, etc.) where the search is performed.
    target : Any
        The value to search for.

    Returns
    -------
    int
        Index of `target` if present; otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage (can be removed or commented out in production)
if __name__ == "__main__":
    sample = [1, 3, 5, 7, 9, 11, 13]
    print("Index of 7:", binary_search(sample, 7))  # Output: 3
    print("Index of 2:", binary_search(sample, 2))  # Output: -1
