"""
14. Longest Common Prefix
Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/

──────────────────────────────────────────────────

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

        • 1 <= strs.length <= 200

        • 0 <= strs[i].length <= 200

• strs[i] consists of only lowercase English letters if it is
non-empty.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        current_idx = 0

        ret = ""

        n_min = min([len(s) for s in strs])

        if n_min == 0:
            return ""

        while True:
            use_c = strs[0][current_idx]

            for s in strs[1:]:
                if s[current_idx] != use_c:
                    return ret

            ret += use_c

            current_idx += 1
            if current_idx >= n_min:
                return ret
