import unittest


class Solution(object):
    def brute_force_two_sum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i, j]

    def optimized(self, numbers, target):
        seen = dict()

        for i, value in enumerate(numbers):
            remaining = target - value

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
            {'input': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
            {'input': [3, 3], 'target': 6, 'expected': [0, 1]}
        ]

    def test_optimized(self):
        for test in self.test_values:
            with self.subTest(test=test):
                output = self.solution.optimized(numbers=test['input'], target=test['target'])
                self.assertEqual(set(output), set(test['expected']))

    def test_brute_force_two_sum(self):
        for test in self.test_values:
            with self.subTest(test=test):
                output = self.solution.brute_force_two_sum(numbers=test['input'], target=test['target'])
                self.assertEqual(set(output), set(test['expected']))


if __name__ == '__main__':
    unittest.main()
