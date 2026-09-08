"""
16. 3Sum Closest
Difficulty: Medium
https://leetcode.com/problems/3sum-closest/

──────────────────────────────────────────────────

Given an integer array nums of length n and an integer target, find
three integers at distinct indices in nums such that the sum is
closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1
= 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 =
0).



Constraints:

        • 3 <= nums.length <= 500

        • -1000 <= nums[i] <= 1000

        • -10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        n = len(nums)

        ret = 0
        diff = float("inf")

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                curr_diff = target - s

                if curr_diff > 0:
                    j += 1
                elif curr_diff < 0:
                    k -= 1
                else:
                    return target

                if abs(curr_diff) < diff:
                    diff = abs(curr_diff)
                    ret = s

        return ret
