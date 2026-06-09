# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Finding the Middle
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Sever and Reverse 
        second = slow.next
        slow.next = None  
        
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # The Alternating Zipper 
        first = head
        second = prev  # 'prev' is the head of the newly reversed second half
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2