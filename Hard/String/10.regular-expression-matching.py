"""
10. Regular Expression Matching
Difficulty: Hard
https://leetcode.com/problems/regular-expression-matching/

──────────────────────────────────────────────────

Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*' where:

        • '.' Matches any single character.​​​​

        • '*' Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire
input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".



Constraints:

        • 1 <= s.length <= 20

        • 1 <= p.length <= 20

        • s contains only lowercase English letters.

        • p contains only lowercase English letters, '.', and '*'.

• It is guaranteed for each appearance of the character '*', there
will be a previous valid character to match.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(2, m + 1, 2):
            if p[j - 1] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, n + 1):
            i_index = i - 1
            for j in range(1, m + 1):
                j_index = j - 1
                if p[j_index] == "." or p[j_index] == s[i_index]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j_index] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j_index - 1] == "." or p[j_index - 1] == s[i_index]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]
