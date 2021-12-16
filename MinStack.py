class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.input_stack = []
        self.min_value = sys.maxsize

    def push(self, val):
        self.input_stack.append(val)

        if self.min_value > val:
            self.min_stack.append(val)
            self.min_value = val
        else:
            self.min_stack.append(self.min_value)

    def pop(self):
        self.input_stack.pop()
        self.min_stack.pop()
        if len(self.input_stack) == 0:
            self.min_value = sys.maxsize
        else:
            self.min_value = self.min_stack.__getitem__(len(self.min_stack) - 1)

    def top(self):
        return self.input_stack.__getitem__(len(self.input_stack) - 1)

    def getMin(self):
        return self.min_stack.__getitem__(len(self.min_stack) - 1)