# import time
import cProfile

def advanced_sort_bad(unsortedList):
    sortedList = []
    usedChars = []
    sublist = []
    for item in unsortedList:
        if not item in usedChars:
            for i in range(len(unsortedList)):
                if item == unsortedList[i]:
                    sublist += [item,]
                    # print(f"sublist: {sublist}")
            usedChars += [item,]
            sortedList += [sublist,]
            sublist = []
    #     print(f"usedChars: {usedChars}")
    # print(f"sortedList: {sortedList}")
    return sortedList
    
# unsortedList = [2, 1, 2, 1, 3, 5, 5, 5, 2, 1, 9]
unsortedList = ["a", "a", "c", "B", "b", "c", "a", "a"]
# start_time = time.monotonic()
sortedList = advanced_sort_bad(unsortedList)
# print(f"advanced_sort_bad() took: {(time.monotonic() - start_time)}")
print(f"unsortedList: {unsortedList}")
print(f"sortedList: {sortedList}")


# From some guys's solutions in the SB newsletter comments
def advancedListSearch(input): 
    fin = [] 
    for i in list(set(input)): 
        fin.append([i] * input.count(i)) 
    return sorted(fin, key=lambda x: input.index(x[0]))

# start_time = time.monotonic()
sortedList = advancedListSearch(unsortedList)
# print(f"advancedListSearch() took: {(time.monotonic() - start_time)}")
print(f"sortedList (2nd): {sortedList}")

def testingFunc():
    x = 0
    for i in range(0, 10000000):
        x *= i

cProfile.run('testingFunc()')