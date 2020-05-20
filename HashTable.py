#Hash table
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.hash = None

class Hasht:
    def __init__(self, node):
        self.pnode = node
        self.dnode = node
    def insertn(self, data):
        curr = self.pnode
        while curr.next != None:
            curr = curr.next
        curr.next = Node(data)
        return self.dnode
    def inserth(self, posdata, data):
        curr = self.pnode
        while curr.next != None:
            if curr.data == posdata:
                has = curr
                while has.hash != None:
                    has = has.hash
                has.hash = Node(data)
                break
            curr = curr.next
        if curr.next == None:
            print("Given position data in not in linked list.")
        return self.dnode
    def shown(self):
        curr = self.pnode
        while curr.next != None:
            print(curr.data, end = " ")
            curr = curr.next
        print()
        return self.dnode
    def showh(self, posdata):
        curr = self.pnode
        while curr.next != None:
            if curr.data == posdata:
                has = curr
                while has.hash != None:
                    print(has.data, end = " ")
                    has = has.hash
            curr = curr.next
        print()
        return self.dnode
    def showallh(self):
        curr = self.pnode
        while curr.next != None:
            has = curr
            print("At " + str(curr.data) + " -> ", end = " ")
            while has.hash != None:
                print(has.data, end = " ")
                has = has.hash
            curr= curr.next
            print()
        return self.dnode

node = Node(0)
has = Hasht(node)
for x in range(11):
    val = has.insertn(x)

#Change the value and run again and see the difference
value = 5

for x in range(20, 25):
    val = has.inserth(value, x)
print("Shows the main linked list: ", end = " ")
has.shown()
print("Hash data: ", end = " ")
has.showh(value)
print("Show availability of hash: ")
has.showallh()
