"""
Andry Bintoro
UNHM COMP705/805 Lab 2
11 Feb 2018

Tests all functions required in lab2
Uses python unittest framework:
https://docs.python.org/3/library/unittest.html#module-unittest
"""
import unittest


class TestLab2(unittest.TestCase):

    def setUp(self):
        """
        This is ran automatically at the beginning of the test cases
            defined below
        It is good to factor out any setup-code for subsequent tests
        It is NOT required to define setUp, it is just helpful in many cases
        """
        pass #because we dont have anything to setup.

    def tearDown(self):
        """
        This is ran automatically at the end of the test cases
            defined below
        It is good to factor out any tear down-code for subsequent tests
        It is NOT required to define tearDown, it is just helpful in many cases
        """
        pass #because we dont have anything to tearDown.

    def test_squared_nums(self):
        func = lab2.squared_nums # create a reference to the function

        case1 = [1,2,3]
        expected1 = [1,4,9]
        self.assertEqual(func(case1), expected1)

        case2 = []
        expected2 = []
        self.assertEqual(func(case2), expected2)

        case3 = [-1, -2, -3]
        expected3 = [1, 4, 9]
        self.assertEqual(func(case3), expected3)

        case4 = [1, 0]
        expected4 = [1, 0]
        self.assertEqual(func(case4), expected4)

    def test_check_title(self):
        func = lab2.check_title

        case1 = ['Hello World', 'Hello_world', 'Title']
        expected1 = ['Hello World', 'Title']
        self.assertEqual(func(case1), expected1)

        case2 = ['Hello_World', 'A great 3 Days', 'hello World']
        expected2 = ['Hello World']
        self.assertEqual(func(case2), expected2)
        
        case3 = ['10,11,12']
        expected3 = []
        self.assertEqual(func(case3), expected3)

    def test_restock_inventory(self):
        func = lab2.restock_inventory

        case1 = {'pencil': 10, 'pen': 8, 'paper': 7}
        expected1 = {'pencil': 20, 'pen': 18, 'paper': 17}
        self.assertDictEqual(func(case1), expected1)

        case2 = {'pencil': 0, 'pen': -3, 'paper': -11}
        expected2 = {'pencil': 10, 'pen': 7, 'paper': -1}
        self.assertDictEqual(func(case2), expected2)

        case3 = {'pencil': 0.5, 'pen': -3.2, 'paper': 11.0}
        expected3 = {'pencil': 10.5, 'pen': 6.8, 'paper': 21.0}
        self.assertDictEqual(func(case3), expected3)

    def test_filter_0_items(self):
        func = lab2.filter_0_items

        case1 = {'pencil': 10, 'pen': 8, 'paper': 7}
        expected1 = {'pencil': 10, 'pen': 8, 'paper': 7}
        self.assertDictEqual(func(case1), expected1)

        case2 = {'pencil': 0, 'pen': -3, 'paper': -11}
        expected2 = {'pen': -3, 'paper': -11}
        self.assertDictEqual(func(case2), expected2)

        case3 = {'pencil': 0.5, 'pen': -3.2, 'paper': 0.0}
        expected3 = {'pencil': 0.5, 'pen': -3.2}
        self.assertDictEqual(func(case3), expected3)

    def test_average_grades(self):
        func = lab2.average_grades

        case1 = {
                    'Michael': [100,78,88, 900/10],
                    'Daniel': [80,95,77,64.0],
                    'Josh': [99,89,94,66]
                }
        expected1 = {'Michael': [89.0], 'Daniel': [79.0], 'Josh': [87.0]}
        self.assertDictEqual(func(case1), expected1)

        case2 = {
                    'Michael': [5*20,188 * .5, 88],
                    'Daniel': [80.5, .15, 66, 64.0],
                    'Josh': [99 + 1 * -2, 40/.5]
                }
        expected2 = {'Michael': [94.0], 'Daniel': [52.6625], 'Josh': [88.5]}
        self.assertDictEqual(func(case2), expected2)

        case3 = {
                    'Michael': [78],
                    'Daniel': [90],
                    'Josh': [900/-9]
                }
        expected3 = {'Michael': [78.0], 'Daniel': [90.0], 'Josh': [-100.0]}
        self.assertDictEqual(func(case3), expected3)

if __name__ == '__main__':
    try:
        import lab2
        print('Found your lab2.py file. LETS DO IT!!!!')
    except ImportError:
        print('Snap...can\'t find lab2.py...I have no clue what do now. Bye!')
        exit()
    unittest.main()
