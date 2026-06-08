# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together
#  the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head_lst1=list1
        head_lst2=list2
        dummy_lst=ListNode(0)
        tail=dummy_lst
        while head_lst1 and head_lst2:
            if head_lst1.val>head_lst2.val:
                tail.next=head_lst2
                head_lst2=head_lst2.next
            else:
                tail.next=head_lst1
                head_lst1=head_lst1.next
            tail=tail.next
        if head_lst1 is None and head_lst2:
            tail.next=head_lst2
        else:
            tail.next=head_lst1
        return dummy_lst.next


        