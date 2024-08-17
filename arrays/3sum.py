import unittest


class Solution(object):
    def using_dict(self, nums):
        triplets = set()
        nums.sort()
        for i, value in enumerate(nums[:-2]):
            if i > 0 and value == nums[i - 1]:
                continue

            seen = dict()
            for value2 in nums[i+1:]:
                remaining = -value - value2

                if value2 not in seen:
                    seen[remaining] = 1
                else:
                    triplets.add((value, remaining, value2))

        return [list(t) for t in triplets]


    def two_pointer(self, nums):
        triplets = []
        n = len(nums)
        nums = sorted(nums)
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                sum_ = nums[left] + nums[right] + value

                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    triplets.append([value, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_values = [
            {'input': [-1,0,1,2,-1,-4], 'expected': [[-1,-1,2],[-1,0,1]]},
            {'input': [0,1,1], 'expected': []},
            {'input': [0,0,0], 'expected': [[0,0,0]]},
        ]

    def run_test(self, method):
        for test in self.test_values:
            with self.subTest(test=test):
                output = method(nums=test['input'])
                self.assertEqual(output, test['expected'])

    def test_using_dict(self):
        self.run_test(self.solution.using_dict)

    def test_two_pointer(self):
        self.run_test(self.solution.two_pointer)


if __name__ == '__main__':
    unittest.main()


