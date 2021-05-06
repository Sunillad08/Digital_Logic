#All functions used in other program files are stored here

#Normalise Logic Values : Changes values to binary data for logic gates to work

def normalize_logic_values(*args):
    args = list(args)
    for i in range(len(args)):
        if args[i] > 0:
            args[i] = 1
        elif args[i] < 1:
            args[i] = 0
    return args

def valid_value(*args):
    if(isinstance(args,int) and isinstance(args,float)):
        return(True)
