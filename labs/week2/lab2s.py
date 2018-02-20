def squared_nums(num_list):
    """
    Squares numbers in a num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    return [num**2 for num in num_list]

def check_title(title_list):
    """
    Removes strings in title_list that thave numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    for word_index in range(len(title_list)):
        # strip the underscores out
        title_list[word_index] = title_list[word_index].replace('_', ' ')
    return [word for word in title_list if word.istitle()]


def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    Inventory: a dictinoary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    return {key: val + 10 for key, val in inventory.items()}

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: intenger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    return {key: val for key, val in inventory.items() if inventory[key] != 0}

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
        key: string of students name
        value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    return {key: [float(sum(val) / len(val))] for key, val in grades.items()}
