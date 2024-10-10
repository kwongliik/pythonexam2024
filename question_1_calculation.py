# The following code contains errors.
# You need to do 5 corrections on the code.
# Try to do corrections on online-python.com OR IDLE PYTHON before you commit the changes.

def calculation(x, y):
    subtraction = x - y
    multiplication = x * y
    division = x / y if y != 0 else None  # To handle division by zero
    return subtraction, multiplication, division

def get_numbers():
    A = float(input("Input A: "))
    B = float(input("Input B: "))    
    return A, B

def main():
    [x, y] = get_numbers()
    [S, T, U] = calculation(x, y)
    print(f"subtraction = {S}, multiplication = {T}, division = {U}") 

if __name__ == "__main__":
    main()