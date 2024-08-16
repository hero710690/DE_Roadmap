
def is_prime(num):
    if num <=1:
        return True
    if num%2 == 0 and num%3==0:
        return False
    i = 5
    while i < num:
        if num%i==0:
            return False
        i+=6
    return True

if __name__=='__main__':
    print(is_prime(23))  # Output: True
    print(is_prime(10))  # Output: False