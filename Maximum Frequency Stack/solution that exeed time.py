class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.size += 1


    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data


    def peek(self):
        if self.is_empty():
            return None
        return self.top.data


    def is_empty(self):
        return self.top is None


class FreqStack:

    def __init__(self):
        self.levels = Stack()


    def push(self, val: int) -> None:
        frequency = 0
        saving_stacks = Stack()

        while not self.levels.is_empty():
            floor = self.levels.pop()
            if self._contains(floor, val):
                frequency += 1
            saving_stacks.push(floor)

        while not saving_stacks.is_empty():
            self.levels.push(saving_stacks.pop())


        the_freq = frequency + 1
        if self.levels.size < the_freq:
            self.levels.push(Stack())

        for i in range(self.levels.size - the_freq):
            saving_stacks.push(self.levels.pop())

        self.levels.peek().push(val)
        while not saving_stacks.is_empty():
            self.levels.push(saving_stacks.pop())


    def _contains(self, stack, val):
        found = False
        saving_stacks = Stack()
        while not stack.is_empty():
            item = stack.pop()
            saving_stacks.push(item)
            if item == val:
                found = True
        while not saving_stacks.is_empty():
            stack.push(saving_stacks.pop())
        return found


    def pop(self) -> int:
        top_level = self.levels.peek()
        val = top_level.pop()

        if top_level.is_empty():
            self.levels.pop()

        return val




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
