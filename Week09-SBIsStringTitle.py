# Bad solution (memory, speed and readability bad), first solution
def is_title(tString):
    isTitle = True
    nextCBig = False
    for c in tString:
        if nextCBig and not c.isupper():
            isTitle = False
        nextCBig = False
        if c == " ":
            nextCBig = True
    return isTitle

# Better solution from Adham-Emam in comments, edited
# https://github.com/Adham-Emam/Problem-Solving/blob/main/check_title/check_title.py
def is_title_better(tString):
    for word in tString.split(" "):
        if word[0].islower():
            return False
    return True

# Testing
print("\nis_title:")
print(is_title("Hello How Are You?"))
print(is_title("A Simple C++ Program!"))
print(is_title("Water is transparent"))

print("\nis_title_better:")
print(is_title_better("Hello How Are You?"))
print(is_title_better("A Simple C++ Program!"))
print(is_title_better("Water is transparent"))