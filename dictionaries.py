#!/usr/bin/env python3

course = {'Name':'Mike', 'title':'Introducing Dictionaires', 'level':'Beginner'}

print(course['Name'])


course['Name'] = 'Nicky'
course['level'] = 'Advanced'

course['stages'] = 2
del(course['stages'])

print(course)