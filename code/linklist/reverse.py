class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createLL()->Node:
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head = n1
    return head

def traverse(head):
    if head == None:
        return
    print(head.value)
    traverse(head.next)

def reverse(head):
    prev = None
    curr = head
    while curr.next != None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return curr


def __main__():
    head = createLL()
    head = reverse(head)
    traverse(head)

__main__()