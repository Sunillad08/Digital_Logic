# Design counters
'''
1. Ring counter
2. Jonhson counter
3. Ripple counter
'''

from Gates import logic_not
from Conversion import decimal_to_binary , binary_to_decimal

'''Ring counter'''
class counter_ring:

    # initializing counter
    def __init__(self , count , start = None):
        if start == None:
            start = [0 for i in range(count)]
            start[0]=1
        elif isinstance(count,int) == False:
            raise ValueError("Invalid value for count")
        elif isinstance(start , list) == False:
            raise ValueError("Invalid value for start , Values should be in list")
        elif len(start) != count:
            raise ValueError(f"Invalid values for start , Exact {count} required")
        
        for i in start:
            if i not in [0,1]:
                raise ValueError("Binary values only")
                
        if start.count(1) != 1:
            raise ValueError("Invalid starting Value , There will be only one 1")
 
        self.count_bits = count
        self.start = start
        self.__current_value = start

    # to get next value
    def next(self):
        temp = self.__current_value.pop()
        self.__current_value.insert(0,temp)
        return self.__current_value

    # to get current value
    def now(self):
        return self.__current_value

'''Jonhson counter or twisted ring counter'''
class counter_johnson:

    # initializing counter
    def __init__(self , count , start = None):
        if start == None:
            start = [0 for i in range(count)]
        elif isinstance(count,int) == False:
            raise ValueError("Invalid value for count")
        elif isinstance(start , list) == False:
            raise ValueError("Invalid value for start , Values should be in list")
        elif len(start) != count:
            raise ValueError(f"Invalid values for start , Exact {count} required")
        
        for i in start:
            if i not in [0,1]:
                raise ValueError("Binary values only")
        
        temp = start[0]
        flag = False
        for i in range(len(start)):
            if start[i] == temp:
                continue
            else:
                if flag:
                    raise ValueError("Invalid value for Johnson counter")
                flag = True
                temp = start[i]

        self.count_bits = count
        self.start = start
        self.__current_value = start

    # to get next value
    def next(self):
        temp = self.__current_value.pop()
        self.__current_value.insert(0,logic_not(temp))
        return self.__current_value
    
    # to get current value
    def now(self):
        return self.__current_value

'''Ripple counter or basic binary counter'''
class counter_ripple:

    # initializing counter
    def __init__(self , count , start = None):
        if start == None:
            start = [0 for i in range(count)]
        elif isinstance(count,int) == False:
            raise ValueError("Invalid value for count")
        elif isinstance(start , list) == False:
            raise ValueError("Invalid value for start , Values should be in list")
        elif len(start) != count:
            raise ValueError(f"Invalid values for start , Exact {count} required")
        
        for i in start:
            if i not in [0,1]:
                raise ValueError("Binary values only")
 
        self.count_bits = count
        self.start = start
        self.__current_value = start
        

    # to get next value
    def next(self):

        decimal = binary_to_decimal(self.__current_value)
        decimal += 1

        if decimal >= 2**(self.count_bits):
            decimal = 0
        
        temp = decimal_to_binary(decimal)
        temp = [str(i) for i in str(temp)] 
        
        while len(temp) < len(self.__current_value):
            temp.insert(0 , "0")
        
        self.__current_value = [int(i) for i in temp]
        return self.__current_value

    # to get current value
    def now(self):
        return self.__current_value


if __name__ == "__main__":
    '''Tested counter and currently works as charm'''
    n = counter_ripple(2)
    print(n.now())
    for i in range(25):
        print(n.next())
         

