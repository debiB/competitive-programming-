# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        temp  =  head
        even = head.next
        sp = even
        while temp.next and even.next:
            temp.next = even.next
            temp = even.next
            even.next = temp.next
            even = temp.next
        temp.next = sp
        return head