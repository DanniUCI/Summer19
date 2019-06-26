# Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # iterater
    def swapPairs_iterater(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next, pre = head, dummy
        while pre.next and pre.next.next:
            node1, node2 = pre.next, pre.next.next
            node1.next, node2.next, pre.next = node2.next, node1, node2
            pre = node1
        return dummy.next

    # recursive
    def swapPairs_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = head.next
        temp = head.next.next
        head.next.next = head
        head.next = self.swapPairs(temp)
        return res
