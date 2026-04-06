class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data


    def peek(self):
        if self.is_empty():
            return None
        return self.top.data


    def is_empty(self):
        return self.top is None


class MyQueue:

    def __init__(self):
        self.stack_input = Stack()
        self.stack_output = Stack()


    def push(self, x: int) -> None:
        self.stack_input.push(x)


    def pop(self) -> int:
        self.transfer()
        return self.stack_output.pop()


    def peek(self) -> int:
        self.transfer()
        return self.stack_output.peek()


    def empty(self) -> bool:
        return self.stack_input.is_empty() and self.stack_output.is_empty()


    def transfer(self):
        if self.stack_output.is_empty():
            while not self.stack_input.is_empty():
                data = self.stack_input.pop()
                self.stack_output.push(data)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
