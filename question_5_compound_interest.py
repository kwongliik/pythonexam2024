# This program is used to calculate compound interest.
# User can input: 
# (a) principal (P), 
# (b) interest rate (r), 
# (c) time in years (t), and 
# (d) number of periods the interest is compounded per year (n)
# You need to complete the code below.
# Upon completion, you should test run the code to give you correct output.

# compound_interest() is a function that will return the result of calculation
def cal_matured_value(P, r, t, n):
    result = P * (pow(1 + ((r / 100) / n), n * t)) # Use built-in function "pow()" to complete the formula
    return result 

def get_inputs():
    p = float(input("Enter the principal amount: ")) 
    r = float(input("Enter the interest rate: ")) 
    t = float(input("Enter the time in years: ")) 
    n = float(input("Enter the number of periods the interest is compounded per year: ")) 
    return (p, r, t, n) 
    
def main():
    P, R, T, N = get_inputs()
    matured_value = cal_matured_value(P, R, T, N)
    print(f"Matured value is {matured_value :.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()