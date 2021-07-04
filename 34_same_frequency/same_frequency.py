def frequency_counter(num):
    """Auxiliary function for same_frequency to get digit frequency for each number
    """
    count = {}
    for digit in str(num):
        count[digit] = count.get(digit, 0) + 1
    return count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return frequency_counter(num1) == frequency_counter(num2)