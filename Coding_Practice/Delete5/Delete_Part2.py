# This program will delete every value that has the value 5 in it or is divisible by 5. It will then print the remaining values.

def check5(nums: int):
    """
    Takes in nums(int)
    Uses if elses to check for a 5 in the number or if it is divisible by 5
    """
    
    for num in nums:
        if '5' in str(num) or num % 5 == 0:
            continue
        else:
            print(num)
            
            
if __name__ == "__main__":
    nums = range(1, 101)
    check5(nums)