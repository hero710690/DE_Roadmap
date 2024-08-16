def isArmstrongNumber(num):
    str_num = str(num)
    n = len(str_num)
    sum = 0
    for i in range(n):
        sum+=int(str_num[i])**n
    if sum == num:
        return True
    else:
        return False

if __name__ == '__main__':
    # Example usage:
    print(isArmstrongNumber(153))  # Output: True
    print(isArmstrongNumber(9474))  # Output: True
    print(isArmstrongNumber(123))  # Output: False