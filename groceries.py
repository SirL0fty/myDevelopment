#!/usr/bin/env python3

groceries = ['Tacos', 'Beef', 'Cheese', 'Salsa', 'Sour Cream', 'Tortillas' ]


for index, item in enumerate(groceries, 1):
        print(f'{index}. {item}')
        index +=1