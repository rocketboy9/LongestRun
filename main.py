#longest run project
#created a list of random integers with the length of the list being given by user input and then found the longest sequence where the numbers increased or decreased.
#printed out the indexes and the numbers at those indeces which made up the sequence
import random

def LongestRun(list):

    ascending = False#values to know whether the for loop is descending or ascending
    descending = False

    currentList = []#lists for possible max values
    maxList = []

    temp = 0    #holds the int variable for the previous loop
    currentMax = 0#holds the max
    current = 0#holds whatever the current max is
    index = 0
    checkingCurrentIndex = 0#possible max index
    startIndexOfLongest = 0#possible max index that might be overwritten
    for num in list:
        if index == 0:#code for first pass
            temp = num
            index += 1
            startIndexOfLongest = 0
            continue

        if index == 1:#code for second pass
            if num > temp:
                ascending = True
                current = 2
                currentMax = 2
            if num<temp:
                descending = True
                current = 2
                currentMax = 2
            currentList.append(temp)
            currentList.append(num)
            temp = num
            index += 1
            continue

        if ascending:#at the current index of the list if ascending, this is the if statement you will go down
            if num>temp:#if still ascending
                current += 1
                currentList.append(num)
                if current>currentMax:#if greater than max
                    currentMax = current
                    maxList = currentList.copy()
                    startIndexOfLongest = checkingCurrentIndex
            if temp>num:#if not ascending anymore
                currentList.clear()#clear and append the 2 values to the list
                currentList.append(temp)
                currentList.append(num)
                checkingCurrentIndex = index-1
                current = 2
                descending = True#switch ascending and descending values
                ascending = False
        elif descending:#at the current index of the list if descending, this is the if statement you will go down
            if num<temp:#if still descending
                current+=1
                currentList.append(num)
                if current>currentMax:#if greater than max
                    currentMax = current
                    maxList = currentList.copy()
                    startIndexOfLongest = checkingCurrentIndex
            if temp<num:#if not descending anymore
                currentList.clear()#clear and append the 2 values to the list
                currentList.append(temp)
                currentList.append(num)
                checkingCurrentIndex = index-1
                current = 2
                descending = False#switch ascending and descending values
                ascending = True

        temp = num
        index += 1

    print("Max ascending/descending length: ", currentMax, "\nindex where the longest list of AscDesc starts: ", startIndexOfLongest, "\nList of numbers in the max length list", maxList)


if __name__ == '__main__':

    listOfRandomIntegers = []
    for x in range(500):#Creates a random list of 500 integers with values in the range 1-1000
        number = random.randint(1, 1000)
        listOfRandomIntegers.append(number)

    LongestRun(listOfRandomIntegers)#call the longestRun function using a list

