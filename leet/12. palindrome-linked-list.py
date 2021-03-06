"""
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""
from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


four = ListNode(1)
three = ListNode(2, four)
two = ListNode(2, three)
one = ListNode(1, two)

sol = Solution()
print(sol.isPalindrome(one))


class Solution2:
    # 1 2 3 2 1
    def isPalindrome2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            print(rev.val)
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


five = ListNode(1)
four = ListNode(2, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

sol = Solution2()
print(sol.isPalindrome2(one))
