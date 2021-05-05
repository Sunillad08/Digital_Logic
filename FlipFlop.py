## Designing flip flop logic for 
'''
1. NOR Latch
2. NAND latch
3. SR flip flop
4. D flip flop
5. JK flip flop
6. Master slave JK flip flop
7. T flip flop
'''

# format to define functions

'''
define function(Input1 , Input2 , clock)
Input1 and Input2 : *args
clock : *args should have same length as Inputs
return output in list/tuple (decide!)
'''

'''
Normalize values above 1 to 1 and below 1 to 0
'''

from main_functions import *


def nor_latch(s , r , clock):

    # to check input is int or float only!
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return -1
        else:
            '''NOR Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return -1 # last state
                else:
                    return 0 # 0
            else:
                if r == 0:
                    return 1 # 1
                else:
                    return None # race around

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
        
def nand_latch(s , r , clock):

    # to check input is int or float only!
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return -1
        else:
            '''NAND Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return None # race around
                else:
                    return 1 # 0
            else:
                if r == 0:
                    return 0 # 1
                else:
                    return -1 # last state

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
                

if __name__ == "__main__":

    def check_possible_combinations(func):
        print("Clock : 0")
        print(func(0 , 0, 0))
        print(func(0 , 1, 0))
        print(func(1 , 0, 0))
        print(func(1 , 1, 0))
        print("Clock : 1")
        print(func(0 , 0, 1))
        print(func(0 , 1, 1))
        print(func(1 , 0, 1))
        print(func(1 , 1, 1))
        print(f"Ended checking {func.__name__}\n")
    
    check_possible_combinations(nor_latch)
    check_possible_combinations(nand_latch)