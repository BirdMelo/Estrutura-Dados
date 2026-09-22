class Queue:
    def __init__(self):
        self.items = []
    
    def line_up(self,value):
        self.items.append(value)
    
    def length(self):
        return len(self.items)

    def is_empty(self):
        return self.length() == 0
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.items.pop(0)
    def front(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.items[0]