def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True
    
num = int(input("Is your number a prime number?: "))
print("It is! :D") if isPrime(num) else print("It's not... :(")
        
        