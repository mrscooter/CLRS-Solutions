# Implements Max Heap
class Heap:
    def __init__(self, is_greater_or_equal_than_function=(lambda a, b: a >= b), elems=list()):
        self.__is_greater_or_equal_than_function = is_greater_or_equal_than_function
        self.__heap = elems
        self.__build_heap()

    def __build_heap(self):
        for i in range(len(self.__heap)-1,-1,-1):
            self.__heapify(i)

    def __heapify(self,i):
        if self.__left_child(i) >= len(self.__heap):
            return

        left_child_value = self.__heap[self.__left_child(i)]

        has_right_child = False
        if self.__right_child(i) < len(self.__heap):
            has_right_child = True
            right_child_value = self.__heap[self.__right_child(i)]

        if (not has_right_child) and self.__is_greater_or_equal_than_function(left_child_value, self.__heap[i]):
            self.__exchange_and_heapify_recursively(i,self.__left_child(i))
        elif has_right_child:
            if self.__is_greater_or_equal_than_function(left_child_value, right_child_value) and self.__is_greater_or_equal_than_function(left_child_value, self.__heap[i]):
                self.__exchange_and_heapify_recursively(i,self.__left_child(i))
            elif self.__is_greater_or_equal_than_function(right_child_value, left_child_value) and self.__is_greater_or_equal_than_function(right_child_value, self.__heap[i]):
                self.__exchange_and_heapify_recursively(i,self.__right_child(i))

    def __exchange_and_heapify_recursively(self, parent, child):
        child_value = self.__heap[child]
        self.__heap[child] = self.__heap[parent]
        self.__heap[parent] = child_value
        self.__heapify(child)

    @staticmethod
    def __parent(i):
        return ((i+1) // 2)-1

    @staticmethod
    def __left_child(i):
        return 2*(i+1)-1

    @staticmethod
    def __right_child(i):
        return 2*(i+1)

    def __reversed__heapify(self, i):
        if i == 0:
            return

        parent_value = self.__heap[self.__parent(i)]
        if self.__is_greater_or_equal_than_function(self.__heap[i], parent_value):
            self.__heap[self.__parent(i)] = self.__heap[i]
            self.__heap[i] = parent_value
            self.__reversed__heapify(self.__parent(i))

    def __print_heap(self, i, offset):
        if i >= len(self.__heap):
            return

        offset_string = "\t"*offset
        print(f"{offset_string}{self.__heap[i]}")
        self.__print_heap(self.__left_child(i),offset+1)
        self.__print_heap(self.__right_child(i),offset+1)

    def print_heap(self):
        self.__print_heap(0,0)

    def extract_max(self):
        if self.is_empty():
            raise  Exception("Empty heap!")

        max_elem = self.__heap[0]

        self.__heap[0] = self.__heap[len(self.__heap)-1]
        del self.__heap[len(self.__heap)-1]

        self.__heapify(0)

        return max_elem

    def insert(self,elem):
        self.__heap.append(elem)
        self.__reversed__heapify(len(self.__heap)-1)

    def is_empty(self):
        return len(self.__heap) == 0








