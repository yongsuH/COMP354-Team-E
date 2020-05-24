# Algorithm
# 1. Calculate Mean
# 2. Sum the absolute values of all values minus the mean
# 3. Divide the sum by the number of values

# Primary Algoirthm
# -----------------
def mean_absolute_deviation(input):
    # Local variables
    mean = calculate_mean(input)
    dividend = 0
    diviser = calculate_length(input)

    # Calculate the dividend
    for x in input:
        dividend += absolute_value(x - mean)

    # Return the Mean Absolute Deviation
    return (float(dividend) / diviser)
        
# Helper Functions
# ----------------
def calculate_mean(input): 
    sum = 0
    for x in input:
        sum += x
    return (sum / calculate_length(input))

def absolute_value(input):
    if input < 0:
        return -input
    else:
        return input

def calculate_length(input):
    n = 0
    for x in input:
        n = n + 1
    return n

# Test Functions
# --------------

# Should equal 127.2
x = mean_absolute_deviation([600, 470, 170, 430, 300])

# Should equal 3.75
y = mean_absolute_deviation([3, 6, 6, 7, 8, 11, 15, 16])

print(x)
print(y)
