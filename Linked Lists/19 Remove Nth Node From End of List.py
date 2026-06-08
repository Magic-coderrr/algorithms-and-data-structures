# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy_lst = ListNode(0)
        dummy_lst.next = head
        
        left = dummy_lst
        right = dummy_lst

        # Creating the gap of size n
        for i in range(n):
            right = right.next

        # Sliding the window until right hits the last node
        while right.next:
            left = left.next
            right = right.next
            
        # Delete the target node
        left.next = left.next.next
        
        return dummy_lst.next