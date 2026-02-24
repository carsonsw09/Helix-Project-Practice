# This program will take in a list and return the sum of the
# lucky digits which is 7. Negative numbers can be included in this
# For example, [7,-7,27,0] should return 27

def LuckyListSum(nums: list) -> int:
    """
    Takes in nums(list) and return the sum of the lucky digits (7) in that list
    """
    
    total_sum = 0
    for num in nums:
        if '7' in str(num):
            total_sum += num
    return total_sum




if __name__ == "__main__":
    # Test Cases
    number_list = [100, -70, 24, 0]
    result = LuckyListSum(number_list)
    print(result)