import unittest


class Solution(object):
    def kadane_algorithm(self, prices):
        b = prices[0]
        p = 0
        for i in range(1, len(prices)):
            if prices[i] < b:
                b = prices[i]
            elif (prices[i] - b) > p:
                p = prices[i] - b

        return p

    def two_pointer(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [7, 1, 5, 3, 6, 4], 'expected': 5},
            {'input': [7, 6, 4, 3, 1], 'expected': 0}
        ]

    def run_test(self, method):
        for test in self.test_values:
            with self.subTest(test=test):
                output = method(test['input'])
                self.assertEqual(output, test['expected'])

    def test_using_dict(self):
        self.run_test(self.solution.two_pointer)

    def test_two_pointer(self):
        self.run_test(self.solution.kadane_algorithm)


if __name__ == '__main__':
    unittest.main()
