class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []     # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                  # new item stored at end of list

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()               # remove last item from list

    if __name__ == '__main__':

        from array_stack import ArrayStack
        s = ArrayStack()

        # question 3 of take home exam
        s.push(3)    # bottom
        s.push(2)    # middle
        s.push(1)    # top

        x = s.pop()
        if x < s.top():
            x = s.top()

        print x






        #HW3 Question 4
        #items = [1, 2, 3]

        #print items

        #for i in range(0, len(items)):
        #    s.push(items[i])

        #items = []

        #while not s.is_empty():
        #    items.append(s.pop())

        #print items


        # Loops for user push on to stack
        # while len(s) < 10:
        #     s.push(input("Insert elements on to stack:"))
        # while len(s) > 0:
        #     print(s.pop())
        # print



#  S.push(5)                        # contents: [5]
#  S.push(3)                        # contents: [5, 3]
#  print(len(S))                    # contents: [5, 3];    outputs 2
#  print(S.pop())                   # contents: [5];       outputs 3
#  print(S.is_empty())              # contents: [5];       outputs False
#  print(S.pop())                   # contents: [ ];       outputs 5
#  print(S.is_empty())              # contents: [ ];       outputs True
#  S.push(7)                        # contents: [7]
#  S.push(9)                        # contents: [7, 9]
#  print(S.top())                   # contents: [7, 9];    outputs 9
#  S.push(4)                        # contents: [7, 9, 4]
#  print(len(S))                    # contents: [7, 9, 4]; outputs 3
#  print(S.pop())                   # contents: [7, 9];    outputs 4
#  S.push(6)                        # contents: [7, 9, 6]
#  S.push(8)                        # contents: [7, 9, 6, 8]
#  print(S.pop())                   # contents: [7, 9, 6]; outputs 8
