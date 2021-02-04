#!/usr/bin/env python
import numpy as np

class Dog:
    def __init__(self, number):
        self.number = str(number)
        self.type = "doggie"
        self.color = "brown"

    def __str__(self):
        return "a {self.type} dog with {self.color} color, number = {self.number}". format(self=self)

cony  = Dog(1)
ton = Dog(2)
bella = Dog(3)
yuta = Dog(4)

print(cony)
print(ton)
print(bella)
print(yuta)

array = np.zeros((1,4), dtype = object)

print(array)
print(array.shape)
for i in range(array.shape[1]):
    array[0, i] = Dog(i)
    print(i)

print(array[0, 2])
