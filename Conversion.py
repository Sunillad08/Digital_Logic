'''
Converting bases
1.Binary to Decimal
2.Binary to Hexadecimal
3.Binary to Octal
4.Decimal to Hexadecimal
5.Decimal to Octal
6.Decimal to Binary
7.Octal to Hexadecimal
8.Octal to Decimal
9.Octal to Binary
10.Hexadecimal to Octal
11.Hexadecimal to Decimal
12.Hexadecimal to Binary
'''

'''Binary to other bases conversion'''
def binary_to_decimal(binary):
    if isinstance(binary , str):
        binary = list(binary)

    if isinstance(binary , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(binary[0] , int):
        valid_values = [0 , 1]
    else:
        valid_values = ['0' , '1']

    for i in binary:
        if i not in valid_values:
            raise ValueError("Invalid Binary value")
    
    binary = "".join([str(i) for i in binary])

    return int(binary , 2)

def binary_to_hexadecimal(binary):
    if isinstance(binary , str):
        binary = list(binary)

    if isinstance(binary , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(binary[0] , int):
        valid_values = [0 , 1]
    else:
        valid_values = ['0' , '1']

    for i in binary:
        if i not in valid_values:
            raise ValueError("Invalid Binary value")
    
    binary = "".join([str(i) for i in binary])
    '''binary -> decimal ->hexadecimal'''
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)

    return hexadecimal

def binary_to_octal(binary):
    if isinstance(binary , str):
        binary = list(binary)

    if isinstance(binary , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(binary[0] , int):
        valid_values = [0 , 1]
    else:
        valid_values = ['0' , '1']

    for i in binary:
        if i not in valid_values:
            raise ValueError("Invalid Binary value")
    
    binary = "".join([str(i) for i in binary])
    '''binary -> decimal ->hexadecimal'''
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)

    return octal

'''Decimal to other bases conversion'''
def decimal_to_binary(decimal):
    if isinstance(decimal , str):
        if decimal.isdigit():
            decimal = int(decimal)
        else:
            raise ValueError("Invalid Decimal value")
        
    if isinstance(decimal , int) == False:
        raise ValueError("Invalid Decimal value")

    return bin(decimal).replace("0b" , "")

def decimal_to_hexadecimal(decimal):
    if isinstance(decimal , str):
        if decimal.isdigit():
            decimal = int(decimal)
        else:
            raise ValueError("Invalid Decimal value")
        
    if isinstance(decimal , int) == False:
        raise ValueError("Invalid Decimal value")

    return hex(decimal).replace("0x" , "")

def decimal_to_octal(decimal):
    if isinstance(decimal , str):
        if decimal.isdigit():
            decimal = int(decimal)
        else:
            raise ValueError("Invalid Decimal value")
        
    if isinstance(decimal , int) == False:
        raise ValueError("Invalid Decimal value")

    return oct(decimal).replace("0o" , "")

'''Octal to other bases conversion'''
def octal_to_decimal(octal):
    if isinstance(octal , str):
        octal = list(octal)

    if isinstance(octal , int):
        octal = list(str(octal))

    if isinstance(octal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(octal[0] , int):
        valid_values = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]
    else:
        valid_values = ['0' , '1', '2' , '3' , '4' , '5' , '6' , '7']

    for i in octal:
        if i not in valid_values:
            raise ValueError("Invalid Octal value")
    
    octal = "".join([str(i) for i in octal])

    return int(octal , 8)

def octal_to_binary(octal):
    if isinstance(octal , str):
        octal = list(octal)

    if isinstance(octal , int):
        octal = list(str(octal))

    if isinstance(octal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(octal[0] , int):
        valid_values = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]
    else:
        valid_values = ['0' , '1', '2' , '3' , '4' , '5' , '6' , '7']

    for i in octal:
        if i not in valid_values:
            raise ValueError("Invalid Octal value")
    
    '''octal -> decimal ->  binary'''
    octal = "".join([str(i) for i in octal])
    decimal = octal_to_decimal(octal)
    binary = decimal_to_binary(decimal)

    return binary

def octal_to_hexadecimal(octal):
    if isinstance(octal , str):
        octal = list(octal)

    if isinstance(octal , int):
        octal = list(str(octal))

    if isinstance(octal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(octal[0] , int):
        valid_values = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]
    else:
        valid_values = ['0' , '1', '2' , '3' , '4' , '5' , '6' , '7']

    for i in octal:
        if i not in valid_values:
            raise ValueError("Invalid Octal value")
    
    '''octal -> decimal -> hexadecimal'''
    octal = "".join([str(i) for i in octal])
    decimal = octal_to_decimal(octal)
    hexadecimal = decimal_to_hexadecimal(decimal)

    return hexadecimal

'''Hexadecimal to other bases conversion'''
def hexadecimal_to_decimal(hexadecimal):
    if isinstance(hexadecimal , str):
        hexadecimal = list(hexadecimal)

    if isinstance(hexadecimal , int):
        hexadecimal = list(str(hexadecimal))

    if isinstance(hexadecimal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(hexadecimal[0] , int):
        valid_values = [0,1,2,3,4,5,6,7,8,9]
    else:
        valid_values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

    for i in hexadecimal:
        if i not in valid_values:
            raise ValueError("Invalid Hexadecimal value")
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    return int(hexadecimal , 16)

def hexadecimal_to_binary(hexadecimal):
    if isinstance(hexadecimal , str):
        hexadecimal = list(hexadecimal)

    if isinstance(hexadecimal , int):
        hexadecimal = list(str(hexadecimal))

    if isinstance(hexadecimal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(hexadecimal[0] , int):
        valid_values = [0,1,2,3,4,5,6,7,8,9]
    else:
        valid_values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

    for i in hexadecimal:
        if i not in valid_values:
            raise ValueError("Invalid Hexadecimal value")
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    '''hexadecimal -> decimal -> binary'''
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)

    return binary

def hexadecimal_to_octal(hexadecimal):
    if isinstance(hexadecimal , str):
        hexadecimal = list(hexadecimal)

    if isinstance(hexadecimal , int):
        hexadecimal = list(str(hexadecimal))

    if isinstance(hexadecimal , list) == False:
        raise SyntaxError("Values should be in list or string format!")
    
    if isinstance(hexadecimal[0] , int):
        valid_values = [0,1,2,3,4,5,6,7,8,9]
    else:
        valid_values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

    for i in hexadecimal:
        if i not in valid_values:
            raise ValueError("Invalid Hexadecimal value")
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    '''hexadecimal -> decimal -> octal'''
    decimal = hexadecimal_to_decimal(hexadecimal)
    octal = decimal_to_octal(decimal)

    return octal

if __name__ == "__main__": 
    '''Tested everything!!'''
    # data = ["0" , "1" , "10" , "11" , ['1' , '0' , '0' , '0'] , [1,0,1,0] , "1111"]
    # for i in data:
    #     print(binary_to_decimal(i))
    # data = ["0" , "1" , "10" , "11" , ['1' , '0' , '0' , '0'] , [1,0,1,0] , "1111"]
    # for i in data:
    #     print(binary_to_octal(i))
    # data = ["0" , "1" , "10" , "11" , ['1' , '0' , '0' , '0'] , [1,0,1,0] , "1111"]
    # for i in data:
    #     print(binary_to_hexadecimal(i))
    # for i in range(1,100):
    #     print(decimal_to_binary(str(i)))
    # for i in range(1,20):
    #     print(decimal_to_hexadecimal(i))
    # for i in range(1,20):
    #     print(decimal_to_octal(i))
    # data = [11,12,13,14,15,16,17,'20','21','22','77']
    # for i in data:
    #     print(octal_to_decimal(i))
    # data = [11,12,13,14,15,16,17,'20','21','22','77',00]
    # for i in data:
    #     print(octal_to_hexadecimal(i))
    # data = [0,1,2,3,4,5,6,7,11,12,13,14,15,16,17,'20','21','22','77']
    # for i in data:
    #     print(octal_to_binary(i))
    # data = [0,1,2,3,4,5,6,7,'a','b','c','D','e','F','10',11,12,13,14,15,16,17,'20','21','22','77','a','A','b','Abf' , '66']
    # for i in data:
    #     print(hexadecimal_to_decimal(i))
    # data = [0,1,2,3,4,5,6,7,8,9,'a','b','c','D','e','F','10',11,12,13,14,15,16,17,'20','21','22','77','a','A','b','Abf' , '66']
    # for i in data:
    #     print(hexadecimal_to_binary(i))
    # data = [0,1,2,3,4,5,6,7,8,9,'a','b','c','D','e','F','10',11,12,13,14,15,16,17,'20','21','22','77','a','A','b','Abf' , '66']
    # for i in data:
    #     print(hexadecimal_to_octal(i))