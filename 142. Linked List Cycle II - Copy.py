# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # i=9
        # print('tail connects to node index '+`i`)
        if not head:
            return None
        dicts = {head, }
        head = head.next
        while head and head not in dicts:
            dicts.add(head)
            head = head.next
        
        if head:
            return head
        else:
            return None