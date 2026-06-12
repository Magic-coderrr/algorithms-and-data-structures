# Given the head of a linked list, rotate the list to the right by k places.
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        # edge cases: empty list or just one node
        if not head or not head.next:
            return head
        
        # get total length and park old_tail at the very last node
        length = 1
        old_tail = head
        while old_tail.next:
            length += 1
            old_tail = old_tail.next
            
        # optimize k so we don't do useless full rotations as if there are 3 elements in list and 
        # k is also 3 then we can just skip rotations as we will get same list after 3 rotations 
        k = k % length
        if k == 0:
            return head
            
        # connect end to start to make a circle
        old_tail.next = head
        
        # walk to the node right before the cut (length - k - 1 steps)
        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next
            
        # save the new head, then break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head