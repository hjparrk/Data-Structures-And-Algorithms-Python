class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __createNode(self, data):
        return Node(data)
    
    def print_stack(self):
        tmp = self.top
        for i in range(self.size):
            if i == self.size-1:
                print(tmp.data)
            else:   
                print(tmp.data, end=" - ")
            tmp = tmp.next
        print()

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def push(self, data):
        
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
        if not self.isEmpty:
            self.isEmpty = False
        return True
        

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print(stack.getSize())
    print(stack.isEmpty())
    
if __name__ == "__main__":
    main()