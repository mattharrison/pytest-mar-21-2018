from block import Amount

import unittest


class TestAmount(unittest.TestCase):
    def test_todict(self):
        a = Amount('matt', 5)
        res = a.todict()
        self.assertEqual(res,
            {'uuid': 'matt', 'amount': 5})


if __name__ == '__main__':
    unittest.main()
