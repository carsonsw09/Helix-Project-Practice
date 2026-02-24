# My program designed to turn every value (1-100) that has a 7 in it or is divisible by 7 into Lucky! and return every other value
# as normal

def isLucky(n: int) -> bool:
    """
    Takes in n(int)
    Returns a bool
    Every number divisible by 7 or containing the digit '7' is considered lucky
    So that will return true and any other number will return false
    """
    # Condition 1: Divisible by 7
    if n % 7 == 0:
        return True
    
    # Condition 2: Contains digit '7'
    if '7' in str(n):
        return True
    
    return False

def LuckyNumberPrinter():
    for i in range(1, 101):
        if isLucky(i):
            print("Lucky!")
        else:
            print(i)
            
if __name__ == "__main__":
    LuckyNumberPrinter()
            