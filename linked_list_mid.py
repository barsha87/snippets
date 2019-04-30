
# Node Class


class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
import math
def findMid(head):
    node = head
    mid_node = head
    count = 1
    mid_count = 1
    while node:
        node = node.next
        count += 1
        if mid_count < math.ceil(count/2):
            mid_node = mid_node.next
            mid_count += 1
    return mid_node

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)

"""
2
5
1 2 3 4 5
6
2 4 6 7 5 1


output
3
7
"""