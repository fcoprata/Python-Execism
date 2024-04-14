def append(list1, list2):
    """
    Concatenates two lists and returns the result.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: The concatenated list.
    """
    return list1 + list2


def concat(lists):
    """
    Concatenates a list of lists into a single list.

    Args:
        lists (list): A list of lists.

    Returns:
        list: The concatenated list.

    Example:
        >>> concat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    concat = []
    for list in lists:
        concat += list
    return concat


def filter(function, lists):
    """
    Filters the given lists based on the provided function.

    Args:
        function: A function that takes an element from the lists as input and returns a boolean value.
        lists: A list of lists to be filtered.

    Returns:
        A new list containing only the elements from the lists that satisfy the given function.

    Example:
        >>> filter(lambda x: x % 2 == 0, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[2], [4, 6], [8]]
    """
    items = []
    for list in lists:
        if function(list):
            items = concat([items, [list]])

    return items


def length(list):
    """
    Returns the length of the given list.

    Parameters:
    list (list): The list for which the length needs to be calculated.

    Returns:
    int: The length of the list.
    """
    return sum(1 for x in list)


def map(function, list):
    """
    Applies the given function to each element in the list and returns a new list
    containing the results.

    Args:
        function: The function to apply to each element.
        list: The list of elements to apply the function to.

    Returns:
        A new list containing the results of applying the function to each element.
    """
    return [function(x) for x in list]


def foldl(function, list, initial):
    """
    Applies a function to each element in the list, starting with the initial value,
    and returns the final result.

    Args:
        function: The function to apply to each element.
        list: The list of elements to iterate over.
        initial: The initial value to start with.

    Returns:
        The final result after applying the function to each element.
    """
    for x in list:
        initial = function(initial, x)
    return initial


def foldr(function, list, initial):
    """
    Applies a function to the elements of a list from right to left, using an initial value.

    Args:
        function: The function to apply to the elements of the list.
        list: The list of elements to apply the function to.
        initial: The initial value to use in the folding operation.

    Returns:
        The result of applying the function to the elements of the list from right to left.

    """
    for x in list[::-1]:
        initial = function(initial, x)
    return initial


def reverse(list):
    """
    Reverses the order of elements in a list.

    Args:
        list (list): The list to be reversed.

    Returns:
        list: The reversed list.
    """
    return list[::-1]
