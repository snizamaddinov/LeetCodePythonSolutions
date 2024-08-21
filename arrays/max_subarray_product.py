import unittest


class Solution(object):
    def brute_force(self, nums):
        max_product = float('-inf')
        n = len(nums) - 1

        for i in range(0, n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]

            if max_product < curr:
                max_product = curr

        for i in range(n - 1, -1, -1):
            curr = 1
            for j in range(i, -1, -1):
                curr *= nums[j]

            if max_product < curr:
                max_product = curr

        return max_product


    def kadane_algorithm(self, nums):
        max_product = float('-inf')
        current_product = 1
        for n in nums:
            current_product *= n

            if max_product < current_product:
                max_product = current_product

            if current_product == 0:
                current_product = 1

        current_product = 1
        for i in range(len(nums) - 1, -1, -1):
            current_product *= nums[i]

            if max_product < current_product:
                max_product = current_product

            if current_product == 0:
                current_product = 1

        return max_product

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [2,3,-2,4], 'expected': 6},
            {'input': [-2,0,-1], 'expected': 0},
            # {'input': [5,4,-1,7,8], 'expected': 23}
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