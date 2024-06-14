# -*- coding: utf-8 -*-
"""
This is the decoder for QZSS L1S MT43

@author: 2024 Allystar Technology Co. Limited
"""
from MT43_Match_Table import mt43_earthquakeearly_dec, mt43_hypocenter_dec, mt43_seismic_dec, \
    mt43_nankai_dec, mt43_tsunami_dec, mt43_nwptsunami_dec, mt43_volcano_dec, mt43_ashfall_dec, \
    mt43_weather_dec, mt43_flood_dec, mt43_typhoon_dec, mt43_marine_dec

def decoder_MT43(binary_data):
    Rc = int(binary_data[0:3], 2)
    Dc = int(binary_data[3:7], 2)
    #TODO: Add other Dc type
    if Dc == 1: #Earthquake Early Warning
        print_message = mt43_earthquakeearly_dec(binary_data[7:])
        return print_message
    elif Dc == 2: #Hypocenter
        print_message = mt43_hypocenter_dec(binary_data[7:])
        return print_message        
    elif Dc == 3: #Seismic Intensity
        print_message = mt43_seismic_dec(binary_data[7:])
        return print_message
    elif Dc == 4: #Nankai Trough Earthquake
        print_message = mt43_nankai_dec(binary_data[7:])
        return print_message
    elif Dc == 5: #Tsunami
        print_message = mt43_tsunami_dec(binary_data[7:])
        return print_message
    elif Dc == 6: #Northwest Pacific Tsunami
        print_message = mt43_nwptsunami_dec(binary_data[7:])
        return print_message
    elif Dc == 7: #Unused
        print_message = ''
        return print_message
    elif Dc == 8: #Volcano
        print_message = mt43_volcano_dec(binary_data[7:])
        return print_message
    elif Dc == 9: #Ash Fall
        print_message = mt43_ashfall_dec(binary_data[7:])
        return print_message
    elif Dc == 10: #Weather
        print_message = mt43_weather_dec(binary_data[7:])
        return print_message
    elif Dc == 11: #Flood
        print_message = mt43_flood_dec(binary_data[7:])
        return print_message
    elif Dc == 12: #Typhoon
        print_message = mt43_typhoon_dec(binary_data[7:])
        return print_message
    elif Dc == 13: #Unused
        print_message = mt43_marine_dec(binary_data[7:])
        return print_message
    elif Dc == 14: #Marine
        print_message = mt43_marine_dec(binary_data[7:])
        return print_message
    else:
        return "MT43: invalid type"
