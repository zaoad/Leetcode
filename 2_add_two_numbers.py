# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        ans=ListNode()
        ans=head
        carry=0
        while l1 or l2:
            val1=0
            val2=0
            if(l1!=None):
                val1=l1.val
            if(l2!=None):
                val2=l2.val
            temp=ListNode((val1+val2+carry)%10, None)
            carry=int((val1+val2+carry)/10)
            ans.next=temp
            ans=ans.next
            if(l1!=None):
                l1=l1.next
            if(l2!=None):
                l2=l2.next

        if carry:
            ans.next = ListNode( carry )

        return head.next