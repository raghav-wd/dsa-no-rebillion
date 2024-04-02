class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse(head):
    if head == None:
        return
    print(str(head.value), end="->")
    traverse(head.next)

def insertAt(head, position, value):
    king = head
    newNode = Node(value)
    if position == 0:
        newNode.next = head
        head = newNode
        return head
    index = 0
    while head != None:
        if index == position-1:
            tmp = head.next
            head.next = newNode
            newNode.next = tmp
        index = index + 1
        head = head.next
    return king

def __main__():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    head = n1

    traverse(head)
    head = insertAt(head, 2, 3)
    print()
    traverse(head)

__main__()
