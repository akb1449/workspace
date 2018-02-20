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
    new_list = [ ]  #initialize list to hold results
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
    new_list = [" "]    #initialize list to hold strings
    #iterate through title_list and remove strings that have numbers
    for string in title_list:
        if string.isalpha() and string.istitle():
            new_list.append(string)
    return new_list

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    new_inventory = { }    #initialize new inventory
    for key, value in inventory.items():
        val = val + 10
        inventory[key] = val
        #value += 10
        #inventory.update({key:value})
    return new_inventory

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: tring that is the name of the inventory item
        value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    new_inventory = { }    #initialize new inventory
    for key, value in inventory.items():
        if value in inventory == 0:
            new_inventory[key]=value
        """
        if value == 0:
            inventory.pop({key:None})
        else:
            inventory.update()
        """
    return new_inventory

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
        grades: a dictionary of grades with:
        key: string of students name
        value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    new_grades = {} #initialize new grades
    for name, grades in grades.items():
        new_grades[name]=sum(grades) /len(grades)
    return new_grades
