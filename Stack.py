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
        
        new_node = self.__createNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
        if not self.isEmpty:
            self.isEmpty = False
        return True
        
    def pop(self):
        
        if self.size == 0 or self.top is None:
            return None
        
        tmp = self.top
        self.top = tmp.next
        tmp.next = None
        self.size -= 1
        return tmp.data
    
    def peek(self):
        
        if self.size == 0 or self.top is None:
            return None
        
        return self.top.data
    
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.push(5)
    stack.print_stack()
    print(stack.peek())
    stack.pop()
    stack.print_stack()
    print(stack.peek())
    print("top: {}".format(stack.top.data))
    print("size: {}".format(stack.getSize()))
    print(stack.isEmpty())
    
if __name__ == "__main__":
    main()