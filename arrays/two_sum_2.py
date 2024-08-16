"""
Two Sum II - Input Array Is Sorted

!!! IMPORTANT
1 <= index1 < index2 <= numbers.length

indices should be in order, preserve order of indices, add 1
"""
import unittest


class Solution(object):
    def using_dict(self, numbers, target):
        seen = dict()

        for i, value in enumerate(numbers):
            remaining = target - value

            if remaining in seen:
                return [seen[remaining] + 1, i + 1]  # to preserve order
            else:
                seen[value] = i

    def two_pointer(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [2, 7, 11, 15], 'target': 9, 'expected': [1,2]},
            {'input': [2, 3, 4], 'target': 6, 'expected': [1,3]},
            {'input': [3, 3], 'target': 6, 'expected': [1, 2]},
            {'input': [-1, 0], 'target': -1, 'expected': [1, 2]},
        ]

    def run_test(self, method):
        for test in self.test_values:
            with self.subTest(test=test):
                output = method(numbers=test['input'], target=test['target'])
                self.assertEqual(output, test['expected'])

    def test_using_dict(self):
        self.run_test(self.solution.using_dict)

    def test_two_pointer(self):
        self.run_test(self.solution.two_pointer)


if __name__ == '__main__':
    unittest.main()
