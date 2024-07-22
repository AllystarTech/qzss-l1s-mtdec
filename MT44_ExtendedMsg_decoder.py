
# -*- coding: utf-8 -*-

#  File Name: MT44_ExtemdedMsg_decoder.py
# -----------------------------------------------------------------------------
#  MT44 Extended Message decoder
#
#  Copyright (c) 2024 Allystar Technology Co. Limited
#
#  SPDX-License-Identifier: MIT
# -----------------------------------------------------------------------------

class ExtendedMsg:
    def __init__(self, DCX_type):
        self.DCX_type = DCX_type
        if self.DCX_type == 0 or self.DCX_type == 2:
            self.EX1 = None
            self.EX2 = None
            self.EX3 = None
            self.EX4 = None
            self.EX5 = None
            self.EX6 = None
            self.EX7 = None
            self.Vn = None
        elif self.DCX_type == 1:
            self.EX8 = None
            self.EX9 = None
            self.EX10 = None
            self.Vn = None
        elif self.DCX_type == 3:
            self.EX11 = None 
            self.Vn = None

def MT44_ExtMsg_dec_0(binary_data, dcxtype):
    table = {
        'EX1': 16,
        'EX2': 1,
        'EX3': 17,
        'EX4': 17,
        'EX5': 5,
        'EX6': 5,
        'EX7': 7,
        'Vn': 6    
    }
    extracted_values = ExtendedMsg(dcxtype)

    start = 0
    for parameter, num_bits in table.items():
        end = start + num_bits
        value = int(binary_data[start:end], 2)
        setattr(extracted_values, parameter, value)
        start = end

    return extracted_values
    
def MT44_ExtMsg_dec_1(binary_data):
    table = {
        'EX8': 1,
        'EX9': 64,
        'EX10': 3,
        'Vn': 6
    }
    extracted_values = ExtendedMsg(1)

    start = 0
    for parameter, num_bits in table.items():
        end = start + num_bits
        value = int(binary_data[start:end], 2)
        setattr(extracted_values, parameter, value)
        start = end

    return extracted_values

def MT44_ExtMsg_dec_3(binary_data):
    table = {
        'EX11': 68,
        'Vn': 6
    }
    
    extracted_values = ExtendedMsg(3)

    start = 0
    for parameter, num_bits in table.items():
        end = start + num_bits
        value = int(binary_data[start:end], 2)
        setattr(extracted_values, parameter, value)
        start = end

    return extracted_values

def MT44_ExtMsg_dec(binary_data, DCX_type):
    extracted_values = 0
    if DCX_type == 0 or DCX_type == 2:
        extracted_values = MT44_ExtMsg_dec_0(binary_data, DCX_type)
    elif DCX_type == 1:
        extracted_values = MT44_ExtMsg_dec_1(binary_data)
    elif DCX_type == 3:
        extracted_values = MT44_ExtMsg_dec_3(binary_data)
    return extracted_values

