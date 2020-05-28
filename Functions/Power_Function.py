#Calculate the specified power of a specified base

def power_function (base, power):
    result = 1
    for counter in range(power): 
        result *= base 
    return result