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

13.Binary to BCD 
14.Binary to gray
15.BCD to Binary
16.BCD to gray
17.Gray to Binary
19.Gray to BCD
'''
'''Checking valuses are valid or not'''
def _check_binary(binary):
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

    return binary

def _check_octal(octal):
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
    
    return octal

def _check_decimal(decimal):
    if isinstance(decimal , str):
        if decimal.isdigit():
            decimal = int(decimal)
        else:
            raise ValueError("Invalid Decimal value")
        
    if isinstance(decimal , int) == False:
        raise ValueError("Invalid Decimal value")

    return decimal

def _check_hexadecimal(hexadecimal):
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
    
    return hexadecimal

def _check_bcd(bcd):
    bcd = _check_binary(bcd)
    if(len(bcd)%4 != 0):
        raise ValueError('Invalid BCD value : length should be multiple of 4')

    return bcd

def _check_gray(gray):
    return _check_binary(gray)

'''Binary to other bases conversion'''
def binary_to_decimal(binary):
    binary = _check_binary(binary)
    
    binary = "".join([str(i) for i in binary])

    return int(binary , 2)

def binary_to_hexadecimal(binary):
    binary = _check_binary(binary)
    
    binary = "".join([str(i) for i in binary])
    '''binary -> decimal ->hexadecimal'''
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)

    return hexadecimal

def binary_to_octal(binary):
    binary = _check_binary(binary)
    
    binary = "".join([str(i) for i in binary])
    '''binary -> decimal ->hexadecimal'''
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)

    return octal

'''Decimal to other bases conversion'''
def decimal_to_binary(decimal):
    decimal = _check_decimal(decimal)

    return bin(decimal).replace("0b" , "")

def decimal_to_hexadecimal(decimal):
    decimal = _check_decimal(decimal)

    return hex(decimal).replace("0x" , "")

def decimal_to_octal(decimal):
    decimal = _check_decimal(decimal)

    return oct(decimal).replace("0o" , "")

'''Octal to other bases conversion'''
def octal_to_decimal(octal):
    octal = _check_octal(octal)
    octal = "".join([str(i) for i in octal])

    return int(octal , 8)

def octal_to_binary(octal):
    octal = _check_octal(octal)
    
    '''octal -> decimal ->  binary'''
    octal = "".join([str(i) for i in octal])
    decimal = octal_to_decimal(octal)
    binary = decimal_to_binary(decimal)

    return binary

def octal_to_hexadecimal(octal):
    octal = _check_octal(octal)
    
    '''octal -> decimal -> hexadecimal'''
    octal = "".join([str(i) for i in octal])
    decimal = octal_to_decimal(octal)
    hexadecimal = decimal_to_hexadecimal(decimal)

    return hexadecimal

'''Hexadecimal to other bases conversion'''
def hexadecimal_to_decimal(hexadecimal):
    hexadecimal = _check_hexadecimal(hexadecimal)
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    return int(hexadecimal , 16)

def hexadecimal_to_binary(hexadecimal):
    hexadecimal = _check_hexadecimal(hexadecimal)
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    '''hexadecimal -> decimal -> binary'''
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)

    return binary

def hexadecimal_to_octal(hexadecimal):
    hexadecimal = _check_hexadecimal(hexadecimal)
    
    hexadecimal = "".join([str(i) for i in hexadecimal])
    hexadecimal.lower()

    '''hexadecimal -> decimal -> octal'''
    decimal = hexadecimal_to_decimal(hexadecimal)
    octal = decimal_to_octal(decimal)

    return octal

'''Binary to other codes'''
def binary_to_bcd(binary):
    binary = _check_binary(binary)

    bcd = []
    decimal = binary_to_decimal(binary)
    if decimal == 0:
        return '0000'
    
    while (decimal > 0):
        temp = decimal % 10
        decimal = decimal // 10
        bcd_temp = decimal_to_binary(temp)
        if len(bcd_temp) < 4:
            bcd_temp = '0'*(4-len(bcd_temp)) + bcd_temp
        bcd.append(bcd_temp)
        
    return " ".join(bcd[::-1])

def binary_to_gray(binary):
    binary = _check_binary(binary)

    if isinstance(binary[0],str):
        binary.insert(0,'0')
    else:
        binary.insert(0,0)
    
    gray = []
    if len(binary) < 2:
        return binary
    for i in range(len(binary)-1):
        if binary[i] == binary[i+1]:
            gray.append(str(0))
        else:
            gray.append(str(1))

    return "".join(gray)

'''BCD to other codes'''
def bcd_to_binary(bcd):
    bcd = _check_bcd(bcd)

    decimal = 0
    for i in range(0,len(bcd)-1,4):
        decimal = decimal*10 + binary_to_decimal(bcd[i:i+4])
    
    return decimal_to_binary(decimal)

def bcd_to_gray(bcd):
    bcd = _check_bcd(bcd)

    '''bcd -> binary -> gray'''
    binary = bcd_to_binary(bcd)
    return binary_to_gray(binary)

'''Gray to other codes'''
def gray_to_binary(gray):
    gray = _check_gray(gray)
    if isinstance(gray[0],int):
        gray = [str(i) for i in gray]
    binary =[]
    temp = gray[0]
    binary.append(temp)
    for i in range (1,len(gray)):
        if temp == gray[i]:
            temp = '0'
        else:
            temp = "1"
        binary.append(temp)
    return "".join(binary)

def gray_to_bcd(gray):
    gray = _check_gray(gray)

    '''gray -> binary -> bcd'''
    binary = gray_to_binary(gray)
    return binary_to_bcd(binary)


if __name__ == "__main__": 
    '''Tested everything!!'''
    # data = ["0" , "1" , "10" , "11" , ['1' , '0' , '0' , '0'] , [1,0,1,0] , "1111"]
    # for i in data:
    #     print(binary_to_bcd(i))
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
    # data = ["0" , "1" , "10" , "11" , ['1' , '0' , '0' , '0'] , [1,0,1,0] , "1111"]
    # for i in data:
    #     print(binary_to_gray(i))
    # print(bcd_to_binary([1,0,0,0,1,0,0,0]))
    # print(bcd_to_gray([1,0,0,0]))
    # print(gray_to_binary('110111'))
    # print(gray_to_bcd('1100'))
