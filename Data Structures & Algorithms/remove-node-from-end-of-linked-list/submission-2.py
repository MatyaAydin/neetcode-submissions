# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0-indexed: remove node at index sz - n
        # n = 1: remove tail
        # make fast do n steps, then init slow at head
        # iter on both, when fast is at tail, slow is just before node to remove
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n+1): # one more iter to account for dummy node
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        