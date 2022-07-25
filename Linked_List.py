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
    def __init__(self, data):
        
        init_node = Node(data) # create an initial node
        self.length = 1 # length of the linked list
        self.head = init_node # A pointer to the head node of the list
        self.tail = init_node # A pointer to the tail node of the list

    # Function to create new Node
    def createNode(self, data):
        new_node = Node(data)
    


# main function
def main():
    linked_list = LinkedList(1)
    
if __name__=="__main__":
    main()
    
    
    
    

         