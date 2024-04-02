class Node:
    def __init__(self, value) -> None:
        self.left = self.right = None
        self.value = value

def createNode():
    val = int(input("Enter node: "))
    if val != -1:
        node = Node(val)
    else: return None
    print('Enter left node for ' + str(val))
    node.left = createNode()
    print('Enter right node for ' + str(val))
    node.right = createNode() 
    return node

def __main__():
    createNode()

__main__()