def super_digit(n, k):
    # Function to find the super digit of a number
    def recursive_super_digit(x):
        if x < 10:
            return x
        else:
            return recursive_super_digit(sum(int(digit) for digit in str(x)))
    
    # Calculate the sum of digits of n
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Multiply the digit sum by k
    total_sum = digit_sum * k
    
    # Find and return the super digit
    return recursive_super_digit(total_sum)

# Get input from user with a message prompt
n, k = input("Enter a number n and the repetition factor k, separated by space: ").split()
k = int(k)

# Print the output (super digit)
print("The super digit is:",super_digit(n, k))
