import random
# bubble sort
# start at the beginning and look at the first two items. If they are
#    out of order, swap them. Continue to the end of the list
#    if we go through the list without swapping, we're done.

list = ['dog', 'ant', 'zebra', 'elephant', 'lizard', 'fox', 'deer', 'cat', 'monkey', 'donkey']

print(list)

def bubblesort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                swap = True
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1] = tmp

bubblesort(list)

print(list)