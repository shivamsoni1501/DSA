import copy

# node class for link List
class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def add_edge(self, b):
        if self.left == None:
            self.left = Node(b)
            return self.left
        else:
            self.right = Node(b)
            return self.right

# Linked Tree to Flat linked list
def tree_to_preOrder(root):
    linkList = copy.deepcopy(root)
    head = linkList
    while head:
        if head.left:
            pred = head.left
            while pred.right:
                pred = pred.right
            pred.right = head.right
            head.right = head.left
            head.left = None
        head = head.right
    return linkList

# Linked Tree to Flat linked list
def tree_to_inOrder(root):
    newRoot = copy.deepcopy(root)
    lasthead = Node(0)
    ans = lasthead
    lasthead.right = newRoot #newRoot.left if newRoot.left else newRoot
    head = newRoot
    while head:
        if head.left:
            left = head.left
            pre = head.left
            # head.left = None
            while pre.right:
                pre = pre.right
            lasthead.right = left
            pre.right = head
            head.left = None
            head = left
        else:
            lasthead = head
            head = head.right
    return ans.right

# Linked Tree to Flat linked list
def tree_to_postOrder(root):
    newRoot = copy.deepcopy(root)
    ans = newRoot.left if newRoot.left else newRoot.right if newRoot.right else newRoot
    head = newRoot
    while head:
        left = head.left
        right = head.right
        if left:
            head.left = None
            head.right = None
            temp = left
            while temp.right:
                temp = temp.right
            temp.right = right
            
            temp = head.right
            head = left
        else:
            head = head.right
    return ans

from collections import deque

def tree_to_levelOrder(root):
    newRoot = copy.deepcopy(root)
    prev = newRoot
    q = deque([newRoot])
    # q.append(newRoot.left)
    # q.append(newRoot.right)
    while q:
        cur = q.popleft()
        if cur:
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

            cur.left = None
            cur.right = q[0] if q else None
    return newRoot

n = Node(4)
l1 = Node(2)
r1 = Node(6)
l2 = Node(1)
r2 = Node(3)
l3 = Node(5)
r3 = Node(7)
n.left = l1
n.right = r1
l1.left = l2
l1.right = r2
r1.left = l3
r1.right = r3

k = tree_to_levelOrder(n)
print(k)
while k:
    print(k.val)
    k = k.right