# NOT FINISHED
def seperate_numbers(number):
    number_list = []
    #print(number % 100000000)
    for l in range(len(str(number-1)), 1, -1):
        #print(l)
        print(number % int('1' + '0'*(l-1)))
        number_list.append(number - number % int('1' + '0'*(l-1)))
    return number_list

# FINISHED
def seperate_numbers_better(number):
    number_list = []
    number_str = str(number)
    for l in range(len(number_str)):
        if number_str[l] != '0':
            number_list.append(int(number_str[l]) * 10**(len(str(number))-l-1))
    
    return number_list
        

#seperate_numbers(123456789)
print(seperate_numbers_better(123456789))
print(seperate_numbers_better(123406789))
print(seperate_numbers_better(359))

#print(seperate_numbers(123456789))