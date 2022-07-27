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
        
        print("First ",end="")
        for i in range(self.length):
            
            if i == self.length - 1:
                print(tmp.data, end=" ")
            else:
                print(tmp.data, end=" - ")
            
            tmp = tmp.next
        print("Last")
        
    def enqueue(self, data):
        new_node = self.__createNode(data)
        
        if self.length == 0 or self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
        return True
        
    
def main():

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    

if __name__ == "__main__":
    main()