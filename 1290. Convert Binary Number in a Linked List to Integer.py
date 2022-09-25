class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = ''
        while head!=None:
            result += str(head.val)
            head = head.next
        
        result = int(result, 2)
        return result