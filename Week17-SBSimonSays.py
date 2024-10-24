#Not returning result as integer, but as float. I don't follow rules, I make them.
# :D

#Does math
def do_math(num1, num2, word_operator):
    if word_operator == "add":
        return num1 + num2
    elif word_operator == "subtract":
        return num1 - num2
    elif word_operator == "multiply":
        return num1 * num2
    elif word_operator == "divide":
        return num1 / num2
    else:
        return "Invalid Word Operator"

#Does string recongition and returns result
def simon_says(command_list):
    number_to_math = 0
    operator_list = ["add", "subtract", "multiply", "divide"]
    for command_item in command_list:
        words = command_item.split()
        if words[0] == "Simon" and words[1] == "says":
            if words[2] in operator_list:
                if words[3] == "by":
                    number_to_math = do_math(float(number_to_math), int(words[4]), words[2])
                else:
                    number_to_math = do_math(float(number_to_math), int(words[3]), words[2])
                print(f"{command_item}: {number_to_math}")
    return number_to_math

print("\nSimon Says test 1 (All are 'Simon says' commands)")                
simon_says(["Simon says add 6", "Simon says subtract 3", "Simon says multiply by 4", "Simon says divide by 2", "Simon says add 3", "Simon says subtract 1", "Simon says multiply by 2", "Simon says divide by 3"])
print("\nSimon Says test 2 (Some are not 'Simon says' commands)")                
simon_says(["Simon says add 6", "Simeon says subtract 3", "Simon says multiply by 4", "Simon says divide by 2", "Simoni says add 3", "Simon says subtract 1", "Smon says multiply by 2", "divide by 3"])
print("\nSimon Says test 3 (Tt accepts 'divide' and 'divide by'. Same with 'multiply'.)")
simon_says(["Simon says add 6", "Simeon says subtract 3", "Simon says multiply 2", "Simon says divide by 6", "Simoni says add 1", "Simon says subtract 1", "Smon says multiply by 2", "divide by 3"])
