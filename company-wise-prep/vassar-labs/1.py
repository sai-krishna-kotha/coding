#implement stacks and queue using arrays
class Stack:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.arr[self.top]

    def print_stack(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(self.arr[:self.top+1])


class Queue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def front_val(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def print_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        idx = self.front
        elements = []
        for _ in range(self.size):
            elements.append(self.arr[idx])
            idx = (idx + 1) % self.capacity
        
        print(elements)
