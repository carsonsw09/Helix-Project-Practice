# This program will take in a number and return the sum of the lucky digits (7) in that number
def LuckyDigitSum(n: int) -> int:
    """
    Takes in n(int)
    Returns the sum of the lucky digits (7) in that number
    """
    num_str = str(abs(n)) # Convert the number to a string to iterate through its digits and remove the negative sign if it exists
    
    count_lucky = 0
    for digit in num_str:
        if digit == '7':
            count_lucky += 1  # If the digit is '7', add 7 to the count
            
    sum_lucky = count_lucky * 7  # Multiply the count of Lucky digits by 7 to get the sum of the Lucky digits
    return sum_lucky


if __name__ == "__main__":
    # Example usage
    number = 71717177
    result = LuckyDigitSum(number)
    print(f"The sum of the Lucky digits in {number} is: {result}")