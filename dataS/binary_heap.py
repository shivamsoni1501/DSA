class BinaryHeap:
    def __init__(self, _array=[]):    
        self._array = _array
        if _array:
            self.heapify()

    def __str__(self): return self._array.__str__()
    def __len__(self):    return len(self._array)
    def isEmpty(self):    return len(self) == 0
    def _parent(self, index):    return (index-1)//2
    def _left_child(self, index):    return 2*index+1
    def _right_child(self, index):    return 2*index+2
    def _is_valid_child(self, index, ch=0): return 2*index+1+ch < len(self)

    def heapify(self):
        for i in range(len(self)//2, -1, -1):
            self._downheap_buid(index=i)

    def _upheap_build(self, index):
        if index > 0:
            parent_i = self._parent(index)
            if self._array[index] < self._array[parent_i]:
                self._array[index], self._array[parent_i] = self._array[parent_i], self._array[index]
                self._upheap_build(parent_i)
    
    def _downheap_buid(self, index=0):
        if self._is_valid_child(index, ch=0):
            least_c = self._left_child(index)
            r_child = self._right_child(index)
            if self._is_valid_child(index, ch=1) and self._array[least_c] > self._array[r_child]:
                least_c = r_child
            if self._array[least_c] < self._array[index]:
                self._array[least_c], self._array[index] = self._array[index], self._array[least_c]
                self._downheap_buid(least_c)

    def min(self):
        return self._array[0] if not self.isEmpty() else -float('inf')

    def push(self, element):
        self._array.append(element)
        if not self.isEmpty():
            self._upheap_build(len(self)-1)
    
    def pop(self):
        if not self.isEmpty():
            self._array[0], self._array[-1] = self._array[-1], self._array[0]
            temp = self._array.pop()
            self._downheap_buid()
            return temp

    def depth_first_search(self, index=0, level=0):
        print( ' '*4*level+'->',self._array[index])
        if self._left_child(index) < len(self):
            self.depth_first_search(self._left_child(index), level+1)
            if self._right_child(index) < len(self):
                self.depth_first_search(self._right_child(index), level+1)


if __name__ == '__main__':
    array = [1,2,42, 12,4,21,1 ,21,4,12,41,24,125,2,43]
    heap = BinaryHeap(array)
    print(array)
    while heap:
        print(heap.pop(), end=' => ')
    # heap = BinaryHeap()
    # heap.push(13)
    # heap.push(14)
    # heap.push(11)
    # heap.push(4)
    # heap.push(12)
    # heap.push(25)
    # heap.push(16)
    # heap.push(15)
    # heap.push(5)
    # heap.push(9)
    # heap.push(7)
    # heap.push(4)
    # heap.push(20)
    # heap.push(6)
    # heap.push(5)
    # heap.push(5)
    # heap.push(4)
    # heap.push(4)

    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
