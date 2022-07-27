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
    
    def append(self, data):
        
        new_node = self.__createNode(data)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1  
        return True

    def prepend(self, data):
        
        new_node = self.__createNode(data)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return True

    def pop(self):
        
        if self.length == 0:
            return None
        
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
            
        self.length -= 1
        return current
    
    def pop_first(self):

        if self.length == 0:
            return None
        
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            current.next = None
            
        self.length -= 1
        return current 

    def get(self, index):
        
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, data):
        
        if index < 0 or index >= self.length:
            return False
        current = self.get(index)
        if current:
            current.data = data
            return True
        else:
            return False
        
    def insert(self, index, data):
        
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(data)
        elif index == self.length:
            return self.append(data)
        else:
            new_node = self.__createNode(data)
            prev = self.get(index -1)
            next = prev.next
            
            prev.next = new_node
            new_node.prev = prev
            
            next.prev = new_node
            new_node.next = next
            
            return True
            

            
            
            
    
        
def main():
    
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    # doubly_linked_list.pop()
    # doubly_linked_list.pop_first()
    doubly_linked_list.print_list()
    doubly_linked_list.set(0, 13)
    doubly_linked_list.prepend(11)
    doubly_linked_list.insert(2, "Seoul")
    doubly_linked_list.print_list()
    
    print("\n{}".format(doubly_linked_list.length))
    
if __name__ == "__main__":
    main()
        
        
