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

    num_lst: list
        The list to take the average of

    Returns
    -------

    ret: float
        The mean of a list

    Examples
    --------

    >>> mean([1, 2, 3, 4, 5])
    3.0

    """
    ret = sum(num_lst) / len(num_lst)
    return ret
    #acumm = 0
    #for i in num_lst:
    #    acumm += i

    #return acumm / len(num_lst)
