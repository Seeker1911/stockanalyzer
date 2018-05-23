import unittest

import stockanalyzer


class StockanalyzerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = stockanalyzer.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to stock_analyzer', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
