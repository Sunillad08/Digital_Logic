class shift_register_SIPO():
    
    def __init__(self,level,inputno = None):
        self.level = level
        self.inputno = inputno
        
    
    def sr_set(self,inputno):
        
        #list input 
        if (isinstance(inputno, list)):
            if(len(inputno) == self.level):
                for bin_in in inputno:
                    if bin_in not in [0,1]:
                        raise ValueError("Invalid value for input")
            else:
                raise ValueError("Number of input bits is not equal to the number of flip flops")
        else:
            raise ValueError("Input must be in a list format")
        self.inputno = inputno
        
                
                
    def sr_get(self,clock):
        
        if(isinstance(clock,int)):
            if (clock < 0):
                raise ValueError("Clock pulses are not negative")
            elif (clock >= self.level):
                clock = self.level - 1
                
        else:
            raise ValueError("The Nth clock pulse should be an integer")
        
        input_cp = self.inputno.copy()
        og_list = []
        for i in range(clock + 1):
            
            #start from the least significant bit
            og_list.insert(0,input_cp[-1])
            input_cp.pop()
           
        if(len(og_list)  < self.level):
            for val in range(self.level - len(og_list)):
                og_list.append(0)
                

        return(og_list)  
        
            
            

class shift_register_PISO():
    
    def __init__(self,level,inputno = None):
        self.level = level
        self.inputno = inputno
        
    
    def sr_set(self,inputno):
        
        #list input 
        if (isinstance(inputno, list)):
            if(len(inputno) == self.level):
                for bin_in in inputno:
                    if bin_in not in [0,1]:
                        raise ValueError("Invalid value for input")
            else:
                raise ValueError("Number of input bits is not equal to the number of flip flops")
        else:
            raise ValueError("Input must be in a list format")
        self.inputno = inputno
        
                
                
    def sr_get(self,clock):
        
        if(isinstance(clock,int)):
            if (clock < 0):
                raise ValueError("Clock pulses are not negative")
            elif (clock >= self.level):
                clock = self.level - 1
                
        else:
            raise ValueError("The Nth clock pulse should be an integer")
        
        input_cp = self.inputno.copy()
        og_list = []
        for i in range(clock + 1):
            
            #start from the least significant bit
            og_list.insert(0,input_cp[-1])
            input_cp.pop()
           
        if(len(og_list)  < self.level):
            for val in range(self.level - len(og_list)):
                og_list.append(0)
                
        
        return(og_list)  
        
class shift_register_SISO():
    
    def __init__(self,level,inputno = None):
        self.level = level
        self.inputno = inputno
        
    
    def sr_set(self,inputno):
        
        #list input 
        if (isinstance(inputno, list)):
            if(len(inputno) == self.level):
                for bin_in in inputno:
                    if bin_in not in [0,1]:
                        raise ValueError("Invalid value for input")
            else:
                raise ValueError("Number of input bits is not equal to the number of flip flops")
        else:
            raise ValueError("Input must be in a list format")
        self.inputno = inputno
        
                
                
    def sr_get(self,clock):
        
        if(isinstance(clock,int)):
            if (clock < 0):
                raise ValueError("Clock pulses are not negative")
            elif (clock >= self.level):
                clock = self.level - 1
                
        else:
            raise ValueError("The Nth clock pulse should be an integer")
        
        input_cp = self.inputno.copy()
        og_list = []
        for i in range(clock + 1):
            
            #start from the least significant bit
            og_list.insert(0,input_cp[-1])
            input_cp.pop()
           
        if(len(og_list)  < self.level):
            for val in range(self.level - len(og_list)):
                og_list.append(0)
                

        return(og_list) 
            

class shift_register_PIPO():
    
    def __init__(self,level,inputno = None):
        self.level = level
        self.inputno = inputno
        
    
    def sr_set(self,inputno):
        
        #list input 
        if (isinstance(inputno, list)):
            if(len(inputno) == self.level):
                for bin_in in inputno:
                    if bin_in not in [0,1]:
                        raise ValueError("Invalid value for input")
            else:
                raise ValueError("Number of input bits is not equal to the number of flip flops")
        else:
            raise ValueError("Input must be in a list format")
        self.inputno = inputno
        
                
                
    def sr_get(self,clock):
        
        if(isinstance(clock,int)):
            if (clock < 0):
                raise ValueError("Clock pulses are not negative")
            else:
                return(self.inputno.copy())
                
        else:
            raise ValueError("The Nth clock pulse should be an integer")
        
