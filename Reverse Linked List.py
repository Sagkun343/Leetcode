# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev is None:
            return head
        curr = prev.next
        if curr is None:
            return head
        forward = curr.next
        if forward is None:
            head = curr
            curr.next = prev
            prev.next = None
            return head
        prev.next = None
        while forward.next is not None:
            curr.next = prev
            prev = curr
            curr = forward
            forward = forward.next
        head = forward
        forward.next = curr
        curr.next = prev
        return head