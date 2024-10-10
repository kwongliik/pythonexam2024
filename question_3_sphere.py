# This program is used to calculate the volume of sphere.
# You need to fill in the blanks to complete the code.
# Upon completion, you need to test run the program to give you correct output

from math import pi

# kira_sfera() is a function that return the volume of sphere
def volume_sphere(radius):
    volume = 4/3 * pi * radius ** 3
    return volume

def main():
    r = float(input("Input radius: ")) 
    Volume = volume_sphere(r) 
    print(f"Isipadu sfera = {Volume :.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()
