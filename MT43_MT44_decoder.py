# -*- coding: utf-8 -*-
"""
This is the decoder for QZSS L1S MT43 MT44

@author: Allystar Technology Co. Limited

"""
#input_path_read = "D:/cherry/QZSS L1S/nmea/COM11(Enhanced)_2024-05-20_14.50.25.GPS"  
#input_path_write = "D:/cherry/QZSS L1S/decoded messages/decode0517.txt" 

from MT43_decoder import decoder_MT43
from MT44_decoder import decoder_MT44

'''
def bool_print_msg(hex_data):
    print_it = True
    num = hex_data.count("0")
    if num > 25:
        print_it = False
    return print_it
'''        

def decoder_MT43_MT44(message, file_path_write):
    #Split the message into lines
    lines = message.split("\n")
    count = 0
    for line in lines:
        if line.startswith("$QZQSM,"):
            char_data = line[10:73].strip()  # Remove the header "$QZQSM,"
            #print(char_data)
            checksum = line[74:].strip()
            #Better add codes for checking the checksum, not skip for simplicity
            #binary_data = binascii.unhexlify(hex_data).decode()
            hex_data =  hex(int(char_data, 16))[2:].upper()
            #print(hex_data)
            binary_data = bin(int(hex_data, 16))[2:].zfill(len(hex_data) * 4)
            #print(binary_data)
            message_type = int(binary_data[8:14],2)
            print_message=''
            if message_type == 43:
                print_message = decoder_MT43(binary_data[14:250])
            elif message_type == 44:                
                #print(binary_data)
                print_message = decoder_MT44(hex_data, binary_data[14:250])
                if not(print_message == ''):
                    count += 1
                    #print_message += "count:" + str(count)+"\n"
            else:
                print_message += "Error in message type."
                
            try:
                    with open(file_path_write, "a", encoding="utf-8") as file:
                        file.write(print_message)
                        
            except IOError:
                print("Error writing to file.")



if __name__ == "__main__":
    input_path_read = input("Enter the path of the nmea.txt file: ")
    input_path_write = input("Enter the path of the file to store the MT43 MT44 decoded messages: ")
    
    try:
        with open(input_path_read, "r", encoding='latin-1') as file:
            read_contents = file.read()
    except FileNotFoundError:
        print("File not found.")
    
    with open(input_path_write, "w", encoding="utf-8"):
        pass  # Create an empty file
        
    decoder_MT43_MT44(read_contents, input_path_write)