class MinStack:

    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Variable to store the current minimum
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        # If the new value is the new minimum, update min_val
        if val < self.min_val:
            self.min_val = val
        # Push a tuple with the current value and the current minimum
        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        if self.stack:
            # Pop from the main stack
            self.stack.pop()
            # Update min_val to the previous minimum
            if self.stack:
                self.min_val = self.stack[-1][1]
            else:
                self.min_val = float('inf')

    def top(self) -> int:
        if self.stack:
            # Return the top element of the main stack
            return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the current minimum
        return self.min_val

# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2
