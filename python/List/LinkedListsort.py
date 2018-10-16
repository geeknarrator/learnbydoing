class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def get_mid(head):
    slow = head
    fast = head
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    head = None
    tail = None
    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            if head is None:
                head = head1
                tail = head1
            else:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
                tail.next = None
        else:
            if head is None:
                head = head2
                tail = head2
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
                tail.next = None

    if head1 is not None:
        tail.next = head1
    elif head2 is not None:
        tail.next = head2

    while tail.next is not None:
        tail = tail.next
    return head


def sort(head, end=None, level=0):
    if head is end:
        return head

    if end is not None:
        end.next = None

    mid = get_mid(head)
    head2 = sort(mid.next, end)
    mid.next = None
    head1 = sort(head, mid)
    merged = merge(head1, head2)
    return merged


n = Node(3, Node(1, Node(8, Node(10, Node(-1, Node(9, None))))))
print(sort(n))
