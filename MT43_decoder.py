# -*- coding: utf-8 -*-
"""
This is the decoder for QZSS L1S MT43

@author: Allystar Technology Co. Limited
"""
from MT43_marine_decoder import mt43_marine_dec

def decoder_MT43(binary_data):
    Rc = int(binary_data[0:3], 2)
    Dc = int(binary_data[3:7], 2)
    #TODO: Add other Dc type
    if Dc == 1:
        print_message = ''
        return print_message
    elif Dc == 2:
        print_message = ''
        return print_message        
    elif Dc == 3:
        print_message = ''
        return print_message
    elif Dc == 4:
        print_message = ''
        return print_message
    elif Dc == 5:
        print_message = ''
        return print_message
    elif Dc == 6:
        print_message = ''
        return print_message
    elif Dc == 7:
        print_message = ''
        return print_message
    elif Dc == 8:
        print_message = ''
        return print_message
    elif Dc == 9:
        print_message = ''
        return print_message
    elif Dc == 10:
        print_message = ''
        return print_message
    elif Dc == 11:
        print_message = ''
        return print_message
    elif Dc == 12:
        print_message = ''
        return print_message
    elif Dc == 13:
        print_message = ''
        return print_message
    elif Dc == 14:
        print_message = mt43_marine_dec(binary_data[7:])
        return print_message
    else:
        return "MT43: invalid type"
