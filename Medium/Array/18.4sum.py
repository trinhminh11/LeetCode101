"""
18. 4Sum
Difficulty: Medium
https://leetcode.com/problems/4sum/

──────────────────────────────────────────────────

Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        • 0 <= a, b, c, d < n

        • a, b, c, and d are distinct.

        • nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]



Constraints:

        • 1 <= nums.length <= 200

        • -10^9 <= nums[i] <= 10^9

        • -10^9 <= target <= 10^9
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        n = len(nums)

        outputs: list[list] = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1

                while k < l:
                    current = nums[i] + nums[j] + nums[k] + nums[l]
                    if current == target:
                        outputs.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l:
                            if nums[k] == nums[k - 1]:
                                k += 1
                            else:
                                break
                        while k < l:
                            if nums[l] == nums[l + 1]:
                                l -= 1
                            break
                    elif current < target:
                        k += 1
                    else:
                        l -= 1

        return list(outputs)
