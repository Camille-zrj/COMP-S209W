class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # Swap current node with parent if it is smaller (min-heap property)
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def _heapify_down(self, index):
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        size = len(self.heap)

        # Find the smallest node among current node and its children
        if left < size and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < size and self.heap[right] < self.heap[min_index]:
            min_index = right

        # Swap and recurse if heap property is violated
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._heapify_down(min_index)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty")

        min_val = self.heap[0]
        # Replace root with the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # Adjust heap property
        self._heapify_down(0)
        return min_val

    def get_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def heapify(self, arr):
        self.heap = arr
        # Start from the last non-leaf node and sift down
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        return self.heap


# Test Cases
if __name__ == "__main__":
    # 1. Initialize min-heap
    heap = MinHeap()
    print("Empty heap:", heap.display())

    # 2. Insert elements
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(2)
    print("Heap after insertion:", heap.display())
    print("Minimum element:", heap.get_min())

    # 3. Extract minimum element
    print("Extracted min:", heap.extract_min())
    print("Heap after extraction:", heap.display())

    # 4. Heapify an array
    arr = [9, 4, 7, 2, 6]
    heap.heapify(arr)
    print("Heap after heapify:", heap.display())
