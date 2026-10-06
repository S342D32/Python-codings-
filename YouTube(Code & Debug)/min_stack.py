class Min_Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    def get_mini(self):
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]

    def top(self):
        if len(self.items) == 0:
            return 0
        return self.items[-1][0]

    def pop(self):
        if len(self.items) == 0:
            return 0
        return self.items.pop()