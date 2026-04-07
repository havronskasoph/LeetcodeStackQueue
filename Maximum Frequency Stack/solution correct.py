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
        self.frequency_dict = {}
        self.levels_dict = {}
        self.max_freq = 0


    def push(self, val: int) -> None:
        f = self.frequency_dict.get(val, 0) + 1
        self.frequency_dict[val] = f

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.levels_dict:
            self.levels_dict[f] = Stack()

        self.levels_dict[f].push(val)


    def pop(self) -> int:
        top_level_stack = self.levels_dict[self.max_freq]
        val = top_level_stack.pop()
        self.frequency_dict[val] -= 1

        if top_level_stack.is_empty():
            self.max_freq -= 1
        return val






# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
