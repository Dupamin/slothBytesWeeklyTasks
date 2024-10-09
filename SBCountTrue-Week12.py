def countTrue(boolVal):
    count = 0
    for i in boolVal:
        if i == True:
            count += 1
    return count

def countTrueShort(boolVal):
    return boolVal.count(True)

# Test Cases
#----------------------------------
# with for loop
print(countTrue([True, False, True, True, False, False, True]))
print(countTrue([]))

# built in boolean function
print(countTrueShort([True, False, True, True, False, False, True]))
print(countTrueShort([]))
#----------------------------------