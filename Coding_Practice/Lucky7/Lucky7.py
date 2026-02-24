def isLucky(n: int) -> bool:
    """
    Returns True if n is divisible by 7
    OR contains the digit '7'.
    """
    
    # Condition 1: Divisible by 7
    if n % 7 == 0:
        return True

    # Condition 2: Contains digit '7'
    if '7' in str(n):
        return True

    return False


def luckyNumberPrinter():
    for i in range(1, 101):
        if isLucky(i):
            print("Lucky!")
        else:
            print(i)


if __name__ == "__main__":
    luckyNumberPrinter()