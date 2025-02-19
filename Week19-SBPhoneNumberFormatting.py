# Lmao, thanks Github Copilot, that was easy
def format_phone_number(number_list):
    return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*number_list)

# My own implementation, seems much worse and probably is, but at least I figured it out myself :)))
def format_phone_number_mine(number_list):
    phone_number_format = "(xxx) xxx-xxxx"
    phone_number = ""
    counter = 0
    for i in range(len(phone_number_format)):
        if phone_number_format[i] == "x":
            phone_number += str(number_list[counter])
            counter += 1
        else:
            phone_number += phone_number_format[i]
    return phone_number

# Test Cases
print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # (123) 456-7890
print(format_phone_number_mine([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # (123) 456-7890