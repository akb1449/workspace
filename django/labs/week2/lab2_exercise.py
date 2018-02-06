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
    new_list = []  #initialize list to hold results
    #iterate through num_list and square each element
    for num in num_list:
        sq_num = pow(num,2)
        new_list.append(sq_num)
    return new_list

def check_title(title_list):

    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    message = "----"
    title_list = []  #initialize list to hold strings
    #iterate through title_list and remove strings that have numbers
    for i in title_list:
        try:
            if not isinstance(title_list[i], str):
                message += 'Did not return a string - Fail'
                #test_failed(results_dict)
            else:
                message += 'A string was returned - Pass'
                #test_passed(results_dict)
    return title_list

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """


def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: tring that is the name of the inventory item
        value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
        grades: a dictionary of grades with:
        key: string of students name
        value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
