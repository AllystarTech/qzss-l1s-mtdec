# -*- coding: utf-8 -*-

#  File Name: MT44 CAMF decoder.py
# -----------------------------------------------------------------------------
#  MT44 CAMF decoder
#
#  Copyright (c) 2024 Allystar Technology Co. Limited
#
#  SPDX-License-Identifier: MIT
# -----------------------------------------------------------------------------

class CAMF:
    def __init__(self):
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.A4 = None
        self.A5 = None
        self.A6 = None
        self.A7 = None
        self.A8 = None
        self.A9 = None
        self.A10 = None
        self.A11 = None
        self.A12 = None
        self.A13 = None
        self.A14 = None
        self.A15 = None
        self.A16 = None
        self.A17 = None
        self.A18 = None
    def printing(self):
        print("A1: "+str(bin(self.A1)))
        print("A2: "+str(bin(self.A2)))
        print("A3: "+str(bin(self.A3)))
        print("A4: "+str(bin(self.A4)))
        print("A5: "+str(bin(self.A5)))
        print("A6: "+str(bin(self.A6)))
        print("A7: "+str(bin(self.A7)))
        print("A8: "+str(bin(self.A8)))
        print("A9: "+str(bin(self.A9)))
        print("A10: "+str(bin(self.A10)))
        print("A11: "+str(bin(self.A11)))
        print("A12: "+str(bin(self.A12)))
        print("A13: "+str(bin(self.A13)))
        print("A14: "+str(bin(self.A14)))
        print("A15: "+str(bin(self.A15)))
        print("A16: "+str(bin(self.A16)))
        print("A17: "+str(bin(self.A17)))
        print("A18: "+str(bin(self.A18)))



def MT44_CAMF_dec(binary_data):
    table = {
        'A1': 2,
        'A2': 9,
        'A3': 5,
        'A4': 7,
        'A5': 2,
        'A6': 1,
        'A7': 14,
        'A8': 2,
        'A9': 1,
        'A10': 3,
        'A11': 10,
        'A12': 16,
        'A13': 17,
        'A14': 5,
        'A15': 5,
        'A16': 6,
        'A17': 2,
        'A18': 15
    }

    extracted_values = CAMF()

    start = 0
    for parameter, num_bits in table.items():
        end = start + num_bits
        value = int(binary_data[start:end], 2)
        setattr(extracted_values, parameter, value)
        start = end

    return extracted_values

