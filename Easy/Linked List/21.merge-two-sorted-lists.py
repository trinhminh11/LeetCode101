"""
21. Merge Two Sorted Lists
Difficulty: Easy
https://leetcode.com/problems/merge-two-sorted-lists/

──────────────────────────────────────────────────

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



Constraints:

        • The number of nodes in both lists is in the range [0, 50].

        • -100 <= Node.val <= 100

        • Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = ListNode(val=list1.val)
        current = head

        current_A = list1.next
        current_B = list2

        increase_A = False

        while True:
            if current_A is None and current_B is None:
                break

            if current_A is None:
                increase_A = False
            elif current_B is None:
                increase_A = True
            else:  # currentA and currentB is not None
                if current_A.val <= current_B.val:
                    increase_A = True
                else:
                    increase_A = False

            if increase_A:
                next_node = ListNode(current_A.val)
                current_A = current_A.next
            else:
                next_node = ListNode(current_B.val)
                current_B = current_B.next
            current.next = next_node
            current = current.next

        return head
