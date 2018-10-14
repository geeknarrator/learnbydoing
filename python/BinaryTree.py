class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.val, end =" ")

    def preorder(self):
        if self:
           print(self.val, end=" ")
           if self.left:
              self.left.preorder()
           if self.right:
              self.right.preorder()

    def inorder(self):
        if self:
           if self.left:
              self.left.inorder()

           print(self.val, end=" ")

           if self.right:
              self.right.inorder()


btree = Node(2,
                   Node(3,
                        Node(4, None, None),
                        Node(5,
                             Node(1, None,
                                  Node(0, None, None)), None)),
             Node(10, None, None))
btree.inorder()
print("\n")
btree.preorder()
print("\n")
btree.postorder()

