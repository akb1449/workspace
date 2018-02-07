"""
Andry Bintoro
UNHM COMP705/805 Lab 2
Week Python Practice
Jan 30, 2018

The purpose of this file is to test the functions declared in
lab2.py. This file does not use pythons unit test framework.
This file is intended to by used as a learning tool.

Please see: https://docs.python.org/3/library/unittest.html for information
    on pythons unit testing framework.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def test_failed(results_dict):
    """
    Increments global variables tests_ran and tests_failed
    """
    results_dict['tests_ran'] += 1
    results_dict['tests_failed'] += 1

def test_passed(results_dict):
    """
    Increments global variables tests_ran and tests_passed
    """
    results_dict['tests_ran'] += 1
    results_dict['tests_passed'] += 1

def test_squared_nums(results_dict):
    """
    Checks that lab2.squarednums() returns number in the list squared
    """
    print("")
    print("Testing lab2.squared_nums()")
    message = "----"
    try: #try with [1,2,3]
        result = lab2.squared_nums([1, 2, 3])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            print(result)
            message = 'Return squared values of 1,2,3 - Pass'
            test_passed(results_dict)
            print(message)
    except AttributeError:
        message += 'Could not find lab2.squared_nums() - Fail'
        test_failed(results_dict)

    try: #try with []
        result = lab2.squared_nums([])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            print(result)
            message = 'Return squared values of [] - Pass'
            test_passed(results_dict)
            print(message)
    except AttributeError:
        message = 'Could not find lab2.squared_nums() - Fail'
        test_failed(results_dict)

    try: #try again with [-1,-2,-3]
        result = lab2.squared_nums([-1, -2, -3])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            print(result)
            message = 'Return squared values of -1,-2,-3 - Pass'
            test_passed(results_dict)
            print(message)
    except AttributeError:
        message += 'Could not find lab2.squared_nums()- Fail'
        test_failed(results_dict)

    try: #try again with [1,0]
        result = lab2.squared_nums([1, 0])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            print(result)
            message = 'Return squared values of 1,0 - Pass'
            test_passed(results_dict)
            print(message)
    except AttributeError:
        message += 'Could not find lab2.squared_nums()- Fail'
        test_failed(results_dict)

def test_check_title(results_dict):
    """
    Checks that lab2.check_title() returns title_list only in strings
    """
    print("")
    print("Testing lab2.check_title()")
    message = "----"
    try:
        result = lab2.check_title(['Hello World', 'Hello_world', 'Title'])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            message = 'Returned title list with only strings - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message += 'Could not find lab2.check_title() - Fail'
        test_failed(results_dict)

    try:
        result = lab2.check_title(['Hello_World', 'A great 3 Days', 'hello World'])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            message = 'Returned title list with only strings - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message += 'Could not find lab2.check_title() - Fail'
        test_failed(results_dict)

    try:
        result = lab2.check_title(['10', '11', '12'])
        if not isinstance(result, list):
            message = 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            message = 'Returned title list with only strings - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message += 'Could not find lab2.check_title() - Fail'
        test_failed(results_dict)

def test_restock_inventory(results_dict):
    """
    Checks that lab2.restock_inventory() returns updated dictionary where each
    inventory item is restocked
    """
    print("")
    print("Testing lab2.restock_inventory()")

    try:
        result = lab2.restock_inventory({'pencil':10, 'pen':8, 'paper':7})
        if not isinstance(result, dict):
            message = 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message = 'A dictionary was returned - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message = 'Could not find lab2.restock_inventory() - Fail'
        test_failed(results_dict)
    print(message)

    try:
        result = lab2.restock_inventory({'pencil':0, 'pen':-3, 'paper':-11})
        if not isinstance(result, dict):
            message = 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message = 'A dictionary was returned - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message = 'Could not find lab2.restock_inventory() - Fail'
        test_failed(results_dict)
    print(message)

    try:
        result = lab2.restock_inventory({'pencil':0.5, 'pen':-3.2, 'paper':11.0})
        if not isinstance(result, dict):
            message = 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message = 'A dictionary was returned - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message = 'Could not find lab2.restock_inventory() - Fail'
        test_failed(results_dict)
    print(message)

def test_filter0_items(results_dict):
    """
    Checks that lab2.filter_0_items() returns the same inventory_dict
    with any item that had 0 quantity removed
    """
    print("")
    print("Testing lab2.filter_0_items()")
    message = "----"
    try:
        result = lab2.filter_0_items({'pencil':0, 'pen':-3, 'paper':-11})
        if not isinstance(result, dict):
            message += 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message += 'A dictionary was returned - Pass'
            test_passed(results_dict)
            print(result)
    except AttributeError:
        message += 'Could not find lab2.filter_0_items() - Fail'
        test_failed(results_dict)
    print(message)

def test_average_grades(results_dict):
    """
    Checks that lab2.average_grades() returns dictionary that averages
    out the grades of each student
    """
    print("")
    print("Testing lab2.average_grades()")
    message = "----"
    try:
        result = lab2.average_grades({'Michael' :[100, 78, 88, 900/10],
            'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]})
        if not isinstance(result, dict):
            message += 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message += 'A dictionary was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab2.average_grades - Fail'
        test_failed(results_dict)
    print(message)

def run():
    """
    This function is the test runner. It calls the functions
    declared in this file that are used to test the functions
    declared in lab2.py
    """
    results_dict = {
                    'tests_ran': 0,
                    'tests_passed': 0,
                    'tests_failed': 0,
                    }

    test_squared_nums(results_dict)
    test_check_title(results_dict)
    test_restock_inventory(results_dict)
    test_filter0_items(results_dict)
    test_average_grades(results_dict)


    print("")
    print("Final Results:")
    results = "%s tests ran: %s passed - %s failed." % (
                                                        results_dict['tests_ran'],
                                                        results_dict['tests_passed'],
                                                        results_dict['tests_failed']
                                                        )
    print(results)
    if results_dict['tests_ran'] == results_dict['tests_passed']:
        print('GOOD JOB! ALL TESTS PASSED!')
    else:
        print('Please correct your errors and run again')


if __name__ == "__main__":
    try:
        import lab2
        print("Found your lab2.py file. Running tests...")
    except ImportError:
        print("Could not import lab2.py. Please make sure both files are"
            " in the same directory")
        exit()
    run()
