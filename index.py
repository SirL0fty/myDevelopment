#!/usr/bin/env python3

#* Lists and Tuples
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog')  # 0
my_pets.index('chicken')  # 3
my_pets.index('lizard')  # ValueError: 'lizard' is not in list

#* Range

nums = range(1, 10, 2)

nums.index(5)  # 2
nums.index(10)  # ValueError: 10 is not in list
nums.index(1)  # 0
