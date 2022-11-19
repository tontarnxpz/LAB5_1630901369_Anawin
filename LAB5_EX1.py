class Node:
    def __init__(self, Value):
        self.Value = Value
        self.NextVal = ""
        self.PrevVal = ""

class List:
    def __init__(self):
        self.header = None
        self.tail = None

    def add(self, Value):
        if self.header is None:
            self.header = Node(Value)
            self.tail = self.header
        elif self.header is not None:
            node = Node(Value)
            self.tail.NextVal = node
            node.PrevVal = self.tail
            self.tail = node
        else:
            print("Error")

    def print_list(self):
        node = self.header
        while node is not None:
            if node == self.tail:
                print(node.Value)
                break
            else:
                print(node.Value,"<-> ",end="")
                node = node.NextVal

header = List()
header.add(1)
header.add(2)
header.add(3)
header.add(4)
header.print_list()