# Given the head of a linked list, reverse the nodes of the list k at a time, and return the 
# modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the
#  number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        # Settingup and Counting
        dummy_node = ListNode(0)
        dummy_node.next = head
        curr = head
        count = 0
        groupPrev = dummy_node
        
        while curr:
            count += 1
            curr = curr.next

        # Loop and Glue
        while count >= k:
            curr = groupPrev.next
            prev = None
            
            # Reversing exactly k nodes
            for _ in range(k):
                nxt = curr.next 
                curr.next = prev
                prev = curr
                curr = nxt
                
            # Glue
            tail = groupPrev.next
            tail.next = curr
            groupPrev.next = prev
            
            # Shifting the anchor to the end of the newly reversed group
            groupPrev = tail
            
            count -= k
            
        return dummy_node.next
        
        