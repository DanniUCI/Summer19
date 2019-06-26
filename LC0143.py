# Reorder List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        mid = self.getMid(head)
        head2, mid.next = mid.next, None
        head2 = self.reverse(head2)
        return self.merge(head, head2)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def merge(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        while head1 and head2:
            head.next = head1
            head1 = head1.next
            head.next.next = head2
            head2 = head2.next
            head = head.next.next
        if head1:
            head.next = head1
        return dummy.next