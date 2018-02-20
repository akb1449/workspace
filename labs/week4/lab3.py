"""
lab3.py
Andry Bintoro
2/6/2018
"""

def switch_case(str_list):
    """
    Maps strings in the str_list to a new string of
    same characters, but the first letter contains
    the opposite case
    str_list: list of strings
    Returns: list of original strings, but with
    opposite casing
    >>> switch_case([test])
    [Test]
    """
    if str_list[0][:1].isupper():
        str_list[0][:1].swapcase()
    elif str_list[0][:1].islower():
        str_list[0][:1].swapcase()
    else:
        return str_list

def only_even(mixed_list):
    """
    Filters out odd integers and strings that
    contain an odd number of characters.
    mixed_list: list of integers and/or strings
    Returns: list of only integers and strings that
    are even or have an even number of characters.
    """

def greatest_difference(num_list):
    """
    Finds the maximum and minimum numbers in a_list
    and computes the difference.
    num_list: list of numbers
    Returns: the difference between the maximum and
    minimum numbers in num_list
    """

def make_title(words):
    """
    Maps words in a list to words in the same list,
    but as titled strings.
    words: list of words
    Returns: new list of titled words
    """

def test_title(names):
    """
    Filters out capitalized and non- cap words into
    their respective lists.
    names: list of names
    Returns: both lists for review
    """

def create_word(char_list):
    """
    Takes a list of characters and creates a word
    (list with alpha chars only) from them.
    letters: list of etters
    Returns: list that has alpha characters only
    """

def three_times_nums(num_list):
    """
    Maps numbers in the num_list to numbers that are
    3 times the original value
    num_list: list of numbers
    Returns: list of numbers that are of three times
    the values in num_list
    """

def keep_lowercase(str_list):
    """
    Filters out strings that have uppercase values
    str_list: list of strings
    Returns: list of strings that do not contain
    uppercase values
    """

def multiplication_total_of(num_list):
    """
    Multiplies all the numbers in num_list together
    and gives the total
    num_list: list of numbers
    Returns: the multiplied total of the numbers in
    the num_list
    """

def square_nums(number_list):
    """
    Maps numbers in the number_list to numbers of
    same value, but squares the number given
    number_list: list of numbers
    Returns: list from number_list which are squared
    """

def lessthan_5(num_list):
    """
    Filters out numbers less than five
    num_list: list of numbers
    Returns: list of numbers in the original list
    that are less than five
    """

def subtraction_of(number_list):
    """
    Subtracts the numbers in number_list
    number_list: list of numbers
    Returns: the difference of the numbers in the
    number_list
    """

def double_nums(num_list):
    """
    Maps numbers in the num_list to their doubles
    num_list: list of numbers
    Returns: list of doubled numbers
    """

def remove_special_characters(string_list):
    """
    Filters out strings that have non-alphanumeric
    elements
    char_list: list of strings
    Returns: list of strings that have only letters
    or numbers in them
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
