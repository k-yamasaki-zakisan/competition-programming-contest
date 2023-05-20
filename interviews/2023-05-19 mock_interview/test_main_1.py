import unittest
import main_1


class TestMain(unittest.TestCase):
    def test_count_by_date(self):
        """test method for count_by_date
        """
        space_id = 0
        day = 3
        ks = [
            [0, 0, 3],
            [0, 1, None],
            [0, 3, None],
            [1, 0, None],
        ]
        actual = main_1.count_by_date(space_id, day, ks)
        expected = [1, 2, 2, 2]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()