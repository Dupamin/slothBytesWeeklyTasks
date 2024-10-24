def fizzBuzz(n):
    strArray = []
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            strArray.append("FizzBuzz")
        elif i % 3 == 0:
            strArray.append("Fizz")
        elif i % 5 == 0: 
            strArray.append("Buzz")
        else:
            strArray.append(f"{i}")
        print(i)
    return strArray

print("Write a number to fizzbuzz: ")
fb_number = int(input()) 
print(fizzBuzz(fb_number))