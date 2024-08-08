def sort_by_letter(abc):
    return sorted(abc, key=lambda x: max(x))

def multiply(n):
    return lambda a: a * n

def main():
    tests = [
        ["932c", "832u32", "2344b"],
        ["99a", "78b", "c2345", "11d"],
        ["572z", "5y5", "304q2"],
        ["111z23", "12121a", "x1", "b2"]
    ]
    for test in tests:
        #print(max(test[0]))
        print(sort_by_letter(test))
        
    bythree = multiply(3)
    print(bythree(11))

if __name__ == "__main__":
    main()
    