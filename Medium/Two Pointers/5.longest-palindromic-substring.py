"""
5. Longest Palindromic Substring
Difficulty: Medium
https://leetcode.com/problems/longest-palindromic-substring/

──────────────────────────────────────────────────

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

        • 1 <= s.length <= 1000

        • s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left: int, right: int):
            if s[left] != s[right]:
                return ""

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        ret = s[0]

        for i in range(n - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)

            print(odd, even)

            if len(odd) > len(ret):
                ret = odd

            if len(even) > len(ret):
                ret = even

        return ret
