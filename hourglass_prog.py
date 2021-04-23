start = 7           # start point 
step  = 2           # step difference from each row
mid_point = False   # mid point check flag

# hourglass function definition
def hourglass(number,space_val):
    global mid_point
    space_symbol = ' '

    print (space_val*space_symbol,(" ".join( "*" for i in range(number)))) # line to print the stars

    # check condition to see if the number reached the mid point of the hour glass    
    if (number == 1 or number == 0 and (mid_point == False)):
        mid_point = True
    
    if (mid_point == True and (number < start)):
        hourglass(number+step,space_val-2)      # lower half recursive function call
    elif(mid_point == False):
        hourglass(number-step,space_val+2)      # upper half recursive function call
    else:
        pass


hourglass(start,0)                              # hourglass function call
