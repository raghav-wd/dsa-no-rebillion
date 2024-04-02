class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createLL()-> Node:
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n1

def reverseLL(head):
    prev = None
    curr = head

    while curr != None:
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead

    return prev


def traverseLL(head):
    if head == None: return
    print(head.value)
    traverseLL(head.next)

def getMiddle(head):
    turtle = rabbit = head
    while rabbit.next != None and rabbit.next.next != None:
        turtle = turtle.next
        rabbit = rabbit.next.next
    return turtle


head = createLL()
# traverseLL(head)
# head = reverseLL(head)
# traverseLL(head)
mid = getMiddle(head)
revLL = reverseLL(mid)
traverseLL(head)
traverseLL(revLL)

