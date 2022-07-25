# Linked list in Python

# Node class
from os import link


class Node:
    
    # Function to initialise the Node object
    def __init__(self, data):
        self.data = data # Data to store
        self.next = None # A Pointer to the next node

# Linked list class
class LinkedList: 
    
    """
        Function to initialise the LinkedList object
        Takes O(1) time complexity
    """
    def __init__(self):
        self.length = 0 # length of the linked list
        self.head = None # A pointer to the head node of the list
        self.tail = None # A pointer to the tail node of the list

    """
        Private function to create new Node (can only be accessed and called in this LinkedList class)
        Takes O(1) time complexity
    """
    def __createNode(self, data):
        new_node = Node(data)
        return new_node
    
    """
        Function to append a new node to the linked list
        Takes O(1) time complexity as we know the tail node
        Having a pointer only to the head node, takes O(n) to append a new node 
        since it has to iterate all the node to reach the tail
    """
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
        return True
        
    """
        this function does not update the pointer to the tail node,
        it is just to show the logic how the append function works without the pointer to the tail node
        Takes O(n) time complexity
    """
    def append_no_tail(self,data):
        new_node = self.__createNode(data)
        if self.length == 0 or self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1
        return True
        
    """
        Function to prepend a new node to the linked list
        Takes O(1) time complexity
    """    
    def prepend(self,data):
        new_node = self.__createNode(data)

        if self.length == 0 or self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        print("prepend " + str(self.head.data))
        return True
        
    """    
        Function to pop the tail node from the linked list
        Takes O(1) time complexity
        Not knowing the tail node, it has to iterate all nodes to the tail one
        So, it takes O(n) time complexity
    """
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
        return temp.data
     
    """ 
        this function does not update the pointer to the tail node,
        it is just to show the logic how the pop function works without the pointer to the tail node
        Takes O(n) time complexity    
    """           
    def pop_no_tail(self):
        if self.length == 0 or self.head is None:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        print("pop " + str(temp.data))
        if self.length == 1 or prev is temp:
            self.head = None
        else:
            prev.next = None
        self.length -= 1    
        return temp.data
        
    """
        Function to pop the head node from the linked list
        Takes O(1) time complexity
    """    
    def pop_first(self):
        if self.length == 0 or self.head is None or self.tail is None:
            return None
        print("pop first " + str(self.head.data))
        
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
            
        return temp.data
    
    """
        Function to get the node according to the given index in the linked list
        Takes O(n) time complexity
    """          
    def get(self, index):
        if self.length == 0:
            return False
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        print("get " + str(temp.data))
        return temp
    
    """
        Function to set (update) the node's data according to the given index and data in the linked list
        Takes O(n) time complexity as get function itself takes O(n) time 
        despite the fact that changing data of the node takes only O(1) time
    """   
    def set(self, index, data):
        if self.length == 0:
            return False
        temp = self.get(index)
        if temp:
            temp.data = data
            return True    
        else:
            return False
    
    """
        Function to insert the node according to the given index and data into the linked list
        Takes O(n) time complexity
    """      
    def insert(self, index, data):
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        
        new_node = self.__createNode(data)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    """
        Function to print all node's data iteratively from the head node to the tail
        Takes O(n) time complexity, iterating through the whole list
    """        
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
    linked_list.prepend(5)
    linked_list.prepend(10)
    linked_list.pop()
    linked_list.pop()
    linked_list.pop_first()
    linked_list.get(0)
    linked_list.set(1,"Test set function")
    linked_list.insert(0, "Woah")
    linked_list.insert(2, 7)
    linked_list.insert(linked_list.length, 10)
    # linked_list.append_no_tail(5)
    # linked_list.pop_no_tail()
    linked_list.print_list()
    
    print(linked_list.length)
    
if __name__=="__main__":
    
    # execute the main function here
    main()
    
    
    
    

         