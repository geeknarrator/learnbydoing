class LinkedListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __len__(self):
        currnode = self
        len=0
        while currnode:
            len+=1
            currnode = currnode.next
        return len

    def __str__(self):
        curr = self
        result = []
        while curr is not None:
            result.append(str(curr.val))
            curr = curr.next
        return ' '.join(result)

    def reverse(self, prevnode):
        currnode = self
        nextnode = currnode.next
        while currnode is not None:
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
            nextnode = nextnode.next if nextnode is not None else None
        return prevnode

    def reversePart(self, i, j):
        # i and j are indices
        # within list range.
        if i not in (0, len(self)) or j not in (0, len(self)):
            return self
        prev = self
        count = 0



    def sort(self):
        # sorts the list
        pass


head = LinkedListNode(3, LinkedListNode(4, LinkedListNode(5, LinkedListNode(6, None))))
print(head.reverse(None))
