# Delete Node in a Linked List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(4)
    node1 = ListNode(5)
    node2 = ListNode(1)
    node3 = ListNode(9)
    head.next = node1
    node1.next = node2
    node2.next = node3
    head = sol.deleteNode(node1)
