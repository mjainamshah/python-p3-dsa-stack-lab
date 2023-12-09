class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack Overflow: Cannot add more items.")
        pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack Underflow: No items to pop.")
        pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("The stack is empty.")
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        for idx in range(len(self.items) - 1, -1, -1):
            if self.items[idx] == target:
                return len(self.items) - idx - 1
        return -1
        pass
