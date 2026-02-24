def isdigit5(n):
    """
    Returns True if n is divisible by 5 or contains the digit '5'.
    Takes in n(int)
    Return a bool
    Every number that is not divisible by 5 or contains 5 returns false
    """
    # Condition 1: Divisible by 5
    if n % 5 == 0:
        return True
    if '5' in str(n):
        return True
    
    return False

def delete5():
    for i in range(1,101):
        if isdigit5(i):
            continue
        else:
            print(i)
    
if __name__ == "__main__":
    delete5()