'''Functions to validate values'''

'''Correction to binary values'''
def normalize_logic_values(*args):
    args = list(args)
    for i in range(len(args)):
        if args[i] > 1.0:
            args[i] = 1
        else:
            args[i] = 0
    return args

'''Correct format : int or float'''
def valid_value(*args):
    bgr = [(isinstance(all_values,int) or isinstance(all_values,float)) for all_values in args] 
    if(all(bgr)):
        return(True)
    else:
        return(False)
