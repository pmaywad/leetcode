'''
641. Design Circular Deque
Design your implementation of the circular double-ended queue (deque).
'''

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = [None]*k
        self.rear = -1
        self.front = -1

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if self.front == -1:
            self.rear = self.front = self.size - 1
            self.queue[self.front] = value
            
        else:
            if self.front == 0:
                self.front = self.size -1
            else:
                self.front = (self.front - 1)
            self.queue[self.front] = value
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        if self.rear == self.front:
            self.queue[self.front] = None
            self.rear = self.front = -1
            
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.queue[self.rear] = None
            self.rear = self.front = -1
            
        else:
            self.queue[self.rear] = None
            if self.rear == 0:
                self.rear = self.size - 1
            else:
                self.rear = self.rear - 1
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        
        return self.queue[self.front]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        
        return self.queue[self.rear]       

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return True
        
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if (self.rear + 1)% self.size == self.front:
            return True
        
        return False
        
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
