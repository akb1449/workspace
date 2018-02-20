import unittest

class Lab2Test(unittest.TestCase):
    def test_squared(self):
        """
        Tests lab2.squared()
        """
        func = lab2.squared

        case1 = [1, 2, 3]
        expected1 = [1, 4, 9]
        self.assertEqual(func(case1), expected1)

    def test_check_title(self):
        """
        Tests lab2.checktitle()
        """
        func = check_title

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
        print("lab2.py module found.Testing...")
        unittest.main( )
    except ImportError:
        print("Missing lab4.py module")
