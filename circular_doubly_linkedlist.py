class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __iter__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Create Circular Doubly Linked List
    def createCircularDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The Circular Doubly Linkdlist is successfully created"

    def insertCDLL(self, value, location):

        if self.head is None:
            print("There is no node in the linked list")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return " The node has been successfully inserted"

    # Reverse a Circular Doubly Linked List
    def reverseCDLL(self):
        if self.head is None:
            print("Nothing to reverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    #Traverse through a Circular Doubly Linked list
    def traversalCircularDLL(self):
        if self.head is None:
            print("Nothing to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Search for a node in Circular Doubly LinkedList

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value doesnot exist in CDLL"
                tempNode = tempNode.next


    #Delete a node from Circular Doubly LinkedList
    #Case 1: Delete from beginning of the LinkedList
    def deleteNode(self, location):
        if self.head is None:
            return "No node exists here"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
        # Delete last node from Circular DLL
            #Case 1: When only one node exists in the Linkedlist
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                #Case 2: When there are more than one node in the CDLL
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            # Delete from the middle of the CDLL
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

    # Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")
circularCDLL = CircularDoublyLinkedList()
circularCDLL.createCircularDLL(5)
circularCDLL.insertCDLL(0, 0)
circularCDLL.insertCDLL(1, 1)
circularCDLL.insertCDLL(2, 2)
circularCDLL.insertCDLL(3, 3)
circularCDLL.insertCDLL(4, 4)
print([node.value for node in circularCDLL])
circularCDLL.reverseCDLL()
circularCDLL.deleteCDLL()
print([node.value for node in circularCDLL])
