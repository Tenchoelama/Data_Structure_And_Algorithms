"""
    Python Data Strucures - A Game-based approach
    Building a Stack class in Python 
    
"""
    
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
# if __name__ == "__main__":
    
s = Stack()

print(s.is_empty())
s.push(1)
s.items.extend([2,3,4,5,6])
print(s.pop())
print(s.peek())
print(s.size())
print(s)
    
    

