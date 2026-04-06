class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def add(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def pop(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return data


    def peek(self):
        if self.is_empty():
            return None
        return self.front.data


    def is_empty(self):
        return self.front is None



class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue2.add(x)
        while not self.queue1.is_empty():
            data = self.queue1.pop()
            self.queue2.add(data)

        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        return self.queue1.pop()


    def top(self) -> int:
        return self.queue1.peek()


    def empty(self) -> bool:
        return self.queue1.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
