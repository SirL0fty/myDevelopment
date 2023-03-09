#!/usr/bin/env python3

#* Lists and Tuples
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits  # False
'eggplant' not in fruits  # True

'eggplant' in vegetables  # True
'eggplant' not in vegetables  # False

#* Ranges

nums = range(10)

0 in nums  # True
10 in nums  # False
4 in nums  # True

0 not in nums  # False
15 not in nums  # True
10 not in nums  # True


nums = range(1, 10, 2)

0 in nums  # False
6 in nums  # False

4 not in nums  # True
8 not in nums  # True
