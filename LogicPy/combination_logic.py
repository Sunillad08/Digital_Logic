## Designing multiplexing logic for 
'''
combination_logic
type:class\n
name-format: [name]\n
multiplexer\n
demultiplexr\n
encoder\n
decoder
'''

import math

'''Multiplexers of n-bits'''
class multiplexer():
    # multiplexer with 2,4,8,16,32,64,... levels
    # checking and raising errors
    def __check_valid_multiplexer_data(data , level):
        if level != 2**(round(math.log2(level))):
            approx_value = 2**round(math.log2(level))
            raise ValueError(f"Invalid value : Do you mean {approx_value} ?") # invalid level
        elif isinstance(data , list) != True:
            raise SyntaxError("Input should be in list or array") # input not in list format
        elif level != len(data):
            raise ValueError(f"Insuffiecient data , exact {level} required") # insuffient data
    
    # initializing multiplexer
    def __init__(self , data , level):
        multiplexer.__check_valid_multiplexer_data(data, level)
        self.data = data
        self.level = level
        self.__select_pins_count = round(math.log2(level))

    # returns input based on selector pins status
    def get_input(self , selectpins):
        # list format compulsion
        if isinstance(selectpins , list):
            # binary only
            for i in selectpins:
                if i not in [0,1]:
                    raise ValueError("Invalid value for select pins")
            
            # suffiecient pins count checking
            if len(selectpins) != self.__select_pins_count:
                if len(selectpins) > self.__select_pins_count:
                    raise ValueError(f"Too many values for select pins , only {self.__select_pins_count} required")
                else:
                    raise ValueError(f"Insuffient values for select pins , {self.__select_pins_count} required")
            
            # main logic
            data_pin_number = 0
            selectpins.reverse()
            for i in range(len(selectpins)):
                data_pin_number += selectpins[i] * (2**i)
             
            try:
                return self.data[data_pin_number]
            except IndexError:
                print(f"Error occured , wrong value {data_pin_number}")
            except :
                print("Error")

        else:
            raise SyntaxError("Input should be in list or array")

    def update_data(self, data_pin , new_value):
        # binary only
        if new_value not in [0,1]:
            raise ValueError("Invalid Value , Binary values only")

        # data pin position confirmation
        if data_pin > self.level -1 or data_pin < 0:
            raise ValueError(f"Invalid data pin value , 0 to {self.level - 1} only")
        
        # updated value
        self.data[data_pin] = new_value

'''Demultiplexer of n-bits'''
class demultiplexer():
    # demultiplexer with 2,4,8,16,32,64,... levels 
    # checking and raising errors
    def __check_valid_demultiplexer_data(input_pin , level):
        if level != 2**(round(math.log2(level))):
            approx_value = 2**round(math.log2(level))
            raise ValueError(f"Invalid value : Do you mean {approx_value} ?") # invalid level
        elif input_pin not in [0,1]:
            raise SyntaxError("Input should be binary") # input not in binary format
    
    # initializing demultiplexer
    def __init__(self , input_pin , level):
        demultiplexer.__check_valid_demultiplexer_data(input_pin, level)
        self.input_pin = input_pin
        self.level = level
        self.__select_pins_count = round(math.log2(level))
        self.output_pins = [-1 for _ in range(level)] # disconnect state for every pin
        self.__current_pin = 0

    # switch input pin from 0 to 1 and vice verse
    def switch_input(self):
        self.input_pin = int(bool(self.input_pin))
        self.output_pins[self.current_pin] = self.input_pin

    # get current pin on which output is redirected
    def get_current_pin(self):
        return self.__current_pin
    
    # changes output pin which is connected to input pin
    def set_select_pin(self , selectpins):
        # list format compulsion
        if isinstance(selectpins , list):
            # binary only
            for i in selectpins:
                if i not in [0,1]:
                    raise ValueError("Invalid value for select pins")
            
            # suffiecient pins count checking
            if len(selectpins) != self.__select_pins_count:
                if len(selectpins) > self.__select_pins_count:
                    raise ValueError(f"Too many values for select pins , only {self.__select_pins_count} required")
                else:
                    raise ValueError(f"Insuffient values for select pins , {self.__select_pins_count} required")
            
            # main logic
            data_pin_number = 0
            selectpins.reverse()
            for i in range(len(selectpins)):
                data_pin_number += selectpins[i] * (2**i)
             
            try:
                self.output_pins[self.__current_pin] = -1 # deattach output pin
                self.__current_pin = data_pin_number
                self.output_pins[data_pin_number] = self.input_pin # connect new pin

            except IndexError:
                print(f"Error occured , wrong value {data_pin_number}")
            except :
                print("Error")
                print(data_pin_number)

        else:
            raise SyntaxError("Input should be in list or array")
        
    # get output pins status
    def get_output_pin(self):
        return tuple(self.output_pins) # returns all pins current status

'''Encoder of n-bits'''
class encoder():   
    # initializing encoder
    def __init__(self, level):
        self.level = level
        self.__output_pins_count = round(math.log2(level))

    def encoder_get(self, inputno):
        # list format compulsion
        if isinstance(inputno , list):
            # binary only
            for i in inputno:
                if i not in [0,1]:
                    raise ValueError("Invalid value for input pins")

            # suffiecient pins count checking
            if len(inputno) != self.level:
                if len(inputno) > self.level:
                    if(all(inputno[0:len(inputno) - self.level]) == 0):
                        outputno = inputno[len(inputno) - self.level:]
                        
                    else:
                        raise ValueError(f"Input value is large for a {self.level}:{self.__output_pins_count} encoder required")
                else:
                    outputno = inputno
                    bg = len(inputno)
                    for MSB_zero in range((self.level) - bg):
                        outputno.insert(0,0)

            else:
                outputno = inputno

            # main logic
            
            try:
                outputno.reverse()
                if(outputno.count(1) > 0):
                    op_val = outputno.index(1)
                    return(list(map(int,(bin(op_val))[2:])))
                else:
                    return(None)
            except :
                print("Error")

        else:
            raise SyntaxError("Input should be in list or array")

'''Decoder of n-bits'''
class decoder():         
    def __init__(self, level):
        self.level = level
        self.__output_pins_count = (2 ** self.level)

    def decoder_get(self, inputno):
        #For list input
        if isinstance(inputno , list):
            # binary only
            for i in inputno:
                if i not in [0,1]:
                    raise ValueError("Invalid value for input pins")

            # suffiecient pins count checking
            if len(inputno) != self.level:
                if len(inputno) > self.level:
                    if(all(inputno[0:len(inputno) - self.level]) == 0):
                        outputno = inputno[len(inputno) - self.level:]

                    
                    else:
                        raise ValueError(f"Input value is large for a {self.level}:{self.__output_pins_count} decoder required")
                else:
                    outputno = inputno
                    bg = len(inputno)
                    for MSB_zero in range((self.level) - bg):
                        outputno.insert(0,0)

            else:
                outputno = inputno

            #main logic
            output_pin_int = int("".join([str(integer) for integer in outputno]),2)
            output = []
            for val in range (self.__output_pins_count):
                if(val == output_pin_int):
                    output.append(1)
                else:
                    output.append(0)
            return(output)
                
        
        # for NoneType input
        elif inputno is None:
                outputno = []
                for zero_val in range (self.__output_pins_count):
                    outputno.append(0)

                return outputno

        else:
            raise SyntaxError("Input should be in list or array")
