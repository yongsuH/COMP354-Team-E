#Goal: Calculate the specified power of a specified base
#Method: Exponentiation by squaring 

def power_function (base, power):
    #Case 1: Power is a negative number
    if (power<0):
        base = 1/base
        power = -power

    #Case 2: Power is equal to 0
    if (power==0):
        return 1
    
    #Case 3: Power is equal to 1
    if (power==1):
        return base
    
    #Case 4: Power is a positive number greater than 1
    result=1
    while(power>1):
        if(power%2==0):
            base=(base*base)
            power=power/2
        else: 
            result=base*result
            base=base*base
            power=(power-1)/2
    
    return base*result