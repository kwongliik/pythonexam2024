# The following code contains errors.
# You need to do 5 corrections on the code.
# Try to do corrections on online-python.com OR IDLE PYTHON before you commit the changes.
# testing
def calculation(a, b):
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return subtraction, multiplication, division  # return 3 values separated by comma

def main():
    [x, y, z] = calculation(30, 5)
    print(f"subtraction = {x}, multiplication = {y}, division = {z}") 

if __name__ == "__main__":
    main()