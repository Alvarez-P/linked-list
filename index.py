# Creamos la clase node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase LinkedList
class LinkedList(object):
    def __init__(self, node = None):
        """Se asigna como None como Nodo inicial y final, se define el tamaño de la lista en cero"""
        self.__last = self.__head = node 
        self.__length = 0

    def getLength(self):
        """Devuelve el tamaño de la lista"""
        return self.__length
    
    def getLastNode(self):
        """Devuelve el ultimo dato de la lista"""
        return {"last: " + str(self.__last.data)}

    def addAtFront(self, d):
        """Agrega un nodo al inicio de la lista enlazada"""
        self.__head = Node(data = d, next=self.__head)
        self.__length += 1
        if self.__last == None:
            self.__last = self.__head
            return True
        
    def addAtEnd(self, data):
        """Agrega un nodo al final de la lista enlazada"""
        if not self.__head:
            self.__last = self.__head = Node(data=data)
            return
        curr = self.__head
        while curr.next:
            curr = curr.next
        self.__last = curr.next = Node(data=data)

    def deleteNode(self, d):
        """Se elimina el nodo que tenga el dato d"""
        currentNode = self.__head
        prevNode = None

        while currentNode:
            if currentNode.data == d:
                if prevNode:
                    # Se asigna al apuntador proximo del nodo anterior, al proximo de nodo actual.
                    prevNode.next = currentNode.next
                else:
                    self.__head = currentNode.next
                # En cualquiera de los dos casos se decrementa el tamaño de la lista.
                self.__length -= 1
                return True
            else:
                prevNode = currentNode
                currentNode = currentNode.next

    def find(self,d):
        """Se busca d en la lista enlazada, si existe devuelve d, si no devuelve None"""
        currentNode = self.__head
        count = 0
        while currentNode:
            if currentNode.data == d:
                return { "data": currentNode.data, "position": count }
            else:
                currentNode = currentNode.next
            count+=1
        #Si no se encuentra devuelve None.
        return None 

    def printList(self):
        node = self.__head
        while node != None:
            print({"data: " + str(self.__last.data)})
            node = node.next

if __name__ == "__main__":
    # Instancia de la clase
    linkedList = LinkedList()

    # Valores
    linkedList.addAtEnd(7)
    linkedList.addAtFront(5)
    linkedList.addAtEnd(8)
    linkedList.addAtEnd(9)
    linkedList.addAtEnd(3)
    linkedList.addAtFront(10)

    # Métodos
    print(linkedList.find(3))
    print(linkedList.getLastNode())
    linkedList.printList()

