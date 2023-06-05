# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        l =  1
        temp = head
        while temp.next != None:
            temp = temp.next
            l += 1
        tail = temp
        print(l)
        k = k%l
        if k==0:
            return head
        temp.next = head
        it = 0;
        temp = head
        while it<l-k-1:
            temp = temp.next            
            it += 1
            print(temp.val)
        head = temp.next
        temp.next= None
        return head
            
