'''
display terminals
type:class\n
name-format: [name]\n
Seven segment display
'''

'''
  ###
 #   #
 #   #
  ###  
 #   #
 #   #
  ###  

Output : 0-9 and a-f same as A-F
'''
'''Seven segment display'''
class seven_segment_display():
    
    # to check inputs are valid or not
    def __check_binary(data):
        if len(data) != 7:
            raise ValueError("Invalid amount of values , exact 7 required!")
        for i in data:
            if i not in [0,1]:
                raise ValueError("Invalid Values , Binary only")

    def __init__(self,data):
        seven_segment_display.__check_binary(data)
        self.input = data 

    def get_display_output(self):

        ## string formats
        final_string = ["     ","     ","     ","     ","     ","     ","     "]
        horizontal_rows = " ### "
        vertical_rows = [(("#   #"),("#   #")) , (("#    "),("#   " )),(( "    #"),("    #"))]

        # flags to check status
        middle_string_flag = False
        vertical_string_1_flag = False # if upper left vertical line is on (f)
        vertical_string_2_flag = False # if upper right vertical line is on (b)

        # handling horizonatal rows (a , d , g)
        if self.input[0] == 1: # a
            final_string[0] = horizontal_rows
        
        if self.input[3] == 1: # d
            final_string[-1] = horizontal_rows
            
        if self.input[6]: # g
            final_string[3] = horizontal_rows
            middle_string_flag = True

        # handling upper 2 vertical rows (f , b)
        if self.input[5] == 1:
            if self.input[1] == 1:
                final_string[1:3] = vertical_rows[0]
                vertical_string_1_flag = True
                vertical_string_2_flag = True
            
            else:
                final_string[1:3] = vertical_rows[1]
                vertical_string_1_flag = True
                
        else:
            if self.input[1] == 1:
                final_string[1:3] = vertical_rows[2]
                vertical_string_2_flag = True
                

        # handling lower 2 vertical rows (e , c)
        if self.input[4] == 1:
            if self.input[2] == 1:
                final_string[4:6] = vertical_rows[0]

                # padding to join vertical lines if both on
                if middle_string_flag == False:
                    temp = list(final_string[3])
                    if vertical_string_1_flag == True:
                        temp[0] = "#"
                    if vertical_string_2_flag == True:
                        temp[-1] = "#"
                    final_string[3] = "".join(temp)

            else:
                final_string[4:6] = vertical_rows[1]

                # padding to join vertical lines if both on
                if middle_string_flag == False:
                    temp = list(final_string[3])
                    if vertical_string_1_flag == True:
                        temp[0] = "#"
                    final_string[3] = "".join(temp)
        else:
            if self.input[2] == 1:
                final_string[4:6] = vertical_rows[2]

                # padding to join vertical lines if both on
                if middle_string_flag == False:
                    temp = list(final_string[3])
                    if vertical_string_2_flag == True:
                        temp[-1] = "#"
                    final_string[3] = "".join(temp)

        return "\n".join(final_string)

    def update_pins(self,data):
        seven_segment_display.__check_binary(data)
        self.input = data
    
    def display_number(self,number):
        # check hexadecimal only
        if number not in [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","A","B","C","D","E","F"]:
            raise ValueError("Invalid value , 0-9 and a-f values only!")
        
        # designing pattern stored
        designs_for_numbers = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
        designs_for_characters = [[1,1,1,0,1,1,1],[0,0,1,1,1,1,1],[1,0,0,1,1,1,0],[0,1,1,1,1,0,1],[1,0,0,1,1,1,1],[1,0,0,0,1,1,1]]

        # return display output for numbers
        if str(number).isdigit():
            self.input = designs_for_numbers[number]
            return self.get_display_output()
        # returns display output for characters A-F or a-f
        else:
            number = number.upper()
            self.input = designs_for_characters[ord(number) - 65]
            return self.get_display_output()
