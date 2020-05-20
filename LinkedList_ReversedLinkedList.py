#Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def insert(node, data_):
        node.next = Node(data_)
        return node.next
    def printdata(node):
        return node.next
node_ = Node(None)
val = node_
for x in range(6):
    node_ = Solution.insert(node_, int(x))
node = node_
for x in range(6):
    val = Solution.printdata(val)
    print(val.data)

#Alternative Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self, initnode):
        self.node = initnode
        self.default = self.node
    def insert(self, data):
        self.node.next = Node(data)
        self.node = self.node.next
    def printL(self):
        curr = self.default.next
        while curr != None:
            print(curr.data)
            curr = curr.next
ll = Linked(Node(0))
for x in range(6):
    ll.insert(x)
ll.printL()

#Reversed Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class ReverseLL:
    def __init__(self, initnode):
        self.initnode = initnode
        self.default = initnode
    def insert(self, data):
        while self.initnode.next:
            self.initnode = self.initnode.next
        self.initnode.next = Node(data)
    def printLR(self):
        curr = self.default.next
        while curr != None:
            print(curr.data)
            curr = curr.next
rll = ReverseLL(Node(0))
for x in range(6):
    rll.insert(x)
rll.printLR()
import sys
print(sys.getsizeof(rll))
ll = [x for x in range(6)]
print(sys.getsizeof(ll))
ll = map(int, [x for x in range(6)])
print(sys.getsizeof(ll))        


    


        
