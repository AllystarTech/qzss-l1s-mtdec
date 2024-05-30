# -*- coding: utf-8 -*-
"""
Extended Message Matching Tables 

@author: Allystar Technology Co. Limited
"""

class MatchTable_EX1:
    def __init__(self):
        self.match_table = {
            0b0: "",
            0b0000010001001100: "Hokkaido",
            0b0000010010110010: "Hokkaido",
            0b0000010010110011: "Hokkaido",
            #......
            0b1011100100010101: "Okinawa",
            0b1011100100010110: "Okinawa"
        }
    
    def get_EX1(self, data):
        EX1 = self.match_table.get(data, "INVALID")
        return EX1 
    
class MatchTable_EX2:
    def __init__(self):
        self.match_table = {
           0b0: "Leave the additional target area range.",
           0b1: "Head to the additional target area range."        
        }
        
    def get_EX2(self, data):
        EX2 = self.match_table.get(data, "INVALID")
        return EX2 
    
class MatchTable_EX3:
    def __init__(self):
        pass
        
    def get_EX3(self, data):
        EX3 = -90 + 180/(2**17-1)*data
        return EX3 
    
    
class MatchTable_EX4:
    def __init__(self):
        pass
        
    def get_EX4(self, data):
        EX4 = 45 + 180/(2**17 - 1)*data
        return EX4 
    
    
class MatchTable_EX5: #same as A14
    def __init__(self):
        self.match_table = {
            0b00000: 0.216,
            0b00001: 0.292,
            0b00010: 0.395,
            0b00011: 0.535,
            0b00100: 0.723,
            0b00101: 0.978,
            0b00110: 1.322,
            0b00111: 1.788,
            0b01000: 2.418,
            0b01001: 3.269,
            0b01010: 4.421,
            0b01011: 5.979,
            0b01100: 8.085,
            0b01101: 10.933,
            0b01110: 14.784,
            0b01111: 19.992,
            0b10000: 27.035,
            0b10001: 36.559,
            0b10010: 49.439,
            0b10011: 66.855,
            0b10100: 90.407,
            0b10101: 122.255,
            0b10110: 165.324,
            0b10111: 223.564,
            0b11000: 302.322,
            0b11001: 408.824,
            0b11010: 552.846,
            0b11011: 747.603,
            0b11100: 1010.970,
            0b11101: 1367.116,
            0b11110: 1848.727,
            0b11111: 2500.000
        }
        
    def get_EX5(self, data):
        EX5 = self.match_table.get(data, "INVALID")
        return EX5 
    
    
class MatchTable_EX6: #same as A15
    def __init__(self):
        self.match_table = {
            0b00000: 0.216,
            0b00001: 0.292,
            0b00010: 0.395,
            0b00011: 0.535,
            0b00100: 0.723,
            0b00101: 0.978,
            0b00110: 1.322,
            0b00111: 1.788,
            0b01000: 2.418,
            0b01001: 3.269,
            0b01010: 4.421,
            0b01011: 5.979,
            0b01100: 8.085,
            0b01101: 10.933,
            0b01110: 14.784,
            0b01111: 19.992,
            0b10000: 27.035,
            0b10001: 36.559,
            0b10010: 49.439,
            0b10011: 66.855,
            0b10100: 90.407,
            0b10101: 122.255,
            0b10110: 165.324,
            0b10111: 223.564,
            0b11000: 302.322,
            0b11001: 408.824,
            0b11010: 552.846,
            0b11011: 747.603,
            0b11100: 1010.970,
            0b11101: 1367.116,
            0b11110: 1848.727,
            0b11111: 2500.000
        
        }
        
    def get_EX6(self, data):
        EX6 = self.match_table.get(data, "INVALID")
        return EX6
    
    
class MatchTable_EX7:
    def __init__(self):
        pass
    
    def get_EX7(self, data):
        EX7 = -90 + 180/2**7*data
        return EX7
    
    
class MatchTable_EX8:
    def __init__(self):
        self.match_table = {
            0b0: "Prefecture code",
            0b1: "Municipality code"
        }
        
    def get_EX8(self, data):
        EX8 = self.match_table.get(data, "INVALID")
        return EX8
    
    
class MatchTable_EX9:
    def __init__(self):
        self.match_table_prefecture = {
            0b1: "Hokkaido",
            0b10: "Aomori",
            0b100: "Iwate",
            0b1000: "Miyagi",
            0b10000: "Akita",
            0b100000: "Yamagata",
            0b1000000: "Fukushima",
            0b10000000: "Ibaraki",
            0b100000000: "Tochigi",
            0b1000000000: "Gunma",
            0b10000000000: "Saitama",
            0b100000000000: "Chiba",
            0b1000000000000: "Tokyo",
            0b10000000000000: "Kanagawa",
            0b100000000000000: "Niigata",
            0b1000000000000000: "Toyama",
            0b10000000000000000: "Ishikawa",
            0b100000000000000000: "Fukui",
            0b1000000000000000000: "Yamanashi",
            0b10000000000000000000: "Nagano",
            0b100000000000000000000: "Gifu",
            0b1000000000000000000000: "Shizuoka",
            0b10000000000000000000000: "Aichi",
            0b100000000000000000000000: "Mie",
            0b1000000000000000000000000: "Shiga",
            0b10000000000000000000000000: "Kyoto",
            0b100000000000000000000000000: "Osaka",
            0b1000000000000000000000000000: "Hyogo",
            0b10000000000000000000000000000: "Nara",
            0b100000000000000000000000000000: "Wakayama",
            0b1000000000000000000000000000000: "Tottori",
            0b10000000000000000000000000000000: "Shimane",
            0b100000000000000000000000000000000: "Okayama",
            0b1000000000000000000000000000000000: "Hiroshima",
            0b10000000000000000000000000000000000: "Yamaguchi",
            0b100000000000000000000000000000000000: "Tokushima",
            0b1000000000000000000000000000000000000: "Kagawa",
            0b10000000000000000000000000000000000000: "Ehime",
            0b100000000000000000000000000000000000000: "Kochi",
            0b1000000000000000000000000000000000000000: "Fukuoka",
            0b10000000000000000000000000000000000000000: "Saga",
            0b100000000000000000000000000000000000000000: "Nagasaki",
            0b1000000000000000000000000000000000000000000: "Kumamoto",
            0b10000000000000000000000000000000000000000000: "Oita",
            0b100000000000000000000000000000000000000000000: "Miyazaki",
            0b1000000000000000000000000000000000000000000000: "Kagoshima",
            0b10000000000000000000000000000000000000000000000: "Okinawa"
        
        }
        self.match_table_municipality = {
            0b0: "",
            0b0000010001001100: "Sapporo",
            0b0000010010110010: "Hakodate",
            0b0000010010110011: "Otaru",
            #......
            0b1011100100010101: "Taketomi",
            0b1011100100010110: "Yonaguni" 
        }
        
    def get_EX9(self, EX9data, EX8data):
        EX9 = []
        if EX8data == 0:    
            #correct: this is OR
            EX9value = int(format(EX9data,"064b")[0:47],2)
            start = 0
            for parameter, country in self.match_table_prefecture.items():
                end = start + 1
                if (EX9value & parameter) >0:
                    EX9.append(country)
                start = end
        elif EX8data == 1:
            EX9_1 = self.match_table_municipality.get(int(format(EX9data,"064b")[0:16],2),"")
            EX9_2 = self.match_table_municipality.get(int(format(EX9data,"064b")[16:32],2),"")
            EX9_3 = self.match_table_municipality.get(int(format(EX9data,"064b")[32:48],2),"")
            EX9_4 = self.match_table_municipality.get(int(format(EX9data,"064b")[48:64],2),"")
            EX9 = [EX9_1, EX9_2, EX9_3, EX9_4]
        return EX9 
    
    
class MatchTable_EX11:
    def __init__(self):
        self.match_table = {
        
        }
        
    def get_EX11(self, data):
        EX11 = self.match_table.get(data, "INVAID")
        return EX11 
    
    
    
    
matchtable_EX1 = MatchTable_EX1()
matchtable_EX2 = MatchTable_EX2()
matchtable_EX3 = MatchTable_EX3()
matchtable_EX4 = MatchTable_EX4()
matchtable_EX5 = MatchTable_EX5()
matchtable_EX6 = MatchTable_EX6()
matchtable_EX7 = MatchTable_EX7()
matchtable_EX8 = MatchTable_EX8()
matchtable_EX9 = MatchTable_EX9()
#matchtable_EX11 = MatchTable_EX11()






def MT44_ExtMsg_msg_gen_0(ExtMsg, DCX_type, A11):
    message =''
    EX1 = matchtable_EX1.get_EX1(ExtMsg.EX1)
    message += "EX1-Target Area Code : " + EX1 + "\n"
    if DCX_type == 0 or A11 != 0:
        message += "EX2 to EX7 : Not used\n"
        return message
    EX2 = matchtable_EX2.get_EX2(ExtMsg.EX2)
    EX3 = matchtable_EX3.get_EX3(ExtMsg.EX3)
    EX4 = matchtable_EX4.get_EX4(ExtMsg.EX4)
    EX5 = matchtable_EX5.get_EX5(ExtMsg.EX5)
    EX6 = matchtable_EX6.get_EX6(ExtMsg.EX6)
    EX7 = matchtable_EX7.get_EX7(ExtMsg.EX7)
    message += "EX2-Evacuate Direction Type : " + EX2 + "\n"
    message += "Additional target area : Area enclosed in the ellipse indicated by the following parameters\n"
    message += "\tEX3-Additional Ellipse Centre Latitude : " + str(format(EX3, ".3f")) + '\n'
    message += "\tEX4-Additional Ellipse Centre Longitude : " + str(format(EX4, ".3f")) + "\n"
    message += "\tEX5-Additional Ellipse Semi-Major Axis : " + str(format(EX5, ".3f")) + "(km)\n"
    message += "\tEX6-Additional Ellipse Semi-Minor Axis : " + str(format(EX6, ".3f")) + "(km)\n"
    message += "\tEX7-Additional Ellipse Azimuth : " + str(format(EX7, ".3f")) + " (degrees)\n"
    return message

def MT44_ExtMsg_msg_gen_1(ExtMsg):
    message =''
    EX8 = matchtable_EX8.get_EX8(ExtMsg.EX8)
    EX9_list = matchtable_EX9.get_EX9(ExtMsg.EX9, ExtMsg.EX8)
    message += "EX8-Target Area Code List Type : " + EX8 + "\n"
    EX9 = ''
    for msg in EX9_list:
        if not(msg == ""):
            if not(EX9 == ""):
                EX9 += ', '
            EX9 += msg
    message += "EX9-Target Area Code List : " + EX9 + "\n"
    return message
  
def MT44_ExtMsg_msg_gen_3(ExtMsg):
    message =''
    message = 'EX11-Organization Outside Japan-Specific Area : \n'
    #EX11 = matchtable_EX11.get_EX11(ExtMsg.EX11)
    return message

def MT44_ExtMsg_msg_gen(ExtMsg, A11):
    message = ''
    if ExtMsg.DCX_type == 0 or ExtMsg.DCX_type == 2:
        message += MT44_ExtMsg_msg_gen_0(ExtMsg, ExtMsg.DCX_type, A11)
    elif ExtMsg.DCX_type == 1:
        message += MT44_ExtMsg_msg_gen_1(ExtMsg)
    elif ExtMsg.DCX_type == 3:
        message += MT44_ExtMsg_msg_gen_3(ExtMsg)
    return message