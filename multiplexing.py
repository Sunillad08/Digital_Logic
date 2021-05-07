## Designing multiplexing logic for 
'''
1. multiplexer
2. demultiplexr
'''

# format to define functions

'''
define function(type , inputs , selection pins , Enabler)
type : 2:1 or 8:3 , etc
inputs : inputs for pins
selection pins : to select pin
enable : to activate circuit i.e 0 (optional)
return output in list/tuple (decide!)
'''
import math

# checking and raising errors
def check_valid_multiplexer_data(data , level):
    if level != 2 ** (round(math.sqrt(level))):
        approx_value = 2 ** (round(math.sqrt(level)))
        raise ValueError(f"Invalid value : Do you mean {approx_value} ?") # invalid level
    elif isinstance(data , list) != True:
        raise SyntaxError("Input should be in list or array") # input not in list
    elif level != len(data):
        raise ValueError(f"Insuffiecient data , exact {len(data)+1} required") # insuffient data

class multiplexer():

    # initializing multiplexer
    def __init__(self , data , level):
        check_valid_multiplexer_data(data, level)
        self.data = data
        self.level = level
        self.select_pins_count = round(math.log2(level))

    # returns input based on selector pins status
    def get_input(self , selectpins):
        # list format compulsion
        if isinstance(selectpins , list):
            # binary only
            for i in selectpins:
                if i not in [0,1]:
                    raise ValueError("Invalid value for select pins")
            
            # suffiecient pins count checking
            if len(selectpins) != self.select_pins_count:
                if len(selectpins) > self.select_pins_count:
                    raise ValueError(f"Too many values for select pins , only {self.select_pins_count} required")
                else:
                    raise ValueError(f"Insuffient values for select pins , {self.select_pins_count} required")
            
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
        

if __name__ == "__main__":
    m = multiplexer([0,1,0,1,1,1,1,1] , 8)
    print(m.get_input([0,1,0]))
    print(m.update_data(2 , 1))
    print(m.get_input([0,1,0]))