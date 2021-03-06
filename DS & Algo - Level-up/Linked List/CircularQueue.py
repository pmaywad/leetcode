"""
622. Design Circular Queue
"""



class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = [None]*k
        self.front = self.rear = -1
        

    def enQueue(self, value):
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

    def deQueue(self):
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

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        
        return self.queue[self.front]

    def Rear(self):
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
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
