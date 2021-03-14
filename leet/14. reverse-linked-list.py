"""
https://leetcode.com/problems/reverse-linked-list/
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# self
def reverse_linked_list(head: ListNode) -> ListNode:
    if head is None or head.val is None:
        return head
    ln2 = ListNode(val=head.val)
    while head.next is not None:
        ln2 = ListNode(val=head.next.val, next=ln2)
        head = head.next
    return ln2


# solution 1
def reverseList1(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# solution 2
def reverseList2(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

result = reverseList1(one)

while result.next is not None:
    print(result.val)
    result = result.next
print(result.val)



