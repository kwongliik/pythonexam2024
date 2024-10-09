# This program is used to reverse a string. 
# Complete the code below and then test run it.

# string_reverse() is a function that reverse "str1" as input
def string_reverse(str1):
    # Initialize an empty string 'rstr1' to store the reversed string
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = .......... # Use built-in function to calculate the 'str1' length as argument
    
    # Execute a while loop until 'index' becomes 0
    ........ index > 0:
        # Concatenate the character at index - 1 of 'str1' to 'rstr1'
        rstr1 ..... str1[.........]
        
        # Decrement the 'index' by 1 for the next iteration
        index = ............
    
    # Return the reversed string stored in 'rstr1'
    return rstr1

# Print the result of calling the string_reverse() function with the input string '1234abcd'
print("String reverse for \'12345abcde\' is", string_reverse('12345abcde')) # The output is "edcba54321"
