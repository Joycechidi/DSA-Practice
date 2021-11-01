class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    #Create of circular single linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "CSLL has been created!"

    #Insert new node to circular singly linked list
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            #insert node to the beginning of the circular singly linked ist
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            #insert node to the end of the linked list
            elif location == -1:
                newNode.next == self.tail.next
                self.tail.next = newNode
                self.til = newNode

            #insert node to any location in the middle of the linked list
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been inserted successfully in the right location"

    # Traversal of a node in circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            print("There is no element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Search for a node in circular singly linked list
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is no node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "No node exists in this CSLL"

    #Delete a node from circular singly linked list
    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the CSLL")
        else:
            #Deleting first node
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                # Deleting a node if we have more than one node in the list
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            # Delete an element from the end of the list
            elif location == 1:
                if self.head == self.tail:
                    if self.head == self.tail:
                        self.head.next = None
                        self.head = None
                        self.tail = None
                    # When we have more than one element and we want to delete the lat node
                    else:
                        node = self.head
                        while node is not None:
                            if node.next == self.tail:
                                break
                            node = node.next
                        node.next = self.head
                        self.tail = node
            # Deleting element from the middle of the linked list
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        #Delete entire circular singly linked list
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
# circularSLL.traversalCSLL()

print([node.value for node in circularSLL])
circularSLL.deleteNode(0)
print([node.value for node in circularSLL])
print(circularSLL.searchCSLL(2))
# circularSLL = CircularSinglyLinkedList()

print([node.value for node in circularSLL])