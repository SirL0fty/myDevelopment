#!/usr/bin/env python3

def print_teacher(**kwargs):
        for key, value in kwargs.items():
                print(f'{key}: {value}')


print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic='javascript')
