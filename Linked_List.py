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
    def __init__(self, data):
        init_node = self.__createNode(data) # create an initial node
        self.length = 1 # length of the linked list
        self.head = init_node # A pointer to the head node of the list
        self.tail = init_node # A pointer to the tail node of the list

    # Private function to create new Node (can only be accessed and called in this LinkedList class)
     # Takes O(1) time complexity
    def __createNode(self, data):
        new_node = Node(data)
        return new_node
    
    # Function to append a new node to the linked list
    # Takes O(1) time complexity as we know the tail node
    # Having a pointer to the head node, takes O(n) to append a new node 
    # since it has to iterate all the node to reach the tail
    def append(self, data):
        new_node = self.__createNode(data)
        self.tail.next = new_node
        self.tail = new_node
    
    # Function to print all node's data iteratively from the head node to the tail
    # Takes O(n) time complexity, iterating through the whole list
    def print_list(self):
        # cursor node
        cursor = self.head
        print()
        # Iterate the whole list
        while cursor is not None:
            # if cursor.next exists, then print " -> "
            if(cursor.next is not None):
                print("Node " + str(cursor.data) ,end=" -> ")
            # Otherwise, print nothing at the end as cursor.next is None
            else:
                print("Node " + str(cursor.data) ,end="")
            # forward the cursor to the next node
            cursor = cursor.next
        print()
    
    def pop(self):
        return None
        

# main function
def main():
    
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.print_list()
    
if __name__=="__main__":
    
    # execute the main function here
    main()
    
    
    
    

         