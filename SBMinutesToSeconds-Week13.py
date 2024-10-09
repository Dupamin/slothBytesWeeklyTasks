# converts time in minutes:seconds format to seconds (O(n) time complexity based on 
# https://stackoverflow.com/questions/55113713/time-space-complexity-of-in-built-python-functions
# and )
def MinutesToSeconds(timeStr):
    timeStr = timeStr.split(":")
    if int(timeStr[1]) > 59:
        return -1
    return int(timeStr[0]) * 60 + int(timeStr[1])

# without built-in functions (O(n) time complexity, right?)
def MinutesToSecondsHarder(timeStr):
    time = str.split
    minutes = ""	
    for i in range(len(timeStr)):
        if timeStr[i] == ":":
            seconds = timeStr[i+1:]
            break
        else:
            minutes += timeStr[i]
    if int(seconds) > 59:
        return -1
    return int(minutes) * 60 + int(seconds)

# test cases ----------------------
# with built in functions
print(MinutesToSeconds("1:01"))
print(MinutesToSeconds("0:59"))
print(MinutesToSeconds("0:60"))
print(MinutesToSeconds("121:55"))
# without built in functions
print(MinutesToSecondsHarder("1:01"))
print(MinutesToSecondsHarder("0:59"))
print(MinutesToSecondsHarder("0:60"))
print(MinutesToSecondsHarder("121:55"))
#----------------------------------