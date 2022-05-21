import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function"""

    def test_first_last_name(self):
        """能够正确处理项 moon fan这样的姓名么"""
        full_name = get_formatted_name('moon', 'fan1')
        self.assertEqual(full_name, 'Moon Fan')


if __name__ == '__main__':
    unittest.main()

