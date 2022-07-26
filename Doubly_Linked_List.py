class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def __createNode(self, data):
        return Node(data)
    
    def print_list(self):
        current = self.head
        
        while current is not None:
            if(current.next is not None):
                print("Node {}".format(str(current.data)), end=" -> ")
            else:
                print("Node {}".format(str(current.data)))
                
            current = current.next
    
    def append(self):
        print("ha")
        print("ho")
        return None
    
def main():
    
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.print_list()
    
if __name__ == "__main__":
    main()
        
        
