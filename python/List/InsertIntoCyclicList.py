"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head.next == head:
            node = Node(insertVal)
            head.next = node
            node.next = head
            return head if head.val < node.val else node
        current = head
        next_node = current.next
        node = Node(insertVal)
        while next_node is not head:
            if current.val <= node.val <= next_node.val:
                node.next = next_node
                current.next = node
            elif current.val <= next_node.val <= node.val:
                node.next = next_node.next
                next_node.next = node
            else:
                current = current.next
                next_node = next_node.next

        while head.val > head.next.val:
            head = head.next

        return head

