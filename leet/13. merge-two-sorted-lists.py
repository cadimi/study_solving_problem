"""
https://leetcode.com/problems/merge-two-sorted-lists/
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


five = ListNode(2)
four = ListNode(1, five)
# three = ListNode(1, four)

five2 = ListNode(3)
four2 = ListNode(1, five2)
# three2 = ListNode(1, four2)

result = mergeTwoLists(four, four2)

while result.next is not None:
    print(result.val)
    result = result.next
print(result.val)