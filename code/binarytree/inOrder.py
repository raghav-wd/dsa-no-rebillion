class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createBT():
    value = input("Enter value")
    if value == '-1':
        return 
    node = Node(value)
    print('Enter left node for ' + node.value)
    node.left = createBT()
    print('Enter right node for ' + node.value)
    node.right = createBT()
    return node

def inOrder(node):
    if node == None: return
    inOrder(node.left)
    print(node.value)
    inOrder(node.right)

# def createBT():
#     n1 = Node(5)
#     n1.left = Node(3)
#     n1.right = Node(7)
#     n1.left.left = Node(1)
#     n1.left.left.left = Node(0)
#     return n1

node = createBT()
inOrder(node)


