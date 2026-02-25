# This program will take in a list and then return the sum of all the lucky digits which will be 7 and 9.
# If this is the list [9,7,0,9] then the output will be 25. If there are no lucky digits then the output should be 0.

def checklucky(nums: int):
    """
    Takes in nums(int)
    Use if else to check for 7 and 9 in the number
    Then adds the numbers to find the sum of the lucky digits
    """
    lucky_total = 0
    for num in nums:
        if '7' in str(num) or '9' in str(num):
            lucky_total += int(num)
    
    print(lucky_total)
    
    
if __name__ == "__main__":
    nums = [29, 7, 0, 4] 
    nums2 = [0, 0, 7, 0]
    nums3 = [0, 0, 0, 0]
    nums4 = [700, 900, 79]
    
    checklucky(nums) # 36
    checklucky(nums2) # 7
    checklucky(nums3) # 0
    checklucky(nums4) # 1679