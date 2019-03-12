class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[0]
        self.items.remove(item)
        return item

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    @staticmethod
    def to_stack(items):
        stack = Stack()
        for item in items:
            stack.push(item)
        return stack