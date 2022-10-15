from math import fabs
from tempfile import tempdir


class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Bst:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if temp.data == new_node.data:
                return False
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right        
            
    def contains(self, data): 
        temp = self.root
        while (temp is not None):
            if data < temp.data:
                temp = temp.left
            elif data > temp.data:
                temp = temp.right
            else:
                return True
        return False


def main():
    
    bst = Bst()
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    
    print(bst.root.data)
    print(bst.root.left.data)
    print(bst.root.left.right.data)
    print(bst.root.right.data)

    print(bst.contains(3))
    print(bst.contains(1))
    print(bst.contains(2))
    print(bst.contains(5))
    print(bst.contains(4))
    
    
    
    
if __name__ == "__main__":
    main()