# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        ptr = dummy
        buff = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            if (val1 + val2) > 9 and buff == 0:
                ptr.next = ListNode((val1 + val2) % 10)
                buff = 1
            elif (val1 + val2) >= 9 and buff == 1:
                ptr.next = ListNode((val1 + val2 + buff) % 10)
            elif (val1 + val2) < 9 and buff == 1:
                ptr.next = ListNode((val1 + val2 + buff) % 10)
                buff = 0
            else:
                ptr.next = ListNode((val1 + val2 + buff) % 10)
                buff = 0
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if buff != 0:
            ptr.next = ListNode(buff)
        return dummy.next
