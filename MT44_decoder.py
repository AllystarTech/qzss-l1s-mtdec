# -*- coding: utf-8 -*-
"""
This is the decoder for QZSS L1S MT44

@author: 2024 Allystar Technology Co. Limited
"""

from MT44_SD_decoder import SD, MT44_SD_dec, MT44_SD_msg_gen
from MT44_CAMF_decoder import CAMF, MT44_CAMF_dec
from MT44_CAMF_Match_Table import MT44_CAMF_msg_gen
from MT44_ExtendedMsg_decoder import MT44_ExtMsg_dec
from MT44_ExtMsg_Match_Table import MT44_ExtMsg_msg_gen
from MT44_CRC_decoder import MT44_CRC_dec

def is_MT44_null(binary_data):
    return int(binary_data,2) == 0xDE0000000000000000000000000000000000000000000000 #0b0000110111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def decoder_MT44(hex_data, binary_data):
    Message = ''
    if is_MT44_null(binary_data[10:206]):
        #print("MT44 Null Message")
        #print(hex_data)
        return ""
    #print(hex_data)
    #TODO: add the decoder for MT44
    SD_data = MT44_SD_dec(binary_data[0:10])
    #Message += MT44_SD_msg_gen(SD_data)
    CAMF_data = MT44_CAMF_dec(binary_data[10:132])
    tmp, DCX_Type = MT44_CAMF_msg_gen(CAMF_data)
    Message += tmp
    ExtendedMsg_data = MT44_ExtMsg_dec(binary_data[132:206], DCX_Type)
    Message += MT44_ExtMsg_msg_gen(ExtendedMsg_data, CAMF_data.A11)
    CRC = MT44_CRC_dec(binary_data[212:236])
    
    #SD_data.printing()
    #CAMF_data.printing()    

    
    return Message
