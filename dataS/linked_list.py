
class LinkedList:
    class Node:
        def __init__(self, key= -1<<30, val = 0):
            self.key = key
            self.val = val
            self.right = None
            self.left = None
            self.isF = False

    def __init__(self):
        self.head = self.Node()
        self.Tail = self.head

    
    def insert(self, k, v):
        temp = self.Node(k, v)
        next = self.head.right
        self.head.right = temp
        temp.right = next
        temp.left = self.head
        if next == None:
            self.Tail = temp
        else:
            next.left = temp
        return temp

    def remove(self, node):
        next = node.right
        prev = node.left

        prev.right = next
        if next == None:
            self.Tail = prev
        else:
            next.left = prev
        del node

    def pop(self):
        if self.Tail != self.head:
            k = self.Tail.key
            self.Tail = self.Tail.left
            del self.Tail.right
            self.Tail.right = None
            return k
    
    def print(self):
        h = self.head
        while h:
            print(h.key, h.val, end= ', ')
            h = h.right
        print()

