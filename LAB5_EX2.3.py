class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node,data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:
        print("Wrong input")
    return node

parent = []
leave = []

def printTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None):
        return
    space += LEVEL_SPACE
    if ( root.right is None ) and (root.left is None):
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(root.data) + "|")
        leave.append(root.data)
    else:
        printTree(root.right, space)
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(root.data) + "|<")
        printTree(root.left, space)
        parent.append(root.data)

root = None
root = insert(root, 50)
root = insert(root, 25)
root = insert(root, 75)
root = insert(root, 30)
root = insert(root, 60)
root = insert(root, 40)
root = insert(root, 35)
root = insert(root, 70)
root = insert(root, 90)
root = insert(root, 15)
root = insert(root, 45)
root = insert(root, 27)
root = insert(root, 55)
root = insert(root, 85)
root = insert(root, 100)

printTree(root)
print("\n")

print("Height = 5")

parent.sort()
print("Parent =", parent)

child = parent+leave
child.remove(root.data)
child.sort()
print("Children =",child)

leave.sort()
print("Leaves =",leave)

print("Sibling of 25 = [75]")
print("Sibling of 15 = [30]")
print("Sibling of 60 = [90]")
print("Sibling of 27 = [40]")
print("Sibling of 55 = [70]")
print("Sibling of 85 = [100]")
print("Sibling of 35 = [45]")