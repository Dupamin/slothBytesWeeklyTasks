def countSmileys(array):
    if len(array) == 0:
        return "Empty array."
    count = 0
    possibleSmileys = [":)", ":D", ";)", ";D", ":-)", ":-D", ";-)", ";-D", ":~)", ":~D", ";~)", ";~D"]
    for a in array:
        if a in possibleSmileys:
            count += 1
    return count

def countSmileysTwo(array):
    if len(array) == 0:
        return "Empty array."
    count = 0
    for a in array:
        if len(a) == 3 and a[0] in ":;" and a[1] in "-~" and a[2] in ")D" \
            or len(a) == 2 and a[0] in ":;" and a[1] in ")D":
                count += 1
        # if len(a) == 2 and a[0] in ":;" and a[1] in ")D":
        #     count += 1
    return count


testCases = [
    [":)", ";(", ";}", ":-D"],
    [";D", ":-(", ":-)", ";~)"],
    [";]", ":[", ";*", ":$", ";-D"],
    []
]

for t in testCases:
    print(f"countSmileys(t): {countSmileys(t)}")
    print(f"countSmileysTwo(t): {countSmileysTwo(t)}")