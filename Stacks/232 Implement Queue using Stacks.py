# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should
#  support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop 
# from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack 
# using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
class MyQueue(object):
    def __init__(self):
        self.Inbox = []
        self.Outbox = []

    def push(self, x):
        self.Inbox.append(x)

    def peek(self):
        # peek does ALL the heavy lifting and pouring
        if not self.Outbox:
            while self.Inbox:
                self.Outbox.append(self.Inbox.pop())
        return self.Outbox[-1]

    def pop(self):
        # pop just triggers peek to do the pouring, then removes the item!
        self.peek()
        return self.Outbox.pop()

    def empty(self):
        return not self.Inbox and not self.Outbox
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()