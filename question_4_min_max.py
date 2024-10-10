# This program will print out the maximum number among four numbers.
# Complete the code below.
# Upon completion, you should test run your program to get the biggest number (maximum number).

# max_value() is a function that will return maximum number.
def min_value(a, b, c, d):
    return min(a, b, c, d)

def max_value(a, b, c, d):
    return max(a, b, c, d)

def main():
    min = min_value(30.34, 22.23, 48.89, 27.49)
    max = max_value(30.34, 22.23, 48.89, 27.49)    
    print(f"Minimum is {min}")
    print(f"Maximum is {max}")

# Don't change the code below!
if __name__ == "__main__":
    main()

