class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
class btree():
    def __init__(self, value):
        self.root = Node(value)
      
    
    def print_tree(self, node):
        if node:
            self.print_tree(node.left)  # Visit left subtree
            print(node.data)  # Print node data
            self.print_tree(node.right)  # Visit right subtree

        
tree = btree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.root.data)             
print(tree.root.left.data)

# Print the entire tree
tree.print_tree(tree.root)