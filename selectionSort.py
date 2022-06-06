import random
# selection sort
#   starting at the beginning, search for the smallest item,
#      then swap it for the first. Then do the same for each
#      spot in the array.
def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

def main():
    names = ['stacy', 'carly', 'ben', 'mike', 'zed', 'vlademeer', 'jo', 'mo', 'abraham', 'lily']
    # let's make a list of random numbers


    print(names[0:10])
    selectionsort(names)
    print(names[0:10])

if __name__ == '__main__':
    main()