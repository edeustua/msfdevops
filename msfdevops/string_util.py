"""
Miscellaneous strin functions
"""

# import me


def title_string(in_str):
    """
    Converts a string to title case

    Title case means that the first character of every word is
    capitalized, otherwise lowercase

    Parameters
    ----------
    in_str: str
        The string to convert to title case


    Returns
    -------
    str
        The input string in title case


    Examples
    --------
    >>> title_string("this iS a StrING to be ConverTeD")
    'This Is A String To Be Converted'

    >>> title_string("this should be a title some time")
    'This Should Be a Title Some Time'

    """

    tmp_s = in_str.lower()

    new_s = ""
    for word in tmp_s.split():
        new_s += word[0].upper() + word[1:] + ' '

    return new_s[0:-1]
