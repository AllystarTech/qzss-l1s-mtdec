# -*- coding: utf-8 -*-

#  File Name: MT43_M44_decoder.py
# -----------------------------------------------------------------------------
#  This is the decoder for QZSS L1S MT43 MT44
#
#  Copyright (c) 2024 Allystar Technology Co. Limited
#
#  SPDX-License-Identifier: MIT
# -----------------------------------------------------------------------------
import sys
import datetime
import warnings

#sys.path.append("./Jupyter/code")
#input_path_read = "D:/cherry/QZSS L1S/japan test 0701/COM18(Enhanced)_115200_2024-07-01_15.33.47.GPS"  

input_path_read = "D:/cherry/QZSS L1S/nmea/0627_murata_shanghai.GPS"  
input_path_write = "D:/cherry/QZSS L1S/decoded messages/decode.txt"

from MT43_decoder import decoder_MT43
from MT44_decoder import decoder_MT44 

def decoder_MT43_MT44(message, file_path_write):
    
    #Split the message into lines
    lines = message.split("\n")
    count = 0
    first_line_GNRMC = None
    last_line_GNRMC = None
    for line in lines:        
        if line.startswith("$GNRMC,"):
            if first_line_GNRMC is None:
                first_line_GNRMC = line.strip()
            last_line_GNRMC = line.strip()
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
                print_message = decoder_MT44(binary_data[14:250])
            else:
                print_message += '' #"Error in message type."
            if print_message != '':
                print_message += "----------\n"

            try:
                with open(file_path_write, "a", encoding="utf-8") as file:
                    #file.write(line + '\n'+ print_message)
                    file.write(print_message)
                        
            except IOError:
                print("Error writing to file. ")

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
    #log_information(first_line_GNRMC, last_line_GNRMC)