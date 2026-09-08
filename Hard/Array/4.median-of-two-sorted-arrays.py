"""
4. Median of Two Sorted Arrays
Difficulty: Hard
https://leetcode.com/problems/median-of-two-sorted-arrays/

──────────────────────────────────────────────────

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

        • nums1.length == m

        • nums2.length == n

        • 0 <= m <= 1000

        • 0 <= n <= 1000

        • 1 <= m + n <= 2000

        • -10^6 <= nums1[i], nums2[i] <= 10^6
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        left = 0
        right = n  # right of nums1

        even = (n + m) % 2 == 0

        while left <= right:
            median_A = (left + right) // 2
            median_B = (n + m + 1) // 2 - median_A

            max_left_A = float("-inf") if median_A == 0 else nums1[median_A - 1]
            min_right_A = float("inf") if median_A == n else nums1[median_A]
            max_left_B = float("-inf") if median_B == 0 else nums2[median_B - 1]
            min_right_B = float("inf") if median_B == m else nums2[median_B]

            if max_left_A <= min_right_B and max_left_B <= min_right_A:
                if even:
                    return (
                        max(max_left_A, max_left_B) + min(min_right_A, min_right_B)
                    ) / 2
                else:
                    return max(max_left_A, max_left_B)

            elif max_left_A > min_right_B:
                right = median_A - 1
            else:
                left = median_A + 1
