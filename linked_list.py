class Node():
    def __init__(self,data):
        self.data= data
        self.link = None

def insert(start, data):
    node = start
    while node.link:
        node = node.link
    avail = Node(data)
    avail.link = None
    node.link = avail

def display(start):
    node = start
    while node:
        print(node.data)
        node = node.link
    print

def reverse(start):
    node = start
    prev = None
    while node:
        new_start = node.link
        node.link = prev
        prev = node
        node = new_start
    return prev

start = Node(3)
insert(start, 5)
insert(start, 17)
insert(start, 43)
insert(start, 10)
display(start)
start=reverse(start)
display(start)