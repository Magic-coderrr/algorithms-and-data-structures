# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):

        prev = None
        curr = head
        
        while curr:

            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
    

