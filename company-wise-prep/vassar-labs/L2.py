class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    def deletion(self, key):
        if self.head is None:
            return
        temp = self.head
        prev = None
        if temp.val == key:
            self.head = temp.next
            if self.head is None:
                self.tail = None
            return
        while temp and temp.val != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        # tail node
        if temp == self.tail:
            self.tail = prev
    def rotate_right(self, k):
        if self.head is None or self.head.next is None:
            return
        l = 1
        temp = self.head
        while temp.next:
            temp = temp.next
            l += 1
        tail = temp
        k = k % l
        if k == 0:
            return
        tail.next = self.head
        steps = l - k - 1
        new_tail = self.head
        for i in range(steps):
            new_tail = new_tail.next
        self.head = new_tail.next
        new_tail.next = None
ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

# ll.display()

# ll.deletion(5)
# ll.insert(6)
ll.display()

ll.rotate_right(5)
ll.display()