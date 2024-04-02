class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def findCycle(head):
    if head == None:
        print('No cycle')
        return
    turtle = rabbit = head
    while(turtle != None and rabbit.next != None):
        turtle = turtle.next
        rabbit = rabbit.next.next
        if turtle == rabbit:
            break
    if turtle != rabbit:
        print('No cycle')
        return
    frnd1 = head
    frnd2 = turtle
    while(frnd1 != frnd2):
        frnd1 = frnd1.next
        frnd2 = frnd2.next
    print(frnd1.value)

def __main__():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n4
    findCycle(head)

__main__()