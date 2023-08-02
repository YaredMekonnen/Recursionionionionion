class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
 
    def getData(self):
        return self.data
 
    def getNext(self):
        return self.next
 
    def setData(self,newdata):
        self.data = newdata
 
    def setNext(self,newnext):
        self.next = newnext
        
    def __repr__(self):
        return str(self.data)
 
 
class UnorderedList:
 
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    #this method is really a prepend - it puts the new node at the beginning
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
            
    def __repr__(self):
        list_representation = ""
        current = self.head #start with the Node at the head
        while current: #this will keep going until current equals None
            list_representation += str(current.getData())+" -> "
            current = current.getNext() #move on to the next Node in the list
        list_representation += "None" #the last one in the list points to None
        return list_representation
    
    def __getitem__(self,index):
        
        if index < 0:
            raise Exception("list index "+str(index)+" is out of range")
        
        current = self.head
        item_counter = 0
        
        while current and item_counter < index:
            
            current = current.getNext()
            item_counter += 1
            
        if current == None:
            raise Exception("list index "+str(index)+" is out of range")
            
        return current.getData()
    def search(self,item):
        current = self.head
        found = False
 
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def index(self, item):
        def index_helper(current, counter):
            if current == None:
                return None
            elif current.getData() == item:
                return counter
            else:
                return index_helper(current.getNext(), counter + 1)
        return index_helper(self.head, 0)
my_list = UnorderedList()
 
my_list = UnorderedList()
 
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
 
print( my_list.index(17) ) #displays 3 because 17 is at index 4 in the list
