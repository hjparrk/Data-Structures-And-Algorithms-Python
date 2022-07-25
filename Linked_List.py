# Linked list in Python

# Node class
class Node:
    
    # Function to initialise the Node object
    def __init__(self, data):
        self.data = data # Data to store
        self.next = None # A Pointer to the next node

# Linked list class
class LinkedList: 
    
    # Function to initialise the LinkedList object
    # Takes O(1) time complexity
    def __init__(self):
        self.length = 0 # length of the linked list
        self.head = None # A pointer to the head node of the list
        self.tail = None # A pointer to the tail node of the list

    # Private function to create new Node (can only be accessed and called in this LinkedList class)
     # Takes O(1) time complexity
    def __createNode(self, data):
        new_node = Node(data)
        return new_node
    
    # Function to append a new node to the linked list
    # Takes O(1) time complexity as we know the tail node
    # Having a pointer only to the head node, takes O(n) to append a new node 
    # since it has to iterate all the node to reach the tail
    def append(self, data):
        new_node = self.__createNode(data)
        if self.length == 0 or self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
        print("append " + str(self.tail.data))
    
    # Function to pop the tail node from the linked list
    # Takes O(1) time complexity
    # Not knowing the tail node, it has to iterate all nodes to the tail one
    # So, it takes O(n) time complexity
    def pop(self):
        if self.length == 0 or self.head is None or self.tail is None:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        print("pop " + str(self.tail.data))
        if self.length == 1 or prev is temp:
            self.head = None
            self.tail = None
        else:
            self.tail = prev
            self.tail.next = None
        self.length -= 1            
        
        
        
        
    # Function to print all node's data iteratively from the head node to the tail
    # Takes O(n) time complexity, iterating through the whole list
    def print_list(self):
        # temporary pointer node (cursor)
        temp = self.head
        print()
        # Iterate the whole list
        while temp is not None:
            # if temp.next exists, then print " -> "
            if(temp.next is not None):
                print("Node " + str(temp.data) ,end=" -> ")
            # Otherwise, print nothing at the end as temp.next is None
            else:
                print("Node " + str(temp.data) ,end="")
            # forward the temp to the next node
            temp = temp.next
        print()
    

# main function
def main():
    
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.pop()
    linked_list.pop()
    linked_list.print_list()
    
    print(linked_list.length)
    
if __name__=="__main__":
    
    # execute the main function here
    main()
    
    
    
    

         