#!/bin/python3

import sys


class Heap:
    def __init__(self, relation):
        self.size = 0
        self.heap = []
        self.enforce_relation = relation

    def get_parent_index(self, index):
        if index < 0 or isinstance(index, int):
            raise ValueError('Index must be positive integer')
        else:
            return int((index - 1) / 2)

    def get_right_child_index(self, index):
        if index < 0 or isinstance(index, int):
            raise ValueError('Index must be positive integer')
        else:
            return (index * 2) + 2

    def get_left_child_index(self, index):
        if index < 0 or isinstance(index, int):
            raise ValueError('Index must be positive integer')
        else:
            return (index * 2) + 1

    def insert(self, val):
        if val is not None and isinstance(val, int):
            self.heap.append(val)
            self.size += 1
            self.heapify_up()
        else:
            raise ValueError('Value must be an integer')

    def heapify_up(self):
        child = self.size - 1
        parent = self.get_parent_index(child)
        while (child != 0 and
               not self.enforce_relation(self.heap[parent], self.heap[child])):
            temp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = temp
            child = parent
            parent = self.get_parent_index(child)

    def heapify_down(self):
        parent = 0
        left_child = self.get_left_child_index(parent)
        right_child = self.get_right_child_index(parent)
        while (left_child < self.size and
               self.enforce_relation(self.heap[parent], self.heap[left_child])):
            if (right_child >= self.size):
                temp = self.heap[parent]
                self.heap[parent] = self.heap[left_child]
                self.heap[left_child] = temp


    def remove_root(self):
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heapify_down()


class MidHeap:
    def __init__(self):
        self.size = 0
        self.greater_min_heap = []
        self.smaller_max_heap = []

    def insert(self, val):
        if self.size <= 1:
            self.smaller_max_heap.append(val)
        elif val > self.smaller_max_heap[0]:
            self.greater_min_heap.append(val)
        else:
            self.smaller_max_heap.append(val)

        self.size += 1


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
