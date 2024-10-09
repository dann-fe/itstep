import unittest as ut

from my_sum import sum

class TestSum(ut.TestCase):
    def test_list_int(self):
        data = [4, 9, 20]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    ut.main()