# -*- coding: utf-8 -*-
"""
MT44 SD decoder

@author: Allystar Technology Co. Limited
"""

class SD:
    def __init__(self):
        self.SDMT = None
        self.SDM1 = None
        self.SDM2 = None
        self.SDM3 = None
        self.SDM4 = None
        self.SDM5 = None
        self.SDM6 = None
        self.SDM7 = None
        self.SDM8 = None
        self.SDM9 = None
    def printing(self):
        print("SDMT: "+str(self.SDMT))
        print("SDM1: "+str(self.SDM1))
        print("SDM2: "+str(self.SDM2))
        print("SDM3: "+str(self.SDM3))
        print("SDM4: "+str(self.SDM4))
        print("SDM5: "+str(self.SDM5))
        print("SDM6: "+str(self.SDM6))
        print("SDM7: "+str(self.SDM7))
        print("SDM8: "+str(self.SDM8))
        print("SDM9: "+str(self.SDM9))


def MT44_SD_dec(binary_data):
    extracted_values = SD()
    extracted_values.SDMT = bool(int(binary_data[0]))
    extracted_values.SDM1 = bool(int(binary_data[1]))
    extracted_values.SDM2 = bool(int(binary_data[2]))
    extracted_values.SDM3 = bool(int(binary_data[3]))
    extracted_values.SDM4 = bool(int(binary_data[4]))
    extracted_values.SDM5 = bool(int(binary_data[5]))
    extracted_values.SDM6 = bool(int(binary_data[6]))
    extracted_values.SDM7 = bool(int(binary_data[7]))
    extracted_values.SDM8 = bool(int(binary_data[8]))
    extracted_values.SDM9 = bool(int(binary_data[9]))
    return extracted_values

def MT44_SD_msg_gen(SD):
    message = ''
    return message