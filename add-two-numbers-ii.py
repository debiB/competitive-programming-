# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev):
            if not head:
                return prev
            else:
                nxt = head.next
                head.next = prev
                return helper(nxt,head)
        head = l1
        head2 = l2
        val1 = 0
        val2= 0 

        while head:
            val1= (val1*10) + head.val  
            head = head.next
        while head2:
            val2 = (val2*10) + head2.val
            head2= head2.next
        _sum = val1+val2
        dummy = ListNode()
        d_h = dummy
        if _sum == 0:
            return ListNode(0)
        while _sum > 0:
            dummy.next = ListNode(_sum%10)
            dummy = dummy.next
            _sum//= 10
        return helper(d_h.next, None)