# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        ret = curr
        addNext = False

        while l1 and l2:
            total = l1.val + l2.val
            if addNext:
                total += 1
            if total >= 10:
                addNext = True
                val = total - 10
            else:
                addNext = False
                val = total
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val if not addNext else l1.val + 1
            if total >= 10:
                val = total - 10
                addNext = True
            else:
                val = total
                addNext = False
            curr.next = ListNode(val)
            l1 = l1.next
            curr = curr.next
        while l2:
            total = l2.val if not addNext else l2.val + 1
            if total >= 10:
                val = total - 10
                addNext = True
            else:
                val = total
                addNext = False
            curr.next = ListNode(val)
            l2 = l2.next
            curr = curr.next
        if addNext:
            curr.next = ListNode(1)

        return ret.next
        