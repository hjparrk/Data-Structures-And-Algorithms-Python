class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def __createNode(self, data):
        return Node(data)
    
    def print_queue(self):
        
        tmp = self.first
        
        print("First - ",end="")
        for i in range(self.length):
            
            if i == self.length - 1:
                print(tmp.data, end=" ")
            else:
                print(tmp.data, end=" - ")
            
            tmp = tmp.next
        print("Last")