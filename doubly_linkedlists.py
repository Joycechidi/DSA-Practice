class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creating a doubly linked list
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully"

    # Inserting a node in a doubly linked list

    # Insert at the beginning of a DLL
    def insertNode(self, nodeValue,location):
        if self.head is None:
            print("The node cannot be inserted!")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
    # Insert at the end of a DLL
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

    # Insert at the middle of a DLL
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    #  Traversal Method in Doubly Linked List
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    #  Reverse Traversal Method in Doubly Linked List
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is no element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search Method in Doubly Linked List
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is no element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"

    # Delete a node from Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is no element in DLL")
        else:
            if location == 0:
                # Delete the first node
                #When we have only one node in the DLL
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                #When more than one node exists in the DLL
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                #If we have only one node in our DLL
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                #Delete the last node
                #If we have more than one node in the DLL
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            #Delete a node from any given location
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

    # Delete entire Doubly Linked List
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")


doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0, 0)
doubyLL.insertNode(2, 1)
doubyLL.insertNode(6, 2)
print([node.value for node in doubyLL])
doubyLL.deleteNode(-1)
# doubyLL.deleteDLL()
print([node.value for node in doubyLL])
