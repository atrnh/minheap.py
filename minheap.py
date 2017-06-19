"""Min heap implemented with a Python list."""

class MinHeap:
    def __init__(self, initial=None):
        self.heap = [None]  # Start at index 1
        if initial:
            for item in initial:
                self.push(item)

    def __repr__(self):
        return str(self.heap)

    def get_parent(self, i):
        """Return the parent item of the given index."""

        if i > 1:
            return self.heap[i // 2]
        else:
            return None  # Error: the root does not have a parent

    def _shift_up(self, i):
        """Given an item's index, shift it as far up heap as it can go."""
        
        while i // 2 > 0:  # Parent should never be index of 0
            # Compare item value to parent value and swap if item is smaller
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
            else:
                break  # We can fail here because item is in the right spot

    def _shift_down(self, i):
        """Given an item's index, shift it as far down as it can go."""

        while i * 2 < len(self.heap):  # while children exist
            child_1 = self.heap[i * 2]
            try:
                child_2 = self.heap[i * 2 + 1]
            except IndexError:
                child_2 = None

            if self.heap[i] < child_1:  # item is smaller than its children
                print "Heap is already valid"
                break

            if child_2:
                # Swap with the smallest child to maintain order
                if child_1 < child_2:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i = i * 2
                else:
                    self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
            else:  # child_2 doesn't exist and the item is larger than its child
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2

    def push(self, el):
        """Add an item to the heap."""
        
        self.heap.append(el)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        """Pop the min item."""

        min_item = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]  # Last item no longer exists
        
        self._shift_down(1)

        return min_item
