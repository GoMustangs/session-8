import random

list = ['fox', 'cat', 'zebra', 'tiger', 'lion', 'dog', 'ant', 'rat', 'bunny']

print(list)


def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos-1]
            pos = pos - 1
        list[pos] = number

insertionsort(list)

print(list)