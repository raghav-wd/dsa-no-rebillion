class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
def createBT():
        val = input('enter value ')
        if val == '-1':
             return
        node = Node(val)
        print('for left node: ' + node.value)
        node.left = createBT()
        print('for right node: ' + node.value)
        node.right = createBT()

createBT()