import unittest


class Solution(object):
    def with_auxiliary(self, nums):
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        ans = list()
        pre[0] = 1
        suf[n - 1] = 1
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        for i in range(n):
            ans.append(pre[i] * suf[i])

        return ans

    def without_auxiliary(self, nums):
        ans = [1] * len(nums)

        curr_pre = 1
        for i in range(len(nums)):
            ans[i] = curr_pre
            curr_pre *= nums[i]

        curr_suf = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= curr_suf
            curr_suf *= nums[i]

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [1, 2, 3, 4], 'expected': [24, 12, 8, 6]},
            {'input': [-1, 1, 0, -3, 3], 'expected': [0, 0, 9, 0, 0]},
        ]

    def run_test(self, method):
        for test in self.test_values:
            with self.subTest(test=test):
                output = method(test['input'])
                self.assertEqual(output, test['expected'])

    def test_using_dict(self):
        self.run_test(self.solution.with_auxiliary)

    def test_two_pointer(self):
        self.run_test(self.solution.without_auxiliary)


if __name__ == '__main__':
    unittest.main()
