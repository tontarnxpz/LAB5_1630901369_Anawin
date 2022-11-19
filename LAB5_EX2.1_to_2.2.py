class List:
    def __init__(self , data = 0):
        self.data = data

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def balance(self,head : List) -> Node:
        def helper(l,r):
            if l > r:
                return None

            mid = (l+r) // 2
            root = Node(head[mid])
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            return root

        return helper(0,len(head)-1)

def inorder(root):
    inorderArr = []

    if root.left:
        leftIn = inorder(root.left)
        inorderArr.extend(leftIn)

    inorderArr.append(root.data)

    if root.right:
        rightIn = inorder(root.right)
        inorderArr.extend(rightIn)

    return inorderArr

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

def deleteNode(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)
        return root

    elif (data> root.data):
        root.right = deleteNode(root.right, data)
        return root

    if root.left is None and root.right is None:
        return None

    if root.left is None:
        temp = root.right
        return temp

    elif root.right is None:
        temp = root.left
        return temp

    return root


def printTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None):
        return
    space += LEVEL_SPACE
    printTree(root.right, space)
    for i in range(LEVEL_SPACE, space):
        print(end = " ")
    print("|" + str(root.data) + "|<")
    printTree(root.left, space)

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

rr = solution()

if __name__ == "__main__":
    m = 0
    while(True):
        inorderArr = inorder(root)
        print("\n",inorderArr)
        print("Please enter number 1-4")
        enter = int(input("1 for Push\n2 for Delete\n3 to print BinaryTree\n4 to exit\n"))
        if enter <= 4 and enter >= 0 :
            if(enter == 1):
                item = input("Enter number to PUSH in BinaryTree\n")
                root = insert(root, int(item))

            if(enter == 2):
                item2 = input("Enter number to DELETE in BinaryTree\n")
                root = deleteNode(root, int(item2))

            if(enter == 3):
                printTree(root)

        if(enter == 4):
            break
        elif (enter > 4) and (enter < 0):
            print("Wrong input!!")