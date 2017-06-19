"""Min heap implemented with a Python list.

We start the list at index 1 instead of 0, otherwise the math won't work out.

A child at index i has a parent at index i // 2. A parent at index i has
children at i * 2 and i * 2 + 1.

For example, this list [None, 1, 2, 3, 4, 5, 6] becomes a heap that looks
like this:
                 1
              /     \
             2       3
           /   \   /
          4    5  6
"""

class MinHeap:
    def __init__(self, initial=None):
        self.heap = [None]  # Start at index 1
        if initial:
            for item in initial:
                self.push(item)

    def __repr__(self):
        return str(self.heap)

    def _shift_up(self, i):
        """Given an item's index, shift it as far up heap as it can go."""
        
        while i // 2 > 0:  # Parent should never be index of 0
            
            # Compare item value to parent value and swap if item is smaller
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                
                i = i // 2  # Reassign i to the correct index

            else:
                break  # Exit out of while loop, item is in the right spot

    def _shift_down(self, i):
        """Given an item's index, shift it as far down as it can go."""

        while i * 2 < len(self.heap):  # while children exist
            child_1 = self.heap[i * 2]
            try:
                child_2 = self.heap[i * 2 + 1]
            except IndexError:
                child_2 = None

            if self.heap[i] < child_1:
                # The item must be smaller than all of its children, so we can
                # exit the while loop
                break

            # Swap with the smallest child to maintain order, then reassign
            # the index
            if child_1 < child_2 or not child_2:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            else:
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1

    def push(self, el):
        """Add an item to the end of the heap.
        
        Shifts the added item to its appropriate location.
        """
        
        self.heap.append(el)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        """Remove the smallest item in the heap and return it."""

        min_item = self.heap[1]
        self.heap[1] = self.heap[-1]  # Place the last item at the root
        del self.heap[-1]  # Last item no longer exists
        
        self._shift_down(1)  # Shift the item down to its correct location

        return min_item
