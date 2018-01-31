"""
lab2.py
Andry Bintoro
1/30/2018
"""

def squared_nums(num_list):
    """
    squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    new_list = [ ] #initialize list to hold results
    #iterate through num_list and square each element
    for num in num_list:
        sq_num = pow(num,2)
        new_list.append(sq_num)
    return new_list

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are title_list
    """
    pass
