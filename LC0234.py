# Palindrome Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        tail = self.getMid(head)
        mid = tail.next
        tail.next = None
        mid = self.reverse(mid)
        while mid:
            if not head or mid.val != head.val:
                return False
            head = head.next
            mid = mid.next
        return True

    def getMid(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre, head = head, temp
        return pre
