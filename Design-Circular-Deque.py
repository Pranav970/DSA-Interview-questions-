class MyCircularDeque(object):

    def __init__(self, k):
       self.k = k
       self.deque = [0]*k
       self.front = 0
       self.rear = 0
       self.size = 0       
        

    def insertFront(self, value):
        if self.isFull():
            return False
        # Update front pointer circularly and insert value
        self.front = (self.front - 1 + self.k) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        # Insert at rear and update rear pointer circularly
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        # Update front pointer circularly
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        # Update rear pointer circularly
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        # The rear pointer points to the next empty position, so we get the last element.
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
