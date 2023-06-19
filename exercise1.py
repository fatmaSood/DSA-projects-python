# Implement a dynamic array in your chosen language with the following operations
# 1. add(val)
# - an element to the end of the array.
# - copy and double if necessary.
# 2. get(i) - returns the element at index i, throw exception if out of bounds.
# 3. set(i, val) - sets the value at index i to val. throw exception if out of bounds.
# 4. size() - returns the size of the array
# 5. capacity() - returns the capacity of the array

class DynamicArray:
    def __init__(self):
        self._capacity = 1  # Initial capacity of the array
        self._size = 0  # Current size of the array
        self._array = [None] * self._capacity  # Internal array to store elements

    def add(self, val):
        if self._size == self._capacity:
            self._resize_array()  # Double the capacity if the array is full

        self._array[self._size] = val
        self._size += 1

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")

        return self._array[i]

    def set(self, i, val):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")

        self._array[i] = val

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def _resize_array(self):
        self._capacity *= 2  # Double the capacity
        new_array = [None] * self._capacity

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array


# Usage example
arr = DynamicArray()
arr.add(10)
arr.add(20)
arr.add(30)

print("Size:", arr.size())  # Output: Size: 3
print("Capacity:", arr.capacity())  # Output: Capacity: 4

print("Element at index 1:", arr.get(1))  # Output: Element at index 1: 20

arr.set(2, 40)
print("Element at index 2 after set:", arr.get(2))  # Output: Element at index 2 after set: 40