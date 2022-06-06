import random

# sequential search
#  look for an item and return where that item is in the list.
#  if it's not there, return -1
def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            return i

    # if we went through the whole haystack, it must not be there
    return -1

def main():
    numbers = ['duck', 'deer', 'dog', 'fox', 'cat', 'sloth', 'turtle']
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    target = 'cat'
    location = sequentialsearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))

main()