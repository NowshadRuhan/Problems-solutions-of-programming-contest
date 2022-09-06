# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print(head)
        if head == None:
            return None
        
        # define head list to first list, it just define the address of value. that means here first.val is 1 means it showing head.val, which is 1.
        first = head
        while first.next:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next
            
        # print(first)
        return head
