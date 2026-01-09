class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(root):
    curr = root
    while curr:
        print(curr.data, end = " ")
        curr = curr.next
    print()

def insertion_begin(root, data):
    new_node = Node(data)
    if not root:
        new_node.next = root
    return new_node

def insertion_end(root, data):
    new_node = Node(data)
    if not root:
        return new_node
    curr = root
    while curr.next:
        curr = curr.next
    curr.next = new_node
    
def insertion_middle(root, data):
    slow = None
    fast = root
    while fast and fast.next:
        if slow == None:
            slow = root
        else:
            slow = slow.next
        fast = fast.next.next
    new_node = Node(data)
    new_node.next = slow.next
    slow.next = new_node
    
def reverse_linkedlist(root):
    prev = None
    curr = root
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
insertion_middle(ll, 5)
insertion_middle(ll, 6)
print_list(ll)
new_root = reverse_linkedlist(ll)
print_list(new_root)