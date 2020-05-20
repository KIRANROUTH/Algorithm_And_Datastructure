#Binary Search tree
class Node:
    def __init__(self, data):
        self.data = data
        self.lnext = None
        self.rnext = None

class Binarytree:
    def __init__(self, node):
        self.pnode = node
        self.dnode = node
        
    def insert(self, node, data):
        
        if node == None:
            return self.dnode
        #print(data, end = " ")
        
        if data > self.pnode.data and self.pnode.rnext == None:
            self.pnode.rnext = Node(data)
            return self.dnode
        elif data < self.pnode.data and self.pnode.lnext == None:
            self.pnode.lnext = Node(data)
            return self.dnode
        
        if data < node.data and node.lnext == None:
            node.lnext = Node(data)
            return self.dnode
        elif data < node.data and node.lnext != None:
            bt = Binarytree(self.dnode)
            return bt.insert(node.lnext, data)

        if data > node.data and node.rnext == None:
            node.rnext = Node(data)
            return self.dnode
        elif data > node.data and node.rnext != None:
            bt = Binarytree(self.dnode)
            return bt.insert(node.rnext, data)

    le = 0
    def findtp(self, node, data):
        Binarytree.le += 1
        print("Passed: " + str(node.data))
        if node.data == data:
            return "Got at layer: " + str(Binarytree.le)

        if data > node.data:
            bt = Binarytree(self.dnode)
            return bt.findtp(node.rnext, data)

        elif data < node.data:
            bt = Binarytree(self.dnode)
            return bt.findtp(node.lnext, data)


node = Node(0)
bt = Binarytree(node)

import random
val = []
while len(val) != 20:
    a = random.randint(1, 50)
    if a not in val:
        val.append(a)
print(val)

for x in val:
    node = bt.insert(node, x)
bt.findtp(node, val[10])
