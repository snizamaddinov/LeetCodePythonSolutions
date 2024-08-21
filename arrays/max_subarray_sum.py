import unittest

class Solution(object):
    def brute_force(self, nums):
        max_sum = nums[0]

        for i in range(0, len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)

        return max_sum

    def kadane_algorithm(self, nums):
        max_sum = float('-inf')
        current_sum = 0

        for i in nums:
            current_sum += i
            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [-2,1,-3,4,-1,2,1,-5,4], 'expected': 6},
            {'input': [1], 'expected': 1},
            {'input': [5,4,-1,7,8], 'expected': 23}
        ]

    def run_test(self, method):
        for test_value in self.test_values:
            with self.subTest(test=test_value):
                output = method(test_value['input'])
                self.assertEqual(output, test_value['expected'])

    def test_brute_force(self):
        self.run_test(self.solution.brute_force)

    def test_kadane_algorithm(self):
        self.run_test(self.solution.kadane_algorithm)


if __name__ == '__main__':
    unittest.main()