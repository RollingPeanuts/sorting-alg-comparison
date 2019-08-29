import random
import numpy as np
import copy

def bubbleSort(num_list):
    #"isSorted" is my flag to check if the list is sorted
    isSorted = False
    count = 0
    while(isSorted == False):
        #Algorithm stops once it cycles through the list without making any changes
        isSorted = True
        for i, num in enumerate(num_list):
            #Making sure that a variables are inbound (whether term i+1 exists)
            if(i+1 < len(num_list)):
                if(num > num_list[i+1]):
                    #Swaps neighbors if former is greater than latter
                    num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                    isSorted = False
            else:
                #Otherwise, Increment the cycle counter once the sorter reaches the last element
                count+=1
                break
    return count


#Bubble sort but not just comparing neighbors
def combSort(number_list):
    count = 0
    gap_list = []
    gap = int(len(number_list)/1.3)

    #Make a list of "gaps" to sort using combsort
    while(gap > 1):
        gap_list.append(gap)
        gap = int(gap/1.3)

    for gap in gap_list:
        for i, num in enumerate(number_list):
                #Checks if the gap is out of bounds
                if(i+gap < len(number_list)):
                    #Swaps the element and (element + gap) if the current element is greater
                    if(num > number_list[i+gap]):
                        number_list[i],number_list[i+gap] = number_list[i+gap],number_list[i]
                else:
                    #Otherwise, adds a count to the number of cycles
                    count+=1
                    break

    #Combsort can't verify an ordered list until gap=1. So I can call bubblesort to finish sorting and check the list for me
    count+=bubbleSort(number_list)
    return count


def generateRandomNumberLists(sampleNum, listSize):
    randSetsList = []
    for i in range(sampleNum):
        rand = random.sample(range(listSize), listSize)
        randSetsList.append(rand)
    return randSetsList


def runSortingAlgorithms(randSetsList):
    #Since my sort functions modify the original list, I need to make deep copies
    randSetsList2 = copy.deepcopy(randSetsList)

    timeListBubble = []
    for i in randSetsList:
        timeListBubble.append(bubbleSort(i))
    print("\nBubbleSort took an average of "+str(np.mean(timeListBubble))+" loops to finish sorting")

    timeListComb = []
    for i in randSetsList2:
        timeListComb.append(combSort(i))
    print("CombSort took an average of "+str(np.mean(timeListComb))+" loops to finish sorting.")


def runTests():
    sampleNum = 0
    while(sampleNum <= 0):
       sampleNum = int(input("How many random number sets? ")) 

    listSize = 0;
    while(listSize <= 0):
        listSize = int(input("How big of a list size? "))

    randSetsList = generateRandomNumberLists(sampleNum, listSize)
    runSortingAlgorithms(randSetsList)

runTests();
