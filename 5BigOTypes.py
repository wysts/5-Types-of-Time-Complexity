# Constant Time Example (0(3))
# A simple function that multiply by two the first item in a list :
def consTime(things):
    twoTimes = things[0] * 2
    print("(Example #1Constant)")
    print(twoTimes)
    print("")
consTime([2, 4, 7, 10])


# Linear Time Example
# A function that prints every item in a list one by one :
def linTime(stuffs):
    for stuff in stuffs:
        print(stuff, end=" ")

print("(Example #2Linear)")
linTime([3, 10, 9, 99, -13])
print("\n")


# Logarithmic Time Example
# A binary search or logarithmic search function that finds the value specified :
def binSearch(list, value):
    n = len(list)
    first = 0
    last = n - 1
    while first <= last:
        midValue = (first + last) // 2
        if value < list[midValue]:
            last = midValue - 1
        elif value > list[midValue]:
            first = midValue + 1
        else:
            return midValue

print("(Example #3Logarithmic)")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binSearch(list, 6))
print(" ")


# Quadratic Time Example
# A function that iterates through all the quants in input list, then a nested inner loop again iterates (n*n) :
def quadTime(quants):
    for quant in quants:
        for inQuant in quants:
            print(quant, ' ', quant)

print("(Example #4Quadratic)")
quadTime([1, 2])
print(" ")


# Exponential Time Example
# A recursive Fibonacci function calls itself in specific conditions :
def recursiveFunct(n):
    if n <= 1:
        return n
    return recursiveFunct(n-1) + recursiveFunct(n-2)

print("(Example #5Exponential)")
print(recursiveFunct(6))
