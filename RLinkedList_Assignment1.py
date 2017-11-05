class RecursionLinkedList(object):
    UNDEF = '\x00'

    def __init__(self):
        """
        :param index:
        :return:
        """
        self.head = None

    def _link_first(self, element):
        #connect newly created node the beginning of the list
        if(self != None):
            self.head = Node(element, self.head)
        else:
            self.head = Node(element, None)

    def _link_last(self, element, node):
        """
        :rtype: Node
        :type node: Node
        :type element: char
        """
        #assignment(1) connect given node the next of the last linked node
        if (node.next == None): #create next node
            node.next = Node(element, None)
        else:#visit next node
            self._link_last(element,node.next)

    def _link_next(self, element, pred):
        """
        :type element: Char
        :type pred: Node
        :param element:
        :param pred:
        :return:
        """
        next = pred.next
        """:type: Node"""
        pred.next = Node(element, next)

    def _unlinkt_first(self):
        #unlinke first node of list
        x = self.head
        """:type : Node"""
        element = x.element
        self.head = x.next
        x.item = self.UNDEF
        return element

    def _unlink_next(self, pred):
        """
        :type pred: Node
        :param pred:
        :return:
        """
        x=pred.next
        """:type: Node"""
        next=x.next
        element=x.element
        x.element=self.UNDEF
        pred.next=next
        return element


    def _get_node(self, index, x):
        """
        :type index:int
        :type x:Node
        :param index:
        :param x:
        :return:
        """
        #assignment(2) Get nth(index) node
        if (index == 0):#return current node
           return x 
        elif (index > 0):#return result of call _get_node
           return self._get_node(index-1,x.next)
    def get_node(self, index):
        return self._get_node(index, self.head)

    def __len__(self):
        if self.head==None:return 0
        return len(self.head)

    def add(self,  element, index=None):
        if index is None:
            if self.head is None: self._link_first(element)
            else: self._link_last(element, self.head)
            return

        if index<0 or index>len(self):
            print "ERROR"
        elif index==0:
            self._link_first(element)
        else:
            self._link_next(index, element)

    def remove(self, index):
        if index<0 or index>len(self):
            print "ERROR"
        elif(index==0):
            return self._unlinkt_first()
        else: return self._unlink_next(self._get_node(index-1, self.head))


    def __str__(self):
        if self.head is None: return "List is null"
        return str(self.head)

    def _reverse(self, x, pred):
        """
        :type x: Node
        :type pred: Node
        :param x:
        :return:
        """
        #Bonus Assignment
        #Fill out, Use recursion
	
	if x is None :
		self.head = pred
		return x 
	else :
		self._reverse(x.next,x)
		x.next = pred

    def reverse(self):
        self._reverse(self.head, None)


class Node(object):
    """
    :type element:char
    :type next: Node
    """

    def __init__(self, element, next):
        """
        :type element : char
        :type next : Node
        """
        self.element = element
        self.next = next
    def __str__(self):
        #assignment(3)
        if self.next is None: #Return string of self.element
		return str(self.element)
        else:
        #Return self.element and string of next
 		return self.element + " " +str(self.next) 

    def __len__(self):
        #assignment(4) Return size of entire node
	if self.next is None :
		return 1
	else :
		return 1 + len(self.next)

def Test_RecursionLinkedList():
    INPUT=['a', 'b', 'c', 'd', 'e']
    test_RLL=RecursionLinkedList()
    for i in INPUT:
        test_RLL.add(i)
    print str(test_RLL)
    print "List size is "+str(len(test_RLL))
    test_RLL.add('z', 0)
    print "List size is "+str(len(test_RLL))
    print str(test_RLL)
    print test_RLL.get_node(4).element

    print test_RLL.remove(0)
    print str(test_RLL)
    test_RLL.reverse()
    print str(test_RLL)

Test_RecursionLinkedList()

