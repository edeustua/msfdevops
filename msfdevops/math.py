"""
Mathematical manipulations

Very cool stuff
"""

# no imports today


def mean(num_lst):
    """
    This function calculates the mean of a list of numbers

    Parameters
    ----------

    num_lst : list or tuple
        The list to take the average of

    Returns
    -------

    ret : float
        The mean of a list

    Examples
    --------

    >>> mean([1, 2, 3, 4, 5])
    3.0

    """
    # Check that user passes list
    #if not isinstance(num_lst, list) and not isinstance(num_lst, tuple):
    if not isinstance(num_lst, list):
        raise TypeError('Input must be a type list')

    # Check list length
    if len(num_lst) == 0:
        raise ZeroDivisionError('Cannot calculate mean of empty list')

    try:
        ret = sum(num_lst) / len(num_lst)
    except TypeError:
        raise TypeError('Values of list must be type int or float')

    return ret
