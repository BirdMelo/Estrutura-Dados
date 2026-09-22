class Stack:
    def __init__(self):
        self.items = []
    
    def to_stack(self, value):
        self.items.append(value)

    def length(self):
        return len(self.items)
    
    def is_empty(self):
        return self.length() == 0
    
    def straighten_out(self):
        if self.is_empty():
            raise IndexError("pilha vazia")
        return self.items.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError("pilha vazia")
        return self.items[-1]
    
    