# -*- coding: utf-8 -*-

#  File Name: MT44_CAMF_Match_Table.py
# -----------------------------------------------------------------------------
#  CAMF Matching Tables 
#
#  Copyright (c) 2024 Allystar Technology Co. Limited
#
#  SPDX-License-Identifier: MIT
# -----------------------------------------------------------------------------

DCX_Type_table = {
    0:"DCX message (L-Alert)",
    1:"DCX message (J-Alert)",
    2:"DCX message (municipality-transmitted information [tentative name])",
    3:"DCX message (information from organizations outside Japan)"
}    

def get_DCX_type_name(num):
    return DCX_Type_table.get(num, "INVALID")
    
def get_DCX_type(a2, a3):
    if a2 == 0x6f: #0b001101111
        if a3 == 0x1: #0b00001
            return 0
        elif a3 == 0x2 or a3 == 0x3: #0b00010 or 0b00011
            return 1
        elif a3 == 0x4: #0b00100
             return 2
        else:
             return 999
    else:
        return 3
        
def is_DCX_valid(type):
    if type in {0, 1, 2, 3}:
        return True
    return False
    
def is_DCX_JAlert(type):
    if type == 1:
        return True
    return False

MatchTable_A1 = {
    0b00: "Test",
    0b01: "Alert",
    0b10: "Update",
    0b11: "All Clear"
}

def get_A1(value):
    return MatchTable_A1.get(value, "Unknown")

MatchTable_A2 = {
    0x0: "Afghanistan",                                  # 0b000000000
    0x1: "Albania",                                      # 0b000000001
    0x2: "Antarctica",                                   # 0b000000010
    0x3: "Algeria",                                      # 0b000000011
    0x4: "American Samoa",                               # 0b000000100
    0x5: "Andorra",                                      # 0b000000101
    0x6: "Angola",                                       # 0b000000110
    0x7: "Antigua and Barbuda",                          # 0b000000111
    0x8: "Azerbaijan",                                   # 0b000001000
    0x9: "Argentina",                                    # 0b000001001
    0xA: "Australia",                                    # 0b000001010
    0xB: "Austria",                                      # 0b000001011
    0xC: "Bahamas (the)",                                # 0b000001100
    0xD: "Bahrain",                                      # 0b000001101
    0xE: "Bangladesh",                                   # 0b000001110
    0xF: "Armenia",                                      # 0b000001111
    0x10: "Barbados",                                    # 0b000010000
    0x11: "Belgium",                                     # 0b000010001
    0x12: "Bermuda",                                     # 0b000010010
    0x13: "Bhutan",                                      # 0b000010011
    0x14: "Bolivia (Plurinational State of)",            # 0b000010100
    0x15: "Bosnia and Herzegovina",                      # 0b000010101
    0x16: "Botswana",                                    # 0b000010110
    0x17: "Bouvet Island",                               # 0b000010111
    0x18: "Brazil",                                      # 0b000011000
    0x19: "Belize",                                      # 0b000011001
    0x1A: "British Indian Ocean Territory (the)",           # 0b000011010
    0x1B: "Solomon Islands",                                # 0b000011011
    0x1C: "Virgin Islands (British)",                       # 0b000011100
    0x1D: "Brunei Darussalam",                              # 0b000011101
    0x1E: "Bulgaria",                                       # 0b000011110
    0x1F: "Myanmar",                                        # 0b000011111
    0x20: "Burundi",                                       # 0b000100000
    0x21: "Belarus",                                       # 0b000100001
    0x22: "Cambodia",                                      # 0b000100010
    0x23: "Cameroon",                                      # 0b000100011
    0x24: "Canada",                                        # 0b000100100
    0x25: "Cabo Verde",                                    # 0b000100101
    0x26: "Cayman Islands (the)",                          # 0b000100110
    0x27: "Central African Republic (the)",                # 0b000100111
    0x28: "Sri Lanka",                                     # 0b000101000
    0x29: "Chad",                                          # 0b000101001
    0x2A: "Chile",                                         # 0b000101010
    0x2B: "China",                                         # 0b000101011
    0x2C: "Taiwan (Province of China)",                    # 0b000101100
    0x2D: "Christmas Island",                              # 0b000101101
    0x2E: "Cocos (Keeling) Islands (the)",                 # 0b000101110
    0x2F: "Colombia",                                      # 0b000101111
    0x30: "Comoros (the)",                                 # 0b000110000
    0x31: "Mayotte",                                       # 0b000110001
    0x32: "Congo (the)",                                   # 0b000110010
    0x33: "Congo (the Democratic Republic of the)",        # 0b000110011
    0x34: "Cook Islands (the)",                            # 0b000110100
    0x35: "Costa Rica",                                    # 0b000110101
    0x36: "Croatia",                                       # 0b000110110
    0x37: "Cuba",                                          # 0b000110111
    0x38: "Cyprus",                                        # 0b000111000
    0x39: "Czechia",                                       # 0b000111001
    0x3A: "Benin",                                         # 0b000111010
    0x3B: "Denmark",                                       # 0b000111011
    0x3C: "Dominica",                                      # 0b000111100
    0x3D: "Dominican Republic (the)",                      # 0b000111101
    0x3E: "Ecuador",                                       # 0b000111110
    0x3F: "El Salvador",                                   # 0b000111111
    0x40: "Equatorial Guinea",                             # 0b001000000
    0x41: "Ethiopia",                                      # 0b001000001
    0x42: "Eritrea",                                       # 0b001000010
    0x43: "Estonia",                                       # 0b001000011
    0x44: "Faroe Islands (the)",                           # 0b001000100
    0x45: "Falkland Islands (the) [Malvinas]",             # 0b001000101
    0x46: "South Georgia and the South Sandwich Islands",  # 0b001000110
    0x47: "Fiji",                                          # 0b001000111
    0x48: "Finland",                                      # 0b001001000
    0x49: "Åland Islands",                                # 0b001001001
    0x50: "France",                                       # 0b001001010
    0x51: "French Guiana",                                # 0b001001011
    0x52: "French Polynesia",                             # 0b001001100
    0x53: "French Southern Territories (the)",            # 0b001001101
    0x54: "Djibouti",                                     # 0b001001110
    0x55: "Gabon",                                        # 0b001001111
    0x56: "Georgia",                                      # 0b001010000
    0x57: "Gambia (the)",                                 # 0b001010001
    0x58: "Palestine, State of",                          # 0b001010010
    0x59: "Germany",                                      # 0b001010011
    0x5A: "Ghana",                                        # 0b001010100
    0x5B: "Gibraltar",                                    # 0b001010101
    0x5C: "Kiribati",                                     # 0b001010110
    0x5D: "Greece",                                       # 0b001010111
    0x5E: "Greenland",                                    # 0b001011000
    0x5F: "Grenada",                                      # 0b001011001
    0x60: "Guadeloupe",                                   # 0b001011010
    0x61: "Guam",                                         # 0b001011011
    0x62: "Guatemala",                                    # 0b001011100
    0x63: "Guinea",                                       # 0b001011101
    0x64: "Guyana",                                       # 0b001011110
    0x65: "Haiti",                                        # 0b001011111
    0x66: "Heard Island and McDonald Islands",            # 0b001100000
    0x67: "Holy See (the)",                               # 0b001100001
    0x68: "Honduras",                                     # 0b001100010
    0x69: "Hong Kong",                                    # 0b001100011
    0x6A: "Hungary",                                      # 0b001100100
    0x6B: "Iceland",                                      # 0b001100101
    0x6C: "India",                                        # 0b001100110
    0x6D: "Indonesia",                                    # 0b001100111
    0x6E: "Iran (Islamic Republic of)",                   # 0b001101000
    0x6F: "Iraq",                                         # 0b001101001
    0x70: "Ireland",                                      # 0b001101010
    0x71: "Israel",                                       # 0b001101011
    0x72: "Italy",                                        # 0b001101100
    0x73: "Côte d'Ivoire",                                # 0b001101101
    0x74: "Jamaica",                                      # 0b001101110
    0x75: "Japan",                                        # 0b001101111
    0x76: "Kazakhstan",                                   # 0b001110000
    0x77: "Jordan",                                       # 0b001110001
    0x78: "Kenya",                                        # 0b001110010
    0x79: "Korea (the Democratic People's Republic of)",  # 0b001110011
    0x7A: "Korea (the Republic of)",                      # 0b001110100
    0x7B: "Kuwait",                                       # 0b001110101
    0x7C: "Kyrgyzstan",                                   # 0b001110110
    0x7D: "Lao People's Democratic Republic (the)",       # 0b001110111
    0x7E: "Lebanon",                                      # 0b001111000
    0x7F: "Lesotho",                                      # 0b001111001
    0x80: "Latvia",                                       # 0b001111010
    0x81: "Liberia",                                      # 0b001111011
    0x82: "Liechtenstein",                                # 0b001111101
    0x83: "Lithuania",                                    # 0b001111110
    0x84: "Luxembourg",                                   # 0b001111111
    0x85: "Macao",                                        # 0b010000000
    0x86: "Madagascar",                                   # 0b010000001
    0x87: "Malawi",                                       # 0b010000010
    0x88: "Malaysia",                                     # 0b010000011
    0x89: "Maldives",                                     # 0b010000100
    0x8A: "Mali",                                         # 0b010000101
    0x8B: "Malta",                                        # 0b010000110
    0x8C: "Martinique",                                   # 0b010000111
    0x8D: "Mauritania",                                   # 0b010001000
    0x8E: "Mauritius",                                    # 0b010001001
    0x8F: "Mexico",                                       # 0b010001010
    0x90: "Monaco",                                       # 0b010001011
    0x91: "Mongolia",                                     # 0b010001100
    0x92: "Moldova (the Republic of)",                    # 0b010001101
    0x93: "Montenegro",                                   # 0b010001110
    0x94: "Montserrat",                                   # 0b010001111
    0x95: "Morocco",                                      # 0b010010000
    0x96: "Mozambique",                                   # 0b010010001
    0x97: "Oman",                                         # 0b010010010
    0x98: "Namibia",                                      # 0b010010011
    0x99: "Nauru",                                         # 0b010010100
    0x9A: "Nepal",                                         # 0b010010101
    0x9B: "Netherlands (the)",                             # 0b010010110
    0x9C: "Curaçao",                                       # 0b010010111
    0x9D: "Aruba",                                         # 0b010011000
    0x9E: "Sint Maarten (Dutch part)",                     # 0b010011001
    0x9F: "Bonaire, Sint Eustatius and Saba",               # 0b010011010
    0xA0: "New Caledonia",                                 # 0b010011011
    0xA1: "Vanuatu",                                       # 0b010011100
    0xA2: "New Zealand",                                   # 0b010011101
    0xA3: "Nicaragua",                                     # 0b010011110
    0xA4: "Niger (the)",                                   # 0b010011111
    0xA5: "Nigeria",                                       # 0b010100000
    0xA6: "Niue",                                          # 0b010100001
    0xA7: "Norfolk Island",                                # 0b010100010
    0xA8: "Norway",                                        # 0b010100011
    0xA9: "Northern Mariana Islands (the)",                # 0b010100100
    0xAA: "United States Minor Outlying Islands (the)",    # 0b010100101
    0xAB: "Micronesia (Federated States of)",              # 0b010100110
    0xAC: "Marshall Islands (the)",                        # 0b010100111
    0xAD: "Palau",                                         # 0b010101000
    0xAE: "Pakistan",                                      # 0b010101001
    0xAF: "Panama",                                        # 0b010101010
    0xB0: "Papua New Guinea",                              # 0b010101011
    0xB1: "Paraguay",                                      # 0b010101100
    0xB2: "Peru",                                          # 0b010101101
    0xB3: "Philippines (the)",                             # 0b010101110
    0xB4: "Pitcairn",                                      # 0b010101111
    0xB5: "Poland",                                        # 0b010110000
    0xB6: "Portugal",                                      # 0b010110001
    0xB7: "Guinea-Bissau",                                 # 0b010110010
    0xB8: "Timor-Leste",                                   # 0b010110011
    0xB9: "Puerto Rico",                                   # 0b010110100
    0xBA: "Qatar",                                         # 0b010110101
    0xBB: "Réunion",                                       # 0b010110110
    0xBC: "Romania",                                       # 0b010110111
    0xBD: "Russian Federation (the)",                      # 0b010111000
    0xBE: "Rwanda",                                        # 0b010111001
    0xBF: "Saint Barthélemy",                              # 0b010111010
    0xC0: "Saint Helena, Ascension and Tristan da Cunha",  # 0b010111011
    0xC1: "Saint Kitts and Nevis",                         # 0b010111100
    0xC2: "Anguilla",                                      # 0b010111101
    0xC3: "Saint Lucia",                                   # 0b010111110
    0xC4: "Saint Martin (French part)",                    # 0b010111111
    0xC5: "Saint Pierre and Miquelon",                     # 0b011000000
    0xC6: "Saint Vincent and the Grenadines",              # 0b011000001
    0xC7: "San Marino",                                    # 0b011000010
    0xC8: "Sao Tome and Principe",                         # 0b011000011
    0xC9: "Saudi Arabia",                                  # 0b011000100
    0xCA: "Senegal",                                       # 0b011000101
    0xCB: "Serbia",                                        # 0b011000110
    0xCC: "Seychelles",                                    # 0b011000111
    0xCD: "Sierra Leone",                                  # 0b011001000
    0xCE: "Singapore",                                     # 0b011001001
    0xCF: "Slovakia",                                      # 0b011001010
    0xD0: "Viet Nam",                                      # 0b011001011
    0xD1: "Slovenia",                                      # 0b011001100
    0xD2: "Somalia",                                       # 0b011001101
    0xD3: "South Africa",                                  # 0b011001110
    0xD4: "Zimbabwe",                                      # 0b011001111
    0xD5: "Spain",                                         # 0b011010000
    0xD6: "South Sudan",                                   # 0b011010001
    0xD7: "Sudan (the)",                                  # 0b011010010
    0xD8: "Western Sahara*",                              # 0b011010011
    0xD9: "Suriname",                                     # 0b011010100
    0xDA: "Svalbard and Jan Mayen",                       # 0b011010101
    0xDB: "Eswatini",                                     # 0b011010110
    0xDC: "Sweden",                                       # 0b011010111
    0xDD: "Switzerland",                                  # 0b011011000
    0xDE: "Syrian Arab Republic (the)",                   # 0b011011001
    0xDF: "Tajikistan",                                   # 0b011011010
    0xE0: "Thailand",                                     # 0b011011011
    0xE1: "Togo",                                         # 0b011011100
    0xE2: "Tokelau",                                      # 0b011011101
    0xE3: "Tonga",                                        # 0b011011110
    0xE4: "Trinidad and Tobago",                          # 0b011011111
    0xE5: "United Arab Emirates (the)",                   # 0b011100000
    0xE6: "Tunisia",                                      # 0b011100001
    0xE7: "Turkey",                                       # 0b011100010
    0xE8: "Turkmenistan",                                 # 0b011100011
    0xE9: "Turks and Caicos Islands (the)",               # 0b011100100
    0xEA: "Tuvalu",                                       # 0b011100101
    0xEB: "Uganda",                                       # 0b011100110
    0xEC: "Ukraine",                                      # 0b011100111
    0xED: "North Macedonia",                              # 0b011101000
    0xEE: "Egypt",                                        # 0b011101001
    0xEF: "United Kingdom of Great Britain and Northern Ireland (the)",  # 0b011101010
    0xF0: "Guernsey",                                     # 0b011101011
    0xF1: "Jersey",                                     # 0b011101100
    0xF2: "Isle of Man",                                # 0b011101101
    0xF3: "Tanzania, the United Republic of",            # 0b011101110
    0xF4: "United States of America (the)",              # 0b011101111
    0xF5: "Virgin Islands (U.S.)",                      # 0b011110000
    0xF6: "Burkina Faso",                               # 0b011110001
    0xF7: "Uruguay",                                    # 0b011110010
    0xF8: "Uzbekistan",                                 # 0b011110011
    0xF9: "Venezuela (Bolivarian Republic of)",         # 0b011110100
    0xFA: "Wallis and Futuna",                          # 0b011110101
    0xFB: "Samoa",                                      # 0b011110110
    0xFC: "Yemen",                                      # 0b011110111
    0xFD: "Zambia"                                      # 0b011111000
}
    
def _is_A2_reserved(a2):
    return (a2 in range(0b011111001, 0b111111111+1))
    
def get_A2(value):
    if _is_A2_reserved(value):
        return "Reserved"
    return MatchTable_A2.get(value, "Unknown")


MatchTable_A3 = {
    0x0: {
        0x6F: "Not Used",                        # 0b001101111
        0x0A: "Not Used",                        # 0b000001010
        0x47: "Not Used",                        # 0b001000111
        0xDB: "Not Used"                         # 0b011011011
    },
    0x1: {
        0x6F: "FMMC",                            # 0b001101111
        0x0A: "National Emergency Management Agency (NEMA)",       # 0b000001010
        0x47: "National Disaster Management Office (NDMO)",         # 0b001000111
        0xDB: "Department of Disaster Prevention and Mitigation (DDPM)"   # 0b011011011
    },
    0x2: {
        0x6F: "FDMA",                            # 0b001101111
        0x0A: "Bureau of Meteorology (BOM)",      # 0b000001010
        0x47: "Fiji Meteorological Service (FMS)", # 0b001000111
        0xDB: "Thai Meteorological Department (TMD)"   # 0b011011011
    },
    0x3: {
        0x6F: "Related Ministries",               # 0b001101111
        0x0A: "Australian Climate Service (ACS)", # 0b000001010
        0x47: "Hydrology Section, Fiji Water Authority (FWA)",      # 0b001000111
        0xDB: "National Disaster Warning Center (NDWC)"   # 0b011011011
    },
    0x4: {
        0x6F: "Municipality",                                      # 0b001101111
        0x0A: "Geoscience Australia (GA)",                          # 0b000001010
        0x47: "Mineral Resources Department (MRD)",                 # 0b001000111
        0xDB: "Department of Mineral Resources (DMR)"               # 0b011011011
    },
    0x5: {
        0x6F: "Reserved",                                          # 0b001101111
        0x0A: "Commonwealth Scientific and Industrial Research Organisation (CSIRO)",   # 0b000001010
        0x47: "Fiji Broadcasting Corporation (FBC)",                # 0b001000111
        0xDB: "Navy Hydrographic Department, Royal Thai Navy (RTN)" # 0b011011011
    },
    0x6: {
        0x6F: "Reserved",                                          # 0b001101111
        0x0A: "Australian Bureau of Statistics (ABS)",              # 0b000001010
        0x47: "Reserved",                                          # 0b001000111
        0xDB: "Department of Water Resources (DWR)"                 # 0b011011011
    },
    0x7: {
        0x6F: "Reserved",                                          # 0b001101111
        0x0A: "Resilience New South Wales (Resilience NSW)",        # 0b000001010
        0x47: "Reserved",                                          # 0b001000111
        0xDB: "Royal Irrigation Department (RID)"                   # 0b011011011
    },
    0x8: {
        0x6F: "Reserved",                                          # 0b001101111
        0x0A: "State Emergency Service New South Wales (SES)",      # 0b000001010
        0x47: "Reserved",                                          # 0b001000111
        0xDB: "Department of Pollution Control (DPC)"               # 0b011011011
    },
    0x9: {
        0x6F: "New South Wales Rural Fire Service (NSW RFS)",       # 0b001101111
        0x0A: "Reserved",                                          # 0b000001010
        0x47: "Geo-Informatics and Space Technology Development Agency (GISTDA)",          # 0b001000111
        0xDB: "Reserved"                                           # 0b011011011
    },
    0xA: {
        0x6F: "Reserved",                                                     # 0b001101111
        0x0A: "Joint Australian Tsunami Warning Centre (JATWC)",               # 0b000001010
        0x47: "Reserved",                                                     # 0b001000111
        0xDB: "Electricity Generating Authority of Thailand (EGAT)"            # 0b011011011
    },
    0xB: {
        0x6F: "Reserved",                                                     # 0b001101111
        0x0A: "Flood Knowledge Centre (FKC)",                                  # 0b000001010
        0x47: "Reserved",                                                     # 0b001000111
        0xDB: "Royal Forest Department (RFD)"                                  # 0b011011011
    },
    0xC: {
        0x6F: "Reserved",                                                     # 0b001101111
        0x0A: "Australian Broadcasting Corporation (ABC)",                     # 0b000001010
        0x47: "Reserved",                                                     # 0b001000111
        0xDB: "Department of Parks, Wildlife and Plant Conservation (DPWPC)"   # 0b011011011
    },
    0xD: {
        0x6F: "Reserved",                                                     # 0b001101111
        0x0A: "Reserved",                                                      # 0b000001010
        0x47: "Reserved",                                                      # 0b001000111
        0xDB: "Water Crisis Prevention Center (WCPC)"                          # 0b011011011
    },
    0xE: {
        0x6F: "Reserved",                                                     # 0b001101111
        0x0A: "Reserved",                                                      # 0b000001010
        0x47: "Reserved",                                                      # 0b001000111
        0xDB: "Reserved"                                                       # 0b011011011
    }
}

def _is_A3_reserved(a3, provider_id):
    return (a3 in {0b001101111, 0b000001010, 0b001000111, 0b011011011}) and (provider_id in range(0b01110 + 1, 0b100000))
    
def get_A3(a3, provider_id):
    if provider_id in MatchTable_A3 and a3 in MatchTable_A3.get(provider_id, {}):
        return MatchTable_A3.get(a3).get(provider_id)
    if _is_A3_reserved(a3, provider_id):
        return "Reserved"
    else:
        return "Unknown Provider"

MatchTable_A4 = {
    0x0: "not used",                                                   # 0b0000000
    0x1: "Air strike",                                                  # 0b0000001
    0x2: "Attack on IT systems",                                        # 0b0000010
    0x3: "Attack with nuclear weapons",                                 # 0b0000011
    0x4: "Biological hazard",                                           # 0b0000100
    0x5: "Chemical hazard",                                             # 0b0000101
    0x6: "Explosive hazard",                                            # 0b0000110
    0x7: "Meteorite impact",                                            # 0b0000111
    0x8: "Missile attack",                                              # 0b0001000
    0x9: "Nuclear hazard",                                              # 0b0001001
    0xA: "Nuclear power station accident",                              # 0b0001010
    0xB: "Radiological hazard",                                         # 0b0001011
    0xC: "Satellite/space re-entry debris",                             # 0b0001100
    0xD: "Siren test",                                                  # 0b0001101
    0xE: "Acid rain",                                                   # 0b0001110
    0xF: "Air pollution",                                               # 0b0001111
    0x10: "Contaminated drinking water",                                # 0b0010000
    0x11: "Gas leak",                                                    # 0b0010001
    0x12: "Marine pollution",                                           # 0b0010010
    0x13: "Noise pollution",                                            # 0b0010011
    0x14: "Plague of insects",                                          # 0b0010100
    0x15: "River pollution",                                            # 0b0010101
    0x16: "Suspended dust",                                             # 0b0010110
    0x17: "UV radiation",                                               # 0b0010111
    0x18: "Conflagration",                                              # 0b0011000
    0x19: "Fire brigade deployment",                                    # 0b0011001
    0x1A: "Fire gases",                                                 # 0b0011010
    0x1B: "Forest fire",                                                # 0b0011011
    0x1C: "Fumes",                                                      # 0b0011100
    0x1D: "Odour nuisance",                                             # 0b0011101
    0x1E: "Risk of fire",                                               # 0b0011110
    0x1F: "Structure fire / Industrial fire",                           # 0b0011111
    0x20: "Ash fall",                                                   # 0b0100000
    0x21: "Avalanche risk",                                             # 0b0100001
    0x22: "Crack in the ground/sinkhole",                               # 0b0100010
    0x23: "Debris flow",                                                # 0b0100011
    0x24: "Earthquake",                                                 # 0b0100100
    0x25: "Geomagnetic or solar storm",                                 # 0b0100101
    0x26: "Glacial ice avalanche",                                      # 0b0100110
    0x27: "Landslide",                                                  # 0b0100111
    0x28: "Lava flow",                                                  # 0b0101000
    0x29: "Pyroclastic flow",                                           # 0b0101001
    0x2A: "Snowdrifts",                                                  # 0b0101010
    0x2B: "Tidal wave",                                                 # 0b0101011
    0x2C: "Tsunami",                                                    # 0b0101100
    0x2D: "Volcanic mud flow",                                          # 0b0101101
    0x2E: "Volcano eruption",                                           # 0b0101110
    0x2F: "Wind/wave/storm surge",                                      # 0b0101111
    0x30: "Epizootic",                                                  # 0b0110000
    0x31: "Food safety alert",                                          # 0b0110001
    0x32: "Health hazard",                                              # 0b0110010
    0x33: "Pandemic",                                                   # 0b0110011
    0x34: "Pest infestation",                                           # 0b0110100
    0x35: "Risk of infection",                                          # 0b0110101
    0x36: "Building collapse",                                          # 0b0110110
    0x37: "Emergency number outage",                                    # 0b0110111
    0x38: "Gas supply outage",                                          # 0b0111000
    0x39: "Outage of IT systems",                                       # 0b0111001
    0x3A: "Power outage",                                               # 0b0111010
    0x3B: "Raw sewage",                                                 # 0b0111011
    0x3C: "Telephone line outage",                                      # 0b0111100
    0x3D: "Black Ice",                                                  # 0b0111101
    0x3E: "Coastal flooding",                                           # 0b0111110
    0x3F: "Cold wave",                                                  # 0b0111111
    0x40: "Derecho",                                                    # 0b1000000
    0x41: "Drought",                                                    # 0b1000001
    0x42: "Dust storm",                                                 # 0b1000010
    0x43: "Floating ice / icebergs",                                    # 0b1000011
    0x44: "Flood",                                                      # 0b1000100
    0x45: "Fog",                                                        # 0b1000101
    0x46: "Hail",                                                        # 0b1000110
    0x47: "Heat wave",                                                  # 0b1000111
    0x48: "Lightning",                                                  # 0b1001000
    0x49: "Pollens",                                                    # 0b1001001
    0x4A: "Rainfall",                                                   # 0b1001010
    0x4B: "Snow storm / blizzard",                                      # 0b1001011
    0x4C: "Snowfall",                                                   # 0b1001100
    0x4D: "Storm or thunderstorm",                                      # 0b1001101
    0x4E: "Thawing",                                                    # 0b1001110
    0x4F: "Tornado",                                                    # 0b1001111
    0x50: "Tropical cyclone (hurricane)",                               # 0b1010000
    0x51: "Wind chill/frost",                                           # 0b1010001
    0x52: "Tropical cyclone (typhoon)",                                 # 0b1010010
    0x53: "Dam failure or bursting of a dam",                           # 0b1010011
    0x54: "Dike failure or bursting of a dike",                         # 0b1010100
    0x55: "Explosive ordnance disposal",                                # 0b1010101
    0x56: "Factory accident",                                           # 0b1010110
    0x57: "Mine hazard",                                                # 0b1010111
    0x58: "SAFETY - Bomb/ammunition discovery",                         # 0b1011000
    0x59: "Demonstration",                                              # 0b1011001
    0x5A: "Hazardous material accident",                                # 0b1011010
    0x5B: "Life Threatening situation",                                  # 0b1011011
    0x5C: "Major event",                                                # 0b1011100
    0x5D: "Missing person/abduction",                                   # 0b1011101
    0x5E: "Risk of explosion",                                           # 0b1011110
    0x5F: "Safety warning",                                              # 0b1011111
    0x60: "Undefined flying object",                                    # 0b1100000
    0x61: "Unidentified animal",                                        # 0b1100001
    0x62: "Chemical attack",                                            # 0b1100010
    0x63: "Guerrilla attack",                                           # 0b1100011
    0x64: "Hijack",                                                     # 0b1100100
    0x65: "Shooting or danger due to weapons",                          # 0b1100101
    0x66: "Special forces attack",                                      # 0b1100110
    0x67: "Terrorism",                                                  # 0b1100111
    0x68: "Aircraft crash",                                             # 0b1101000
    0x69: "Bridge collapse",                                            # 0b1101001
    0x6A: "Dangerous goods accident",                                   # 0b1101010
    0x6B: "Inland waterway transport accident",                         # 0b1101011
    0x6C: "Nautical disaster/Maritime/Marine Security",                 # 0b1101100
    0x6D: "Oil spill",                                                  # 0b1101101
    0x6E: "Road traffic incident",                                      # 0b1101110
    0x6F: "Train/rail accident",                                        # 0b1101111
    0x70: "Tunnel accident",                                            # 0b1110000
    0x71: "Test alert"                                                  # 0b1110001
            '''
            0b0000000: "not used",
            0b0000001: "CBRNE - Air strike",
            0b0000010: "CBRNE - Attack on IT systems",
            0b0000011: "CBRNE - Attack with nuclear weapons",
            0b0000100: "CBRNE - Biological hazard",
            0b0000101: "CBRNE - Chemical hazard",
            0b0000110: "CBRNE - Explosive hazard",
            0b0000111: "CBRNE - Meteorite impact",
            0b0001000: "CBRNE – Missile attack",
            0b0001001: "CBRNE - Nuclear hazard",
            0b0001010: "CBRNE - Nuclear power station accident",
            0b0001011: "CBRNE - Radiological hazard",
            0b0001100: "CBRNE - Satellite/space re-entry debris",
            0b0001101: "CBRNE - Siren test",
            0b0001110: "ENVIRONMENT - Acid rain",
            0b0001111: "ENVIRONMENT - Air pollution",
            0b0010000: "ENVIRONMENT - Contaminated drinking water",
            0b0010001: "ENVIRONMENT - Gas leak",
            0b0010010: "ENVIRONMENT - Marine pollution",
            0b0010011: "ENVIRONMENT - Noise pollution",
            0b0010100: "ENVIRONMENT - Plague of insects",
            0b0010101: "ENVIRONMENT - River pollution",            
            0b0010110: "ENVIRONMENT – Suspended dust",
            0b0010111: "ENVIRONMENT – UV radiation",
            0b0011000: "FIRE – Conflagration",
            0b0011001: "FIRE - Fire brigade deployment",
            0b0011010: "FIRE - Fire gases",
            0b0011011: "FIRE - Forest fire",
            0b0011100: "FIRE - Fumes",
            0b0011101: "FIRE - Odour nuisance",
            0b0011110: "FIRE - Risk of fire",
            0b0011111: "FIRE - Structure fire / Industrial fire",
            0b0100000: "GEO - Ash fall",
            0b0100001: "GEO - Avalanche risk",
            0b0100010: "GEO - Crack in the ground/sinkhole",
            0b0100011: "GEO - Debris flow",
            0b0100100: "GEO - Earthquake",
            0b0100101: "GEO - Geomagnetic or solar storm",
            0b0100110: "GEO - Glacial ice avalanche",
            0b0100111: "GEO - Landslide",
            0b0101000: "GEO - Lava flow",
            0b0101001: "GEO - Pyroclastic flow",
            0b0101010: "GEO - Snowdrifts",
            0b0101011: "GEO - Tidal wave",
            0b0101100: "GEO - Tsunami",
            0b0101101: "GEO - Volcanic mud flow",
            0b0101110: "GEO - Volcano eruption",
            0b0101111: "GEO - Wind/wave/storm surge",
            0b0110000: "HEALTH - Epizootic",
            0b0110001: "HEALTH - Food safety alert",
            0b0110010: "HEALTH - Health hazard",
            0b0110011: "HEALTH - Pandemic",
            0b0110100: "HEALTH - Pest infestation",
            0b0110101: "HEALTH - Risk of infection",
            0b0110110: "INFRASTRUCTURE - Building collapse",
            0b0110111: "INFRASTRUCTURE - Emergency number outage",
            0b0111000: "INFRASTRUCTURE - Gas supply outage",
            0b0111001: "INFRASTRUCTURE - Outage of IT systems",
            0b0111010: "INFRASTRUCTURE - Power outage",
            0b0111011: "INFRASTRUCTURE - Raw sewage",
            0b0111100: "INFRASTRUCTURE - Telephone line outage",
            0b0111101: "MET - Black Ice",
            0b0111110: "MET - Coastal flooding",
            0b0111111: "MET - Cold wave",
            0b1000000: "MET - Derecho",
            0b1000001: "MET - Drought",
            0b1000010: "MET - Dust storm",
            0b1000011: "MET - Floating ice / icebergs",
            0b1000100: "MET - Flood",
            0b1000101: "MET - Fog",
            0b1000110: "MET - Hail",
            0b1000111: "MET - Heat wave",
            0b1001000: "MET - Lightning",
            0b1001001: "MET - Pollens",
            0b1001010: "MET - Rainfall",
            0b1001011: "MET - Snow storm / blizzard",
            0b1001100: "MET - Snowfall",
            0b1001101: "MET - Storm or thunderstorm",
            0b1001110: "MET - Thawing",
            0b1001111: "MET - Tornado",
            0b1010000: "MET - Tropical cyclone (hurricane)",
            0b1010001: "MET - Wind chill/frost",
            0b1010010: "MET - Tropical cyclone (typhoon)",
            0b1010011: "RESCUE - Dam failure or bursting of a dam",
            0b1010100: "RESCUE - Dike failure or bursting of a dike",
            0b1010101: "RESCUE - Explosive ordnance disposal",
            0b1010110: "RESCUE - Factory accident",
            0b1010111: "RESCUE - Mine hazard",
            0b1011000: "Bomb/ammunition discovery",
            0b1011001: "SAFETY - Demonstration",
            0b1011010: "SAFETY - Hazardous material accident",
            0b1011011: "SAFETY - Life Threatening situation",
            0b1011100: "SAFETY - Major event",
            0b1011101: "SAFETY - Missing person/abduction",
            0b1011110: "SAFETY - Risk of explosion",
            0b1011111: "SAFETY - Safety warning",
            0b1100000: "SAFETY - Undefined flying object",
            0b1100001: "SAFETY - Unidentified animal",
            0b1100010: "SECURITY - Chemical attack",
            0b1100011: "SECURITY - Guerrilla attack",
            0b1100100: "SECURITY - Hijack",
            0b1100101: "SECURITY - Shooting or danger due to weapons",
            0b1100110: "SECURITY - Special forces attack",
            0b1100111: "SECURITY - Terrorism",
            0b1101000: "TRANSPORT - Aircraft crash",
            0b1101001: "TRANSPORT - Bridge collapse",
            0b1101010: "TRANSPORT - Dangerous goods accident",
            0b1101011: "TRANSPORT - Inland waterway transport accident",
            0b1101100: "TRANSPORT - Nautical disaster/Maritime/Marine Security",
            0b1101101: "TRANSPORT - Oil spill",
            0b1101110: "TRANSPORT - Road traffic incident",
            0b1101111: "TRANSPORT - Train/rail accident",
            0b1110000: "TRANSPORT - Tunnel accident",
            0b1110001: "OTHER - Test alert"
            '''
}

def _is_A4_reserved(a4):
    return (a4 in range (0b1110010, 0b11111111+1))

def get_A4(a4):
    if _is_A4_reserved(a4):
        return "Reserved"
    elif a4 in MatchTable_A4:
        return MatchTable_A4.get(a4)
    else:
        return "Unknown Hazard Type"

MatchTable_A5 = {
    0x0: "Unknown",                                                     # 0b00
    0x1: "Moderate",                                                    # 0b01
    0x2: "Severe",                                                      # 0b10
    0x3: "Extreme"                                                      # 0b11
}

def get_A5(code):
    return MatchTable_A5.get(code, "Invalid code")

MatchTable_A6 = {
    0x0: "Current",                                                     # 0b0
    0x1: "Next"                                                         # 0b1
}

def get_A6(a6):
    return MatchTable_A6.get(a6, "Invalid code")    

def _is_A7_not_used(a7):
    return a7 in {0, range(0b10011101100001, 0b11111111111111+1)}
    
def _get_A7_week_day(a7):
    if a7 in range(0b00000000000001, 0b00000000000001+1440):
        return "MONDAY"
    elif a7 in range(0b00010110100001, 0b00010110100001+1440):
        return "TUESDAY"
    elif a7 in range(0b00101101000001, 0b00101101000001+1440):
        return "WEDNESDAY"
    elif a7 in range(0b01000011100001, 0b01000011100001+1440):
        return "THURSDAY"
    elif a7 in range(0b01011010000001, 0b01011010000001+1440):
        return "FRIDAY"
    elif a7 in range(0b01110000100001, 0b01110000100001+1440):
        return  "SATURDAY"
    elif a7 in range(0b10000111000001, 0b10000111000001+1440):
        return "SUNDAY"
    else:
        return "INVALID"
        
def _get_A7_hour(delta):
    hour = delta//60
    if hour == 12:
        return hour, "PM"
    elif hour > 12:
        return hour - 12, "PM"
    elif hour < 12:
        return hour, "AM"
    else:
        return 0, "NULL"
        
def _get_A7_minutes(delta):
    minutes = delta % 60
    return minutes
    
def get_A7(a7):
    if _is_A7_not_used(a7):
        return "not used"
    day = _get_A7_week_day(a7)
    delta = a7 % 1440 - 1
    hour, noon = _get_A7_hour(delta)
    minutes = _get_A7_minutes(delta)
    return day + " - " + str(hour) + ":" + str(minutes) + " " + noon

MatchTable_A8 = {
    0x0: "Unknown",                                                     # 0b00
    0x1: "Duration < 6H",                                                # 0b01
    0x2: "6H <= Duration < 12H",                                         # 0b10
    0x3: "12H <= Duration < 24H"                                         # 0b11
}

def get_A8(a8):
    return MatchTable_A6.get(a8, "Invalid code")        
    
MatchTable_A9 = {
    0x0: "International library",                                        # 0b0
    0x1: "Country/region guidance library"                               # 0b1
}

def get_A9(a9):
    return MatchTable_A9.get(a9, "Invalid code")
    
MatchTable_A10 = {
    0x0: "#1",                                                          # 0b000
    0x1: "#2",                                                          # 0b001
    0x2: "#3",                                                          # 0b010
    0x3: "#4",                                                          # 0b011
    0x4: "#5",                                                          # 0b100
    0x5: "#6",                                                          # 0b101
    0x6: "#7",                                                          # 0b110
    0x7: "#8"                                                           # 0b111
}

def get_A10(a10):
    return MatchTable_A10.get(a10, "Invalid code")    

MatchTable_A11_0_1 = {
    0x0: "",                                                            # 0b00
    0x1: "Stay",                                                        # 0b01
    0x2: "Move to/toward",                                               # 0b10
    0x3: "Keep away from"                                               # 0b11
}

MatchTable_A11_0_2 = {
    0x00: "",                                                           # 0b00000000
    0x01: "Under/inside a solid structure",                              # 0b00000001
    0x02: "3rd floor or higher",                                         # 0b00000010
    0x03: "Underground",                                                 # 0b00000011
    0x04: "Mountain",                                                    # 0b00000100
    0x05: "Water area",                                                  # 0b00000101
    0x06: "Building where chemicals are handled, such as a factory",     # 0b00000110
    0x07: "Cliffs and areas at risk of collapse",                        # 0b00000111
    0x7F: "Take the best immediate action to save your life.",            # 0b01111111
    0xFF: "Take the best immediate action to save your life."             # 0b11111111
}

MatchTable_A11_1_1 = {
    0x0: "IC-A-01 [empty]",                                              # 0b00000
    0x1: "IC-A-02 You are in the danger zone, leave the area immediately. Listen to radio or media for directions and information.",  # 0b00001
    0x2: "IC-A-03 You are in the danger zone, leave the area immediately and reach the evacuation point indicated by the area plotted in yellow. Listen to radio or media for directions and information.",  # 0b00010
    0x3: "IC-A-04 Seek shelter in a building immediately. Stay under cover and stay informed.",  # 0b00011
    # Missing middle instructions, cannot found
    0x1F: "IC-A-32 Conditions have improved and are no longer expected to meet alert criteria."  # 0b11111
}

MatchTable_A11_1_2 = {
    0x0: "IC-B-01 [empty]",                                              # 0b00000
    0x1: "IC-B-02 Check with the weather services and local authorities for additional information",  # 0b00001
    0x2: "IC-B-03 Find out the location of the information points set up by the authorities on official channels (radio, internet, TV, social networks...)",  # 0b00010
    0x3: "IC-B-04 Sensitive or vulnerable people should not go out unless they must.",  # 0b00011
    0x1F: "IC-B-32 This replaces the warning previously in effect for this area."  # 0b11111
}
    
def _get_table_A11_0_1(data):
        return MatchTable_A11_0_1.get(data, "")
    
def _get_table_A11_0_2(data):
    if data in range(0b00001000, 0b01111110):
        return "reserved"
    elif data in range(0b10000000, 0b11111110):
        return "Reserved for the evacuation action instruction text for J-Alert"
    else:
        return MatchTable_A11_0_2.get(data, "")
    
def _get_table_A11_1_1(data):
    return MatchTable_A11_1_1.get(data, "")
    
def _get_table_A11_1_2(data):
    return MatchTable_A11_1_2.get(data, "")

def _get_table_A11_0(A11):
    msg = ''
    A11_binary = format(A11, "010b")    
    msg += _get_table_A11_0_1(int(A11_binary[0:2], 2))
    if msg != '':
        msg += ' '
    msg += _get_table_A11_0_2(int(A11_binary[2:10], 2))
    return msg
        
        
def _get_table_A11_1(A11, A9_bit1):
    msg = ""
    if A9_bit1 == 0:    
        A11_binary = format(A11, "010b") 
        msg += _get_table_A11_1_1(int(A11_binary[0:5], 2))
        if msg != '':
            msg += ' '
        msg += _get_table_A11_1_2(int(A11_binary[5:10], 2))
    return msg
    
def get_A11(A11, DCX_type, A9_bit1 = 999):
    if A11 == 0 and DCX_type == 2:
        return "Not specified (Reference EX2 to EX7.)"
    if DCX_type in {0, 1, 2}:
        return "\"" + _get_table_A11_0(A11) + "\""
    elif DCX_type == 3:
        return "\"" + _get_table_A11_1(A11, A9_bit1) + "\""
    else:
        return ""

MatchTable_A14 = {
    0x0: 0.216,                                                         # 0b00000
    0x1: 0.292,                                                         # 0b00001
    0x2: 0.395,                                                         # 0b00010
    0x3: 0.535,                                                         # 0b00011
    0x4: 0.723,                                                         # 0b00100
    0x5: 0.978,                                                         # 0b00101
    0x6: 1.322,                                                         # 0b00110
    0x7: 1.788,                                                         # 0b00111
    0x8: 2.418,                                                         # 0b01000
    0x9: 3.269,                                                         # 0b01001
    0xA: 4.421,                                                         # 0b01010
    0xB: 5.979,                                                         # 0b01011
    0xC: 8.085,                                                         # 0b01100
    0xD: 10.933,                                                        # 0b01101
    0xE: 14.784,                                                        # 0b01110
    0xF: 19.992,                                                        # 0b01111
    0x10: 27.035,                                                       # 0b10000
    0x11: 36.559,                                                       # 0b10001
    0x12: 49.439,                                                       # 0b10010
    0x13: 66.855,                                                       # 0b10011
    0x14: 90.407,                                                       # 0b10100
    0x15: 122.255,                                                      # 0b10101
    0x16: 165.324,                                                      # 0b10110
    0x17: 223.564,                                                      # 0b10111
    0x18: 302.322,                                                      # 0b11000
    0x19: 408.824,                                                      # 0b11001
    0x1A: 552.846,                                                      # 0b11010
    0x1B: 747.603,                                                      # 0b11011
    0x1C: 1010.970,                                                     # 0b11100
    0x1D: 1367.116,                                                     # 0b11101
    0x1E: 1848.727,                                                     # 0b11110
    0x1F: 2500.000                                                      # 0b11111
}

def get_A14(a14):
    return MatchTable_A14.get(a14, "Invalid radius")

MatchTable_A15 = {
    0x0: 0.216,                                                         # 0b00000
    0x1: 0.292,                                                         # 0b00001
    0x2: 0.395,                                                         # 0b00010
    0x3: 0.535,                                                         # 0b00011
    0x4: 0.723,                                                         # 0b00100
    0x5: 0.978,                                                         # 0b00101
    0x6: 1.322,                                                         # 0b00110
    0x7: 1.788,                                                         # 0b00111
    0x8: 2.418,                                                         # 0b01000
    0x9: 3.269,                                                         # 0b01001
    0xA: 4.421,                                                         # 0b01010
    0xB: 5.979,                                                         # 0b01011
    0xC: 8.085,                                                         # 0b01100
    0xD: 10.933,                                                        # 0b01101
    0xE: 14.784,                                                        # 0b01110
    0xF: 19.992,                                                        # 0b01111
    0x10: 27.035,                                                       # 0b10000
    0x11: 36.559,                                                       # 0b10001
    0x12: 49.439,                                                       # 0b10010
    0x13: 66.855,                                                       # 0b10011
    0x14: 90.407,                                                       # 0b10100
    0x15: 122.255,                                                      # 0b10101
    0x16: 165.324,                                                      # 0b10110
    0x17: 223.564,                                                      # 0b10111
    0x18: 302.322,                                                      # 0b11000
    0x19: 408.824,                                                      # 0b11001
    0x1A: 552.846,                                                      # 0b11010
    0x1B: 747.603,                                                      # 0b11011
    0x1C: 1010.970,                                                     # 0b11100
    0x1D: 1367.116,                                                     # 0b11101
    0x1E: 1848.727,                                                     # 0b11110
    0x1F: 2500.000                                                      # 0b11111
}

def get_A15(a15):
    return MatchTable_A15.get(a15, "Invalid radius")

MatchTable_A17 = {
    0b00: "B1 - Improved Resolution of Main Ellipse",
    0b01: "B2 - Position of the Centre of the Hazard",
    0b10: "B3 - Secondary Ellipse Definition",
    0b11: "B4 - Quantitative and detailed information about the Hazard"
}

def get_A17(a17):
    return MatchTable_A17.get(a17, "Invalid code")

MatchTable_A18_C1 = {
    0x0: 0.000000,                                                     # 0b000
    0x1: 0.000343,                                                     # 0b001
    0x2: 0.000687,                                                     # 0b010
    0x3: 0.001030,                                                     # 0b011
    0x4: 0.001373,                                                     # 0b100
    0x5: 0.001717,                                                     # 0b101
    0x6: 0.002060,                                                     # 0b110
    0x7: 0.002403                                                      # 0b111
}

MatchTable_A18_C2 = {
    0x0: 0.000000000,                                                   # 0b000
    0x1: 0.000343325,                                                   # 0b001
    0x2: 0.000686651,                                                   # 0b010
    0x3: 0.001029976,                                                   # 0b011
    0x4: 0.001373301,                                                   # 0b100
    0x5: 0.001716627,                                                   # 0b101
    0x6: 0.002059952,                                                   # 0b110
    0x7: 0.002403278                                                    # 0b111
}

MatchTable_A18_C3 = {
    0x0: 0.000,                                                         # 0b000
    0x1: 0.125,                                                         # 0b001
    0x2: 0.250,                                                         # 0b010
    0x3: 0.375,                                                         # 0b011
    0x4: 0.500,                                                         # 0b100
    0x5: 0.625,                                                         # 0b101
    0x6: 0.750,                                                         # 0b110
    0x7: 0.875                                                          # 0b111
}

MatchTable_A18_C4 = {
    0x0: 0.0,                                                           # 0b000
    0x1: 0.125,                                                         # 0b001
    0x2: 0.250,                                                         # 0b010
    0x3: 0.375,                                                         # 0b011
    0x4: 0.500,                                                         # 0b100
    0x5: 0.625,                                                         # 0b101
    0x6: 0.750,                                                         # 0b110
    0x7: 0.875                                                          # 0b111
}
        
MatchTable_A18_C5 = {
    0x00: -10.000000000,                                                # 0b0000000
    0x01: -9.843750000,                                                 # 0b0000001
    0x02: -9.687500000,                                                 # 0b0000010
    0x03: -9.531250000,                                                 # 0b0000011
    0x04: -9.375000000,                                                 # 0b0000100
    0x05: -9.218750000,                                                 # 0b0000101
    0x06: -9.062500000,                                                 # 0b0000110
    0x07: -8.906250000,                                                 # 0b0000111
    0x08: -8.750000000,                                                 # 0b0001000
    0x09: -8.593750000,                                                 # 0b0001001
    0x0A: -8.437500000,                                                 # 0b0001010
    0x0B: -8.281250000,                                                 # 0b0001011
    0x0C: -8.125000000,                                                 # 0b0001100
    0x0D: -7.968750000,                                                 # 0b0001101
    0x0E: -7.812500000,                                                 # 0b0001110
    0x0F: -7.656250000,                                                 # 0b0001111
    0x10: -7.500000000,                                                 # 0b0010000
    0x11: -7.343750000,                                                 # 0b0010001
    0x12: -7.187500000,                                                 # 0b0010010
    0x13: -7.031250000,                                                 # 0b0010011
    0x14: -6.875000000,                                                 # 0b0010100
    0x15: -6.718750000,                                                 # 0b0010101
    0x16: -6.562500000,                                                 # 0b0010110
    0x17: -6.406250000,                                                 # 0b0010111
    0x18: -6.250000000,                                                 # 0b0011000
    0x19: -6.093750000,                                                 # 0b0011001
    0x1A: -5.937500000,                                                 # 0b0011010
    0x1B: -5.781250000,                                                 # 0b0011011
    0x1C: -5.625000000,                                                 # 0b0011100
    0x1D: -5.468750000,                                                 # 0b0011101
    0x1E: -5.312500000,                                                 # 0b0011110
    0x1F: -5.156250000,                                                 # 0b0011111
    0x20: -5.000000000,                                                 # 0b0100000
    0x21: -4.843750000,                                                 # 0b0100001
    0x22: -4.687500000,                                                 # 0b0100010
    0x23: -4.531250000,                                                 # 0b0100011
    0x24: -4.375000000,                                                 # 0b0100100
    0x25: -4.218750000,                                                 # 0b0100101
    0x26: -4.062500000,                                                 # 0b0100110
    0x27: -3.906250000,                                                 # 0b0100111
    0x28: -3.750000000,                                                 # 0b0101000
    0x29: -3.593750000,                                                 # 0b0101001
    0x2A: -3.437500000,                                                 # 0b0101010
    0x2B: -3.281250000,                                                 # 0b0101011
    0x2C: -3.125000000,                                                 # 0b0101100
    0x2D: -2.968750000,                                                 # 0b0101101
    0x2E: -2.812500000,                                                 # 0b0101110
    0x2F: -2.656250000,                                                 # 0b0101111
    0x30: -2.500000000,                                                 # 0b0110000
    0x31: -2.343750000,                                                 # 0b0110001
    0x32: -2.187500000,                                                 # 0b0110010
    0x33: -2.031250000,                                                 # 0b0110011
    0x34: -1.875000000,                                                 # 0b0110100
    0x35: -1.718750000,                                                 # 0b0110101
    0x36: -1.562500000,                                                 # 0b0110110
    0x37: -1.406250000,                                                 # 0b0110111
    0x38: -1.250000000,                                                 # 0b0111000
    0x39: -1.093750000,                                                 # 0b0111001
    0x3A: -0.937500000,                                                 # 0b0111010
    0x3B: -0.781250000,                                                 # 0b0111011
    0x3C: -0.625000000,                                                 # 0b0111100
    0x3D: -0.468750000,                                                 # 0b0111101
    0x3E: -0.312500000,                                                 # 0b0111110
    0x3F: -0.156250000,                                                 # 0b0111111
    0x40: 0.156250000,                                                  # 0b1000000
    0x41: 0.312500000,                                                  # 0b1000001
    0x42: 0.468750000,                                                  # 0b1000010
    0x43: 0.625000000,                                                  # 0b1000011
    0x44: 0.781250000,                                                  # 0b1000100
    0x45: 0.937500000,   # 0b1000101
    0x46: 1.093750000,   # 0b1000110
    0x47: 1.250000000,   # 0b1000111
    0x48: 1.406250000,   # 0b1001000
    0x49: 1.562500000,   # 0b1001001
    0x4A: 1.718750000,   # 0b1001010
    0x4B: 1.875000000,   # 0b1001011
    0x4C: 2.031250000,   # 0b1001100
    0x4D: 2.187500000,   # 0b1001101
    0x4E: 2.343750000,   # 0b1001110
    0x4F: 2.500000000,   # 0b1001111
    0x50: 2.656250000,   # 0b1010000
    0x51: 2.812500000,   # 0b1010001
    0x52: 2.968750000,   # 0b1010010
    0x53: 3.125000000,   # 0b1010011
    0x54: 3.281250000,   # 0b1010100
    0x55: 3.437500000,   # 0b1010101
    0x56: 3.593750000,   # 0b1010110
    0x57: 3.750000000,   # 0b1010111
    0x58: 3.906250000,   # 0b1011000
    0x59: 4.062500000,   # 0b1011001
    0x5A: 4.218750000,   # 0b1011010
    0x5B: 4.375000000,   # 0b1011011
    0x5C: 4.531250000,   # 0b1011100
    0x5D: 4.687500000,   # 0b1011101
    0x5E: 4.843750000,   # 0b1011110
    0x5F: 5.000000000,   # 0b1011111
    0x60: 5.156250000,   # 0b1100000
    0x61: 5.312500000,   # 0b1100001
    0x62: 5.468750000,   # 0b1100010
    0x63: 5.625000000,   # 0b1100011
    0x64: 5.781250000,   # 0b1100100
    0x65: 5.937500000,   # 0b1100101
    0x66: 6.093750000,   # 0b1100110
    0x67: 6.250000000,   # 0b1100111
    0x68: 6.406250000,   # 0b1101000
    0x69: 6.562500000,   # 0b1101001
    0x6A: 6.718750000,   # 0b1101010
    0x6B: 6.875000000,   # 0b1101011
    0x6C: 7.031250000,   # 0b1101100
    0x6D: 7.187500000,   # 0b1101101        
    0x6E: 7.343750000,   # 0b1101110
    0x6F: 7.500000000,   # 0b1101111
    0x70: 7.656250000,   # 0b1110000
    0x71: 7.812500000,   # 0b1110001
    0x72: 7.968750000,   # 0b1110010
    0x73: 8.125000000,   # 0b1110011
    0x74: 8.281250000,   # 0b1110100
    0x75: 8.437500000,   # 0b1110101
    0x76: 8.593750000,   # 0b1110110
    0x77: 8.750000000,   # 0b1110111
    0x78: 8.906250000,   # 0b1111000
    0x79: 9.062500000,   # 0b1111001
    0x7A: 9.218750000,   # 0b1111010
    0x7B: 9.375000000,   # 0b1111011
    0x7C: 9.531250000,   # 0b1111100
    0x7D: 9.687500000,   # 0b1111101
    0x7E: 9.843750000,   # 0b1111110
    0x7F: 10.000000000   # 0b1111111           
}

MatchTable_A18_C6 = {
    0x00: -10.000000000,   # 0b0000000
    0x01: -9.843750000,    # 0b0000001
    0x02: -9.687500000,    # 0b0000010
    0x03: -9.531250000,    # 0b0000011
    0x04: -9.375000000,    # 0b0000100
    0x05: -9.218750000,    # 0b0000101
    0x06: -9.062500000,    # 0b0000110
    0x07: -8.906250000,    # 0b0000111
    0x08: -8.750000000,    # 0b0001000
    0x09: -8.593750000,    # 0b0001001
    0x0A: -8.437500000,    # 0b0001010
    0x0B: -8.281250000,    # 0b0001011
    0x0C: -8.125000000,    # 0b0001100
    0x0D: -7.968750000,    # 0b0001101
    0x0E: -7.812500000,    # 0b0001110
    0x0F: -7.656250000,    # 0b0001111
    0x10: -7.500000000,    # 0b0010000
    0x11: -7.343750000,    # 0b0010001
    0x12: -7.187500000,    # 0b0010010
    0x13: -7.031250000,    # 0b0010011
    0x14: -6.875000000,    # 0b0010100
    0x15: -6.718750000,    # 0b0010101
    0x16: -6.562500000,    # 0b0010110
    0x17: -6.406250000,    # 0b0010111
    0x18: -6.250000000,    # 0b0011000
    0x19: -6.093750000,    # 0b0011001
    0x1A: -5.937500000,    # 0b0011010
    0x1B: -5.781250000,    # 0b0011011
    0x1C: -5.625000000,    # 0b0011100
    0x1D: -5.468750000,    # 0b0011101
    0x1E: -5.312500000,    # 0b0011110
    0x1F: -5.156250000,    # 0b0011111
    0x20: -5.000000000,     # 0b0100000
    0x21: -4.843750000,    # 0b0100001
    0x22: -4.687500000,    # 0b0100010
    0x23: -4.531250000,    # 0b0100011
    0x24: -4.375000000,    # 0b0100100
    0x25: -4.218750000,    # 0b0100101
    0x26: -4.062500000,    # 0b0100110
    0x27: -3.906250000,    # 0b0100111
    0x28: -3.750000000,    # 0b0101000
    0x29: -3.593750000,    # 0b0101001
    0x2A: -3.437500000,    # 0b0101010
    0x2B: -3.281250000,    # 0b0101011
    0x2C: -3.125000000,    # 0b0101100
    0x2D: -2.968750000,    # 0b0101101
    0x2E: -2.812500000,    # 0b0101110
    0x2F: -2.656250000,    # 0b0101111
    0x30: -2.500000000,    # 0b0110000
    0x31: -2.343750000,    # 0b0110001
    0x32: -2.187500000,    # 0b0110010
    0x33: -2.031250000,    # 0b0110011
    0x34: -1.875000000,    # 0b0110100
    0x35: -1.718750000,    # 0b0110101
    0x36: -1.562500000,    # 0b0110110
    0x37: -1.406250000,    # 0b0110111
    0x38: -1.250000000,    # 0b0111000
    0x39: -1.093750000,    # 0b0111001
    0x3A: -0.937500000,    # 0b0111010
    0x3B: -0.781250000,    # 0b0111011
    0x3C: -0.625000000,    # 0b0111100
    0x3D: -0.468750000,    # 0b0111101
    0x3E: -0.312500000,    # 0b0111110
    0x3F: -0.156250000,    # 0b0111111
    0x40: 0.156250000,      # 0b1000000
    0x41: 0.312500000,    # 0b1000001
    0x42: 0.468750000,    # 0b1000010
    0x43: 0.625000000,    # 0b1000011
    0x44: 0.781250000,    # 0b1000100
    0x45: 0.937500000,    # 0b1000101
    0x46: 1.093750000,    # 0b1000110
    0x47: 1.250000000,    # 0b1000111
    0x48: 1.406250000,    # 0b1001000
    0x49: 1.562500000,    # 0b1001001
    0x4A: 1.718750000,    # 0b1001010
    0x4B: 1.875000000,    # 0b1001011
    0x4C: 2.031250000,    # 0b1001100
    0x4D: 2.187500000,    # 0b1001101
    0x4E: 2.343750000,    # 0b1001110
    0x4F: 2.500000000,    # 0b1001111
    0x50: 2.656250000,    # 0b1010000
    0x51: 2.812500000,    # 0b1010001
    0x52: 2.968750000,    # 0b1010010
    0x53: 3.125000000,    # 0b1010011
    0x54: 3.281250000,    # 0b1010100
    0x55: 3.437500000,    # 0b1010101
    0x56: 3.593750000,    # 0b1010110
    0x57: 3.750000000,    # 0b1010111
    0x58: 3.906250000,     # 0b1011000
    0x59: 4.062500000,    # 0b1011001
    0x5A: 4.218750000,    # 0b1011010
    0x5B: 4.375000000,    # 0b1011011
    0x5C: 4.531250000,    # 0b1011100
    0x5D: 4.687500000,    # 0b1011101
    0x5E: 4.843750000,    # 0b1011110
    0x5F: 5.000000000,    # 0b1011111
    0x60: 5.156250000,    # 0b1100000
    0x61: 5.312500000,    # 0b1100001
    0x62: 5.468750000,    # 0b1100010
    0x63: 5.625000000,    # 0b1100011
    0x64: 5.781250000,    # 0b1100100
    0x65: 5.937500000,    # 0b1100101
    0x66: 6.093750000,    # 0b1100110
    0x67: 6.250000000,    # 0b1100111
    0x68: 6.406250000,    # 0b1101000
    0x69: 6.562500000,    # 0b1101001
    0x6A: 6.718750000,    # 0b1101010
    0x6B: 6.875000000,    # 0b1101011
    0x6C: 7.031250000,    # 0b1101100
    0x6D: 7.187500000,    # 0b1101101
    0x6E: 7.343750000,    # 0b1101110
    0x6F: 7.500000000,    # 0b1101111
    0x70: 7.656250000,    # 0b1110000
    0x71: 7.812500000,    # 0b1110001
    0x72: 7.968750000,    # 0b1110010
    0x73: 8.125000000,    # 0b1110011
    0x74: 8.281250000,    # 0b1110100
    0x75: 8.437500000,     # 0b1110101
    0x76: 8.593750000,     # 0b1110110
    0x77: 8.750000000,     # 0b1110111
    0x78: 8.906250000,     # 0b1111000
    0x79: 9.062500000,     # 0b1111001
    0x7A: 9.218750000,     # 0b1111010
    0x7B: 9.375000000,     # 0b1111011
    0x7C: 9.531250000,     # 0b1111100
    0x7D: 9.687500000,     # 0b1111101
    0x7E: 9.843750000,     # 0b1111110
    0x7F: 10.000000000     # 0b1111111      
}

MatchTable_A18_C8 = {
    0x0: 0.25,     # 0b000
    0x1: 0.5,      # 0b001
    0x2: 0.75,     # 0b010
    0x3: 1,        # 0b011
    0x4: 1.25,     # 0b100
    0x5: 1.5,      # 0b101
    0x6: 1.75,     # 0b110
    0x7: 2         # 0b111
}

MatchTable_A18_C9 = {
    0x0: 0,          # 0b00000
    0x1: 11.25,     # 0b00001
    0x2: 22.5,      # 0b00010
    0x3: 33.75,     # 0b00011
    0x4: 45,        # 0b00100
    0x5: 56.25,     # 0b00101
    0x6: 67.5,      # 0b00110
    0x7: 78.75,     # 0b00111
    0x8: 90,        # 0b01000
    0x9: 101.25,    # 0b01001
    0xA: 112.5,     # 0b01010
    0xB: 123.75,    # 0b01011
    0xC: 135,       # 0b01100
    0xD: 146.25,    # 0b01101
    0xE: 157.5,     # 0b01110
    0xF: 168.75,    # 0b01111
    0x10: 180,      # 0b10000
    0x11: 191.25,   # 0b10001
    0x12: 202.5,    # 0b10010
    0x13: 213.75,   # 0b10011
    0x14: 225,      # 0b10100
    0x15: 236.25,   # 0b10101
    0x16: 247.5,    # 0b10110
    0x17: 258.75,   # 0b10111
    0x18: 270,      # 0b11000
    0x19: 281.25,   # 0b11001
    0x1A: 292.5,    # 0b11010
    0x1B: 303.75,   # 0b11011
    0x1C: 315,      # 0b11100
    0x1D: 326.25,   # 0b11101
    0x1E: 337.5,    # 0b11110
    0x1F: 348.75    # 0b11111
}

MatchTable_A18_C10 = {
    0x0: 'IC-C-01',    # 0b00000
    0x1: 'IC-C-02',    # 0b00001
    0x2: 'IC-C-03',    # 0b00010
    0x3: 'IC-C-04',    # 0b00011
    0x4: 'IC-C-05',    # 0b00100
    0x5: 'IC-C-06',    # 0b00101
    0x6: 'IC-C-07',    # 0b00110
    0x7: 'IC-C-08',    # 0b00111
    0x8: 'IC-C-09',    # 0b01000
    0x9: 'IC-C-10',    # 0b01001
    0xA: 'IC-C-11',    # 0b01010
    0xB: 'IC-C-12',    # 0b01011
    0xC: 'IC-C-13',    # 0b01100
    0xD: 'IC-C-14',    # 0b01101
    0xE: 'IC-C-15',    # 0b01110
    0xF: 'IC-C-16',    # 0b01111
    0x10: 'IC-C-17',   # 0b10000
    0x11: 'IC-C-18',   # 0b10001
    0x12: 'IC-C-19',   # 0b10010
    0x13: 'IC-C-20',   # 0b10011
    0x14: 'IC-C-21',   # 0b10100
    0x15: 'IC-C-22',   # 0b10101
    0x16: 'IC-C-23',    # 0b10110
    0x17: 'IC-C-24',    # 0b10111
    0x18: 'IC-C-25',    # 0b11000
    0x19: 'IC-C-26',    # 0b11001
    0x1A: 'IC-C-27',    # 0b11010
    0x1B: 'IC-C-28',    # 0b11011
    0x1C: 'IC-C-29',    # 0b11100
    0x1D: 'IC-C-30',    # 0b11101
    0x1E: 'IC-C-31',    # 0b11110
    0x1F: 'IC-C-32'     # 0b11111
}
    
MatchTable_A18_D1 = {
    0x0: "1.0-1.9",            # 0b0000
    0x1: "2.0-2.9",            # 0b0001
    0x2: "3.0-3.9",            # 0b0010
    0x3: "4.0-4.9",            # 0b0011
    0x4: "5.0-5.9",            # 0b0100
    0x5: "6.0-6.9",            # 0b0101
    0x6: "7.0-7.9",            # 0b0110
    0x7: "8.0-8.9",            # 0b0111
    0x8: "9.0 and greater"     # 0b1000
}

MatchTable_A18_D2 = {
    0x0: "2",              # 0b000
    0x1: "3",              # 0b001
    0x2: "4",              # 0b010
    0x3: "5 weak",         # 0b011
    0x4: "5 strong",       # 0b100
    0x5: "6 weak",         # 0b101
    0x6: "6 strong",       # 0b110
    0x7: "7"               # 0b111
}
            
MatchTable_A18_D3 = {
    0x0: 0,      # 0b0000
    0x1: 22,     # 0b0001
    0x2: 45,     # 0b0010
    0x3: 67,     # 0b0011
    0x4: 90,     # 0b0100
    0x5: 112,    # 0b0101
    0x6: 135,    # 0b0110
    0x7: 157,    # 0b0111
    0x8: 180,    # 0b1000
    0x9: 202,    # 0b1001
    0xA: 225,    # 0b1010
    0xB: 247,    # 0b1011
    0xC: 270,    # 0b1100
    0xD: 292,    # 0b1101
    0xE: 315,    # 0b1110
    0xF: 337     # 0b1111
}

MatchTable_A18_D4 = {
    0x0: 0.25,   # 0b0000
    0x1: 0.5,    # 0b0001
    0x2: 0.75,   # 0b0010
    0x3: 1.0,    # 0b0011
    0x4: 2.0,    # 0b0100
    0x5: 3.0,    # 0b0101
    0x6: 5.0,    # 0b0110
    0x7: 10.0,   # 0b0111
    0x8: 20.0,   # 0b1000
    0x9: 30.0,   # 0b1001
    0xA: 40.0,   # 0b1010
    0xB: 50.0,   # 0b1011
    0xC: 70.0,   # 0b1100
    0xD: 100.0,  # 0b1101
    0xE: 150.0,  # 0b1110
    0xF: 200.0   # 0b1111
}

MatchTable_A18_D5 = {
    0x0: "H ≤ 0.5",          # 0b000
    0x1: "0.5 < H ≤ 1.0",    # 0b001
    0x2: "1.0 < H ≤ 1.5",    # 0b010
    0x3: "1.5 < H ≤ 2.0",    # 0b011
    0x4: "2.0 < H ≤ 3.0",    # 0b100
    0x5: "3.0 < H ≤ 5.0",    # 0b101
    0x6: "5.0 < H ≤ 10.0",   # 0b110
    0x7: "H > 10.0"          # 0b111
}

MatchTable_A18_D6 = {
    0x0: "T ≤ -30",             # 0b0000
    0x1: "-30 < T ≤ -25",       # 0b0001
    0x2: "-25 < T ≤ -20",       # 0b0010
    0x3: "-20 < T ≤ -15",       # 0b0011
    0x4: "-15 < T ≤ -10",       # 0b0100
    0x5: "-10 < T ≤ -5",        # 0b0101
    0x6: "-5 < T ≤ 0",          # 0b0110
    0x7: "0 < T ≤ 5",           # 0b0111
    0x8: "5 < T ≤ 10",          # 0b1000
    0x9: "10 < T ≤ 15",         # 0b1001
    0xA: "15 < T ≤ 20",         # 0b1010
    0xB: "20 < T ≤ 25",         # 0b1011
    0xC: "25 < T ≤ 30",         # 0b1100
    0xD: "30 < T ≤ 35",         # 0b1101
    0xE: "35 < T ≤ 45",         # 0b1110
    0xF: "T > 45"               # 0b1111
}

MatchTable_A18_D7 = {
    0x0: ("Category 1/5 hurricane: Very dangerous winds will produce some damage. Winds range from 120 to "
          "150 km/h. Falling debris could strike people, livestock and pets, and older mobile homes could be "
          "destroyed. Protected glass windows will generally make it through the hurricane without major "
          "damage. Frame homes, apartments and shopping centres may experience some damage, and "
          "snapped power lines could result in short-term power outages."),  # 0b000
    0x1: ("Category 2/5 hurricane: Extremely dangerous winds will cause extensive damage. Winds range "
          "between 150 and 180 km/h. There is a bigger risk of injury or death to people, livestock and pets from "
          "flying debris. Older mobile homes will likely be destroyed, and debris can ruin newer mobile homes, "
          "too. Frame homes, apartment buildings and shopping centres may see major roof and siding damage, "
          "and many trees will be uprooted. Residents should expect near total power loss after a Category 2 "
          "hurricane, with outages lasting anywhere from a few days to a few weeks."),  # 0b001
    0x2: ("Category 3/5 hurricane: Devastating damage will occur. In a Category 3 hurricane, winds range from "
          "180 to 210 km/h. There is a high risk of injury or death to people, livestock and pets from flying and "
          "falling debris. Nearly all older mobile homes will be destroyed, and most new ones will experience "
          "significant damage. Even well-built frame homes, apartments and industrial buildings will likely "
          "experience major damage, and the storm will uproot many trees that may block roads. Electricity and "
          "water will likely be unavailable for several days to a few weeks after the storm."),  # 0b010
    0x3: ("Category 4/5 hurricane: Catastrophic damage will occur. During a Category 4 hurricane, winds range "
          "from 210 to 250 km/h. At these speeds, falling and flying debris poses a very high risk of injury or "
          "death to people, pets and livestock. Again, most mobile homes will be destroyed, even newer ones. "
          "Some frame homes may totally collapse, while well-built homes will likely see severe damage to their "
          "roofs, and apartment buildings can experience damage to upper floors. A Category 4 hurricane will " 
          "blow out most windows on high-rise buildings, uproot most trees and will likely down many power "
          "lines."),  # 0b011
    0x4: ("Category 5/5 hurricane: Catastrophic damage will occur. In a Category 5 hurricane, the highest "
          "category hurricane, winds are 250 km/h or higher. People, livestock and pets can be in danger from "
          "flying debris, even indoors. Most mobile homes will be completely destroyed, and a high percentage "
          "of frame homes will be destroyed. Commercial buildings with wood roofs will experience severe "
          "damage, metal buildings may collapse and high-rise windows will nearly all be blown out. A Category "
          "5 hurricane is likely to uproot most trees and ruin most power poles. People should expect long-term "
          "water shortages and power outages.")  # 0b100
}

MatchTable_A18_D8 = {
    0x0: "Beaufort 0. 0 km/h < v < 1 km/h - Calm",                # 0b0000
    0x1: "Beaufort 1. 1 km/h < v < 5 km/h - Light Air",          # 0b0001
    0x2: "Beaufort 2. 6 km/h < v < 11 km/h - Light Breeze",      # 0b0010
    0x3: "Beaufort 3. 12 km/h < v < 19 km/h - Gentle Breeze",    # 0b0011
    0x4: "Beaufort 4. 20 km/h < v < 30 km/h - Moderate Breeze",  # 0b0100
    0x5: "Beaufort 5. 31 km/h < v < 39 km/h - Fresh Breeze",     # 0b0101
    0x6: "Beaufort 6. 40 km/h < v < 50 km/h - Strong Breeze",    # 0b0110
    0x7: "Beaufort 7. 51 km/h < v < 61 km/h - Near Gale",        # 0b0111
    0x8: "Beaufort 8. 62 km/h < v < 74 km/h - Gale",             # 0b1000
    0x9: "Beaufort 9. 75 km/h < v < 88 km/h - Strong Gale",      # 0b1001
    0xA: "Beaufort 10. 89 km/h < v < 102 km/h - Storm",          # 0b1010
    0xB: "Beaufort 11. 103 km/h < v < 117 km/h - Violent Storm", # 0b1011
    0xC: "Beaufort 12. V > 118 km/h - Hurricane",                # 0b1100
    0xD: "not used",                                             # 0b1101
    0xE: "not used",                                             # 0b1110
    0xF: "not used"                                              # 0b1111
}

MatchTable_A18_D9 = {
    0x0: "p ≤ 2.5 mm/h",        # 0b000
    0x1: "2.5 < p ≤ 7.5 mm/h",  # 0b001
    0x2: "7.5 < p ≤ 10 mm/h",   # 0b010
    0x3: "10 < p ≤ 20 mm/h",    # 0b011
    0x4: "20 < p ≤ 30 mm/h",    # 0b100
    0x5: "30 < p ≤ 50 mm/h",    # 0b101
    0x6: "50 < p ≤ 80 mm/h",    # 0b110
    0x7: "80 < p mm/h"          # 0b111
}

MatchTable_A18_D10 = {
    0x0: "Category 1 - Very dangerous winds will produce some damage. Scale 1 and Intensity 1",   # 0b000
    0x1: "Category 2 - Extremely dangerous winds will cause extensive damage. Scale 1 and Intensity 2",   # 0b001
    0x2: "Category 3 - Devastating damage will occur. Scale 1 and Intensity 3",   # 0b010
    0x3: "Category 4 - Catastrophic damage will occur. Scale 2 and Intensity 1",   # 0b011
    0x4: "Category 5 - Catastrophic damage will occur. Scale 2 and Intensity 2",   # 0b100
    0x5: "Category 5 - Catastrophic damage will occur. Scale 3 and Intensity 3",   # 0b101
    0x6: "not used",   # 0b110
    0x7: "not used"    # 0b111
}

MatchTable_A18_D11 = {
    0x0: """Non-Threatening
- Threat: No discernible threat to life and property.
- Minimum Action: Listen for forecast changes; review tornado safety rules.
- Potential Impact: None expected; strong wind gusts may still occur.""",  # 0b000
    0x1: """Very Low
- Threat: A very low threat to life and property.
- Minimum Action: Preparations should be made for a very low likelihood (or a 2 to 4% probability) of tornadoes; isolated tornadoes of F0 to F1 intensity possible.
- Potential Impact: The potential for isolated locations to experience minor to moderate tornado damage.""",  # 0b001
    0x2: """Low
- Threat: A low threat to life and property.
- Minimum Action: Preparations should be made for a low likelihood (or a 5 to 14% probability) of tornadoes; scattered tornadoes of F0 to F1 intensity possible.
- Potential Impact: The potential for scattered locations to experience minor to moderate tornado damage.""",  # 0b010
    0x3: """Moderate
- Threat: A moderate threat to life and property.
- Minimum Action: Preparations should be made for a moderate likelihood (or a 15 to 29% probability) of tornadoes; many tornadoes (even families) of F0 to F1 intensity possible.
- Potential Impact: The potential for many locations to experience minor to moderate tornado damage (see below). Some tornadoes may have longer damage tracks.""",  # 0b011
    0x4: """High
- Threat: A high threat to life and property.
- Minimum Action: Preparations should be made for a high likelihood (or a 30 to 44% probability) of tornadoes; scattered tornadoes possible with isolated tornadoes of F2 to F5 intensity also possible.
- Potential Impact: The potential for isolated locations to experience major tornado damage (see below), among scattered locations of minor to moderate tornado damage. Some tornadoes may have longer damage tracks.""",  # 0b100
    0x5: """Extreme
- Threat: An extreme threat to life and property.
- Minimum Action: Preparations should be made for a very high likelihood (or a 45% probability or greater) of tornadoes; many tornadoes (even families) possible with scattered tornadoes of F2 to F5 intensity also possible.
- Potential Impact: The potential for scattered locations to experience major tornado damage (see below), among many locations of minor to moderate tornado damage. Some tornadoes may have longer damage tracks.""",  # 0b101
    0x6: "not used",  # 0b110
    0x7: "not used"   # 0b111
}

MatchTable_A18_D12 = {
    0x0: "H0 - Hard hail. Typical hail diameter of 5 mm. No damage",  # 0b0000
    0x1: "H1 - Potentially damaging. Typical hail diameter of 5-15 mm. Slight general damage to plants, crops",  # 0b0001
    0x2: "H2 - Significant. Typical hail diameter of 10-20 mm. Slight general damage to fruit, crops, vegetation",  # 0b0010
    0x3: "H3 - Severe. Typical hail diameter of 20-30 mm (size of a walnut). Severe damage to fruit and crops, damage to glass and plastic structures, paint and wood scored",  # 0b0011
    0x4: "H4 - Severe. Typical hail diameter of 25-40 mm (size of a squash ball). Widespread glass damage, vehicle bodywork damage",  # 0b0100
    0x5: "H5 - Destructive. Typical hail diameter of 30-50 mm (size of a golf ball). Wholesale destruction of glass, damage to tiled roofs, significant risk of injuries",  # 0b0101
    0x6: "H6 - Destructive. Typical hail diameter of 40-60 mm. Bodywork of grounded aircraft dented, brick walls pitted",  # 0b0110
    0x7: "H7 - Destructive. Typical hail diameter of 50-75 mm (size of a tennis ball). Severe roof damage, risk of serious injuries",  # 0b0111
    0x8: "H8 - Destructive. Typical hail diameter of 60-90 mm (size of a large orange). Severe damage to aircraft bodywork",  # 0b1000
    0x9: "H9 - Super Hailstorms. Typical hail diameter of 75-100 mm (size of a grapefruit). Extensive structural damage. Risk of severe or even fatal injuries to persons caught in the open",  # 0b1001
    0xA: "H10 - Super Hailstorms. Typical hail diameter > 100 mm (size of a melon). Extensive structural damage. Risk of severe or even fatal injuries to persons caught in the open"  # 0b1010
}

MatchTable_A18_D13 = {
    0x0: "Dense fog: visibility < 20 m",  # 0b0000
    0x1: "Thick fog: 20 m < visibility < 200 m",  # 0b0001
    0x2: "Moderate fog: 200 m < visibility < 500 m",  # 0b0010
    0x3: "Light fog: 500 m < visibility < 1000 m",  # 0b0011
    0x4: "Thin fog: 1 km < visibility < 2 km",  # 0b0100
    0x5: "Haze: 2 km < visibility < 4 km",  # 0b0101
    0x6: "Light haze: 4 km < visibility < 10 km",  # 0b0110
    0x7: "Clear: 10 km < visibility < 20 km",  # 0b0111
    0x8: "Very clear: 20 km < visibility < 50 km",  # 0b1000
    0x9: "Exceptionally clear: visibility > 50 km"  # 0b1001
}

MatchTable_A18_D14 = {
    0x0: "0 < daily snow depth ≤ 20 cm",  # 0b00000
    0x1: "20 < daily snow depth ≤ 40 cm",  # 0b00001
    0x2: "40 < daily snow depth ≤ 60 cm",  # 0b00010
    0x3: "60 < daily snow depth ≤ 80 cm",  # 0b00011
    0x4: "80 < daily snow depth ≤ 100 cm",  # 0b00100
    0x5: "100 < daily snow depth ≤ 120 cm",  # 0b00101
    0x6: "120 < daily snow depth ≤ 140 cm",  # 0b00110
    0x7: "140 < daily snow depth ≤ 160 cm",  # 0b00111
    0x8: "160 < daily snow depth ≤ 180 cm",  # 0b01000
    0x9: "180 < daily snow depth ≤ 200 cm",  # 0b01001
    0xA: "200 < daily snow depth ≤ 220 cm",  # 0b01010
    0xB: "220 < daily snow depth ≤ 240 cm",  # 0b01011
    0xC: "240 < daily snow depth ≤ 260 cm",  # 0b01100
    0xD: "260 < daily snow depth ≤ 280 cm",  # 0b01101
    0xE: "280 < daily snow depth ≤ 300 cm",  # 0b01110
    0xF: "300 < daily snow depth ≤ 320 cm",  # 0b01111
    0x10: "320 < daily snow depth ≤ 340 cm",  # 0b10000
    0x11: "340 < daily snow depth ≤ 360 cm",  # 0b10001
    0x12: "360 < daily snow depth ≤ 380 cm",  # 0b10010
    0x13: "380 < daily snow depth ≤ 400 cm",  # 0b10011
    0x14: "400 < daily snow depth ≤ 420 cm",  # 0b10100
    0x15: "420 < daily snow depth ≤ 440 cm",  # 0b10101
    0x16: "440 < daily snow depth ≤ 460 cm",  # 0b10110
    0x17: "460 < daily snow depth ≤ 480 cm",  # 0b10111
    0x18: "480 < daily snow depth ≤ 500 cm",  # 0b11000
    0x19: "500 < daily snow depth ≤ 520 cm",  # 0b11001
    0x1A: "520 < daily snow depth ≤ 540 cm",  # 0b11010
    0x1B: "540 < daily snow depth ≤ 560 cm",  # 0b11011
    0x1C: "560 < daily snow depth ≤ 580 cm",  # 0b11100
    0x1D: "580 < daily snow depth ≤ 600 cm",  # 0b11101
    0x1E: "daily snow depth > 600 cm",  # 0b11110
    0x1F: "not used"  # 0b11111
}

MatchTable_A18_D15 = {
    0x0: "Minor Flooding - minimal or no property damage, but possibly some public threat.",  # 0b00
    0x1: "Moderate Flooding - some inundation of structures and roads near stream. Some evacuations of people and/or transfer of property to higher elevations.",  # 0b01
    0x2: "Major Flooding - extensive inundation of structures and roads. Significant evacuations of people and/or transfer of property to higher elevations.",  # 0b10
    0x3: "Record Flooding"  # 0b11
}

MatchTable_A18_D16 = {
    0x0: "LAL 1 - No thunderstorms",  # 0b000
    0x1: "LAL 2 - Isolated thunderstorms. Light rain will occasionally reach the ground. Lightning is very infrequent, 1 to 5 cloud to ground strikes in a 5-minute period.",  # 0b001
    0x2: "LAL 3 - Widely scattered thunderstorms. Light to moderate rain will reach the ground. Lightning is infrequent, 6 to 10 cloud to ground strikes in a 5-minute period.",  # 0b010
    0x3: "LAL 4 - Scattered thunderstorms. Moderate rain is commonly produced. Lightning is frequent, 11 to 15 cloud to ground strikes in a 5-minute period.",  # 0b011
    0x4: "LAL 5 - Numerous thunderstorms. Rainfall is moderate to heavy. Lightning is frequent and intense, greater than 15 cloud to ground strikes in a 5-minute period.",  # 0b100
    0x5: "LAL 6 - Dry lightning (same as LAL 3 but without rain). This type of lightning has the potential for extreme fire activity and is normally highlighted in fire weather forecasts with a Red Flag Warning."  # 0b101
}

MatchTable_A18_D17 = {
    0x0: "Level 1 of 5: Slight fog or Mist. On land, objects appear hazy or blurry. Road and rail traffic are unhindered. On sea, the horizon cannot be seen. Lights and landmarks can be seen at working distances.",  # 0b000
    0x1: "Level 2 of 5: Slight fog. On land, railroad traffic takes additional caution. On sea, lights on passing vessels are generally not distinct at distances under 1 mile. Fog signals are sounded.",  # 0b001
    0x2: "Level 3 of 5: Moderate fog. On land, rail and road traffic is obstructed. On sea, lights on passing vessels are generally not distinct at distances under 1 mile. Fog signals are sounded. On rivers, navigation is unhindered but extra caution is required.",  # 0b010
    0x3: "Level 4 of 5: Moderate fog. On land, rail and road traffic is impeded. On sea, lights on ships and other vessels cannot be seen at distances of 4 miles or less. On rivers, navigation is suspended.",  # 0b011
    0x4: "Level 5 of 5: Thick fog. On land, all traffic is impeded and totally disorganized. On sea, lights on ships and other vessels cannot be seen at distances of 4 miles or less. On rivers, navigation is suspended."  # 0b100
}

MatchTable_A18_D18 = {
    0x0: "D1 – Moderate Drought – PDSI = -2.0 to -2.9\n\t\tSome damage to crops, pastures\n\t\tStreams, reservoirs, or wells low, some water shortages developing or imminent\n\t\tVoluntary water-use restrictions requested",  # 0b00
    0x1: "D2 – Severe Drought – PDSI = -3.0 to -3.9\n\t\tCrop or pasture losses likely\n\t\tWater shortages common\n\t\tWater restrictions imposed",  # 0b01
    0x2: "D3 – Extreme Drought – PDSI = -4.0 to -4.9\n\t\tMajor crop/pasture losses\n\t\tWidespread water shortages or restrictions",  # 0b10
    0x3: "D4 – Exceptional Drought – PDSI = -5.0 or less\n\t\tExceptional and widespread crop/pasture losses\n\t\tShortages of water in reservoirs, streams, and wells creating water emergencies"  # 0b11
}

MatchTable_A18_D19 = {
    0x0: "1 – Low.\nGenerally stable conditions.\nTriggering is generally possible only from high additional loads in isolated areas of very steep, extreme terrain. Only small and medium natural avalanches are possible.",  # 0b000
    0x1: "2 – Moderate.\nHeightened avalanche conditions on specific terrain features.\nTriggering is possible, primarily from high additional loads, particularly on the indicated steep slopes. Very large natural avalanches are unlikely.",  # 0b001
    0x2: "3 – Considerable.\nDangerous avalanche conditions.\nTriggering is possible, even from low additional loads, particularly on the indicated steep slopes. In certain situations, some large, and in isolated cases very large natural avalanches are possible.",  # 0b010
    0x3: "4 – High.\nVery dangerous avalanche conditions.\nTriggering is likely, even from low additional loads, on many steep slopes. In some cases, numerous large and often very large natural avalanches can be expected.",  # 0b011
    0x4: "5 – Very high.\nExtraordinary avalanche conditions.\nNumerous very large and often extremely large natural avalanches can be expected, even in moderately steep terrain."  # 0b100
}

MatchTable_A18_D20 = {
    0x0: ("Less than 1 mm ash thickness.\n"
          "Possible impact: Will act as an irritant to lungs and eyes. Possible minor damage to vehicles, houses, and equipment caused by fine abrasive ash. Possible contamination of water supplies, particularly roof-fed tank supplies. Dust may affect road visibility and traction for an extended period."),  # 0b000
    0x1: ("1-5 mm ash thickness.\n"
          "Possible impact: Will act as an irritant to lungs and eyes. Minor damage to vehicles, houses, and equipment caused by fine abrasive ash. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Dust may affect road visibility and traction for an extended period. Roads may need to be cleared to reduce the dust nuisance and prevent storm-water systems from becoming blocked. Possible crop damage. Some livestock may be affected."),  # 0b001
    0x2: ("5-100 mm ash thickness.\n"
          "Possible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Most buildings will support the ash load but weaker roof structures may collapse at 100 mm ash thickness, particularly if the ash is wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road transport may be halted due to the build-up of ash on roads. Cars still working may soon stop due to clogging of air-filters. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Likely crop damage. Most pastures will be killed by over 50 mm of ash. Some livestock may be affected."),  # 0b010
    0x3: ("100-300 mm ash thickness.\n"
          "Possible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Buildings that are not cleared of ash will run the risk of roof collapse, especially large flat-roofed structures and if ash becomes wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road transport may be halted due to the build-up of ash on roads. Cars still working may soon stop due to clogging of air-filters. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Likely crop damage. Most pastures will be killed by over 50 mm of ash. Some livestock may be affected."),  # 0b011
    0x4: ("> 300 mm ash thickness.\n"
          "Possible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Buildings that are not cleared of ash will run the risk of roof collapse, especially large flat-roofed structures and if ash becomes wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road unusable until cleared. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Heavy kill of vegetation. Livestock and other animals killed or heavily distressed.")  # 0b100
}

MatchTable_A18_D21 = {
    0x0: """G1 - Minor
Power systems: Weak power grid fluctuations can occur.
Spacecraft operations: Minor impact on satellite operations possible.
Other systems: Migratory animals are affected at this and higher levels; aurora is commonly visible at high latitudes.""",  # 0b000
    0x1: """G2 - Moderate
Power systems: High-latitude power systems may experience voltage alarms, long-duration storms may cause transformer damage.
Spacecraft operations: Corrective actions to orientation may be required by ground control; possible changes in drag affect orbit predictions.
Other systems: HF radio propagation can fade at higher latitudes, and aurora has been seen as low as 55° geomagnetic lat.""",  # 0b001
    0x2: """G3 - Strong
Power systems: Voltage corrections may be required, false alarms triggered on some protection devices.
Spacecraft operations: Surface charging may occur on satellite components, drag may increase on low-Earth-orbit satellites, and corrections may be needed for orientation problems.
Other systems: Intermittent satellite navigation and low-frequency radio navigation problems may occur, HF radio may be intermittent, and aurora has been seen as low as 50° geomagnetic lat.""",  # 0b010
    0x3: """G4 - Severe
Power systems: Possible widespread voltage control problems and some protective systems will mistakenly trip out key assets from the grid.
Spacecraft operations: May experience surface charging and tracking problems, corrections may be needed for orientation problems.
Other systems: Induced pipeline currents affect preventive measures, HF radio propagation sporadic, satellite navigation degraded for hours, low-frequency radio navigation disrupted, and aurora has been seen as low as 45° geomagnetic lat.""",  # 0b011
    0x4: """G5 - Extreme
Power systems: Widespread voltage control problems and protective system problems can occur; some grid systems may experience complete collapse or blackouts. Transformers may experience damage.
Spacecraft operations: May experience extensive surface charging, problems with orientation, uplink/downlink, and tracking satellites.
Other systems: Pipeline currents can reach hundreds of amps, HF (high frequency) radio propagation may be impossible in many areas for one to two days, satellite navigation may be degraded for days, low-frequency radio navigation can be out for hours, and aurora has been seen as low as 40° geomagnetic lat."""  # 0b100
}

MatchTable_A18_D22 = {
    0x0: "Very low threat level. A violent act of terrorism is highly unlikely. Measures are in place to keep the population safe.",  # 0b000
    0x1: "Low threat level. A violent act of terrorism is possible but unlikely. Measures are in place to keep the population safe.",  # 0b001
    0x2: "Medium threat level. A violent act of terrorism could occur. Additional measures are in place to keep the population safe.",  # 0b010
    0x3: "High threat level. A violent act of terrorism is likely. Heightened measures are in place to keep the population safe.",  # 0b011
    0x4: "Critical threat level. A violent act of terrorism is highly likely and could occur imminently. Exceptional measures are in place to keep the population safe."  # 0b100
}

MatchTable_A18_D23 = {
    0x0: """Danger level 1/5 (low or none danger). Small fires cannot be entirely ruled out, but require a high energy input. Lightning hardly ever causes a fire. Rate of spread: Generally slow. Characteristics: Surface or crawling fires, crowns of trees are not affected, topsoil does not burn. Fire-fighting: Forest fire is easy to extinguish. Behaviour: Do not carelessly discard cigarettes, tobacco products or lighters.""",  # 0b000
    0x1: """Danger level 2/5 (moderate danger). Local fires can start spontaneously. Lightning only rarely causes a conflagration. Rate of spread: Slow to medium. Characteristics: Surface or crawling fires, crowns of trees are rarely affected, topsoil is burnt a little or not at all. Fire-fighting: Forest fire is ordinarily easy to extinguish. Behaviour: Do not carelessly discard cigarettes, tobacco products or lighters. Always watch barbecue fires and immediately extinguish stray sparks.""",  # 0b001
    0x2: """Danger level 3/5 (considerable danger): Burning matches and flying sparks from barbecue fires can ignite a fire. Lightning can also trigger widespread fires. Rate of spread: High in open terrain, medium in the forest. Characteristics. Topsoil is partly burnt; individual crown fires are possible. Fire-fighting: Forest fire can be extinguished only by experts using modern equipment. Behaviour: Light barbecue fires only in existing fire places. Always watch the fire and immediately extinguish stray sparks.""",  # 0b010
    0x3: """Danger level 4/5 (high danger). Burning matches, flying sparks from barbecue fires and lightning will very probably ignite a fire. Rate of spread: High, including in forests. Characteristics: Intense surface fires can ignite the crowns of individual trees, spotting is possible, burning topsoil. Fire-fighting: Forest fire is difficult to extinguish and commands extensive resources. Behaviour: As a general rule, do not make any fires outdoors. Permanent fire places (concreted base) in locations designated by the authorities can be used with the utmost caution. Do not make fires in strong winds.""",  # 0b011
    0x4: """Danger level 5/5 (very high danger). Fires can start at any time. Rate of spread: Very high over a long period. Characteristics: Very intense burning, extensive crown fires, long-distance spotting. Fire-fighting: Forest fire is virtually impossible to extinguish. Behaviour: Do not make any fires outdoors. Follow the instructions and observe the fire bans imposed by the local authorities."""  # 0b100
}

MatchTable_A18_D24 = {
    0x0: "Excellent water quality",  # 0b000
    0x1: "Good water quality",  # 0b001
    0x2: "Poor water quality",  # 0b010
    0x3: "Very poor water quality",  # 0b011
    0x4: "Suitable for drinking purposes",  # 0b100
    0x5: "Unsuitable for drinking purpose",  # 0b101
    0x6: "not used",  # 0b110
    0x7: "not used"  # 0b111
}

MatchTable_A18_D25 = {
    0x0: "Index 0 - 2 Low. No protection needed. You can safely stay outside using minimal sun protection.",  # 0b0000
    0x1: "Index 3/11 Moderate. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",  # 0b0001
    0x2: "Index 4/11 Moderate. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",  # 0b0010
    0x3: "Index 5/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",  # 0b0011
    0x4: "Index 6/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",  # 0b0100
    0x5: "Index 7/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",  # 0b0101
    0x6: "Index 8/11 Very high. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",  # 0b0110
    0x7: "Index 9/11 Very high. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",  # 0b0111
    0x8: "Index 10/11 Extreme. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",  # 0b1000
    0x9: "Index 11/11 Extreme. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin."  # 0b1001
}
            
MatchTable_A18_D26 = {
    0x0: "0 - 9",  # 0b00000
    0x1: "10 - 20",  # 0b00001
    0x2: "21 - 50",  # 0b00010
    0x3: "51 - 70",  # 0b00011
    0x4: "71 - 100",  # 0b00100
    0x5: "101 - 125",  # 0b00101
    0x6: "126 - 150",  # 0b00110
    0x7: "151 - 175",  # 0b00111
    0x8: "176 - 200",  # 0b01000
    0x9: "201 - 250",  # 0b01001
    0xA: "251 - 300",  # 0b01010
    0xB: "301 - 350",  # 0b01011
    0xC: "351 - 400",  # 0b01100
    0xD: "401 - 450",  # 0b01101
    0xE: "451 - 500",  # 0b01110
    0xF: "501 - 750",  # 0b01111
    0x10: "751 - 1000",  # 0b10000
    0x11: "> 1000",  # 0b10001
    0x12: "> 2000",  # 0b10010
    0x13: "> 3000",  # 0b10011
    0x14: "> 5000"  # 0b10100
}

MatchTable_A18_D27 = {
        0b0000: "40 < dB ≤ 45",
        0b0001: "45 < dB ≤ 50",
        0b0010: "50 < dB ≤ 60",
        0b0011: "60 < dB ≤ 70",
        0b0100: "70 < dB ≤ 80 (loud)",
        0b0101: "80 < dB ≤ 90 (very loud)",
        0b0110: "90 < dB ≤ 100 (very loud)",
        0b0111: "100 < dB ≤ 110 (very loud)",
        0b1000: "110 < dB ≤ 120 (extremely loud)",
        0b1001: "120 < dB ≤ 130 (extremely loud)",
        0b1010: "130 < dB ≤ 140 (threshold of pain)",
        0b1011: "dB > 140 (pain)",
        0b1100: "not used",
        0b1101: "not used",
        0b1110: "not used",
        0b1111: "not used"
}

MatchTable_A18_D28 = {
    0x0: "Index value 0 - 50. Good. Green. Advisory: None",  # 0b000
    0x1: "Index value 51 - 100. Moderate. Yellow. Unusually sensitive individuals should consider limiting prolonged outdoor exertion",  # 0b001
    0x2: "Index value 101 - 150. Unhealthy for sensitive groups. Orange. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion",  # 0b010
    0x3: "Index value 151 - 200. Unhealthy. Red. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. Everyone else should limit prolonged outdoor exertion.",  # 0b011
    0x4: "Index value 201 - 300. Very unhealthy. Purple. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. Everyone else should limit outdoor exertion.",  # 0b100
    0x5: "Index value 301 - 500. Hazardous. Brown. Everyone should avoid all physical activity outdoors."  # 0b101
}

MatchTable_A18_D29 = {
    0x0: "0 < duration < 30 min",  # 0b00000
    0x1: "30 min ≤ duration < 45 min",  # 0b00001
    0x2: "45 min ≤ duration < 1 h",  # 0b00010
    0x3: "1 h ≤ duration < 1h 30min",  # 0b00011
    0x4: "1h 30min ≤ duration < 2 h",  # 0b00100
    0x5: "2 h ≤ duration < 3 h",  # 0b00101
    0x6: "3 h ≤ duration < 4 h",  # 0b00110
    0x7: "4 h ≤ duration < 5 h",  # 0b00111
    0x8: "5 h ≤ duration < 10 h",  # 0b01000
    0x9: "10 h ≤ duration < 24 h",  # 0b01001
    0xA: "24 h ≤ duration < 2 days",  # 0b01010
    0xB: "2 days ≤ duration < 7 days",  # 0b01011
    0xC: "7 days ≤ duration",  # 0b01100
    0xD: "Unknown",  # 0b01101
    0xE: "not used",  # 0b01110
    0xF: "not used",  # 0b01111
    0x10: "not used"  # 0b10000
}

MatchTable_A18_D30 = {
    0x0: "Unknown",  # 0b0000
    0x1: "Level 0/7. Deviation. No safety significance",  # 0b0001
    0x2: "Level 1/7. Anomaly. Overexposure in excess of statutory annual limits. Minor problems with safety components with significant defence-in-depth remaining. Low activity lost or stolen radioactive source, device, or transport package.",  # 0b0010
    0x3: "Level 2/7. Incident. Impact on people and environment: Exposure of the public in excess of 10 mSv. Exposure of workers in excess of the statutory annual limits. Impact on radiological barriers and control: Radiation levels in an operating area of more than 50 mSv/h. Significant contamination within the facility into an area not expected by design. Possible cause: Significant failures in safety provisions but with no actual consequences. Found highly radioactive sealed orphan source, device or transport package with safety provisions intact. Inadequate packaging of a highly radioactive sealed source.",  # 0b0011
    0x4: "Level 3/7. Serious incident. Impact on people and environment: Exposure in excess of ten times the statutory annual limit for workers. Non-lethal deterministic health effect (e.g., burns) from radiation. Impact on radiological barriers and control: Exposure rates of more than 1 Sv/h in an operating area. Severe contamination in an area not expected by design, with a low probability of significant public exposure. Possible cause: Near-accident at a nuclear power plant with no safety provisions remaining. Lost or stolen highly radioactive sealed source. Misdelivered highly radioactive sealed source without adequate procedures in place to handle it.",  # 0b0100
    0x5: "Level 4/7. Accident with local consequences. Impact on people and environment: Minor release of radioactive material unlikely to result in implementation of planned countermeasures other than local food controls. Impact on radiological barriers and control: Release of significant quantities of radioactive material within an installation with a high probability of significant public exposure.",  # 0b0101
    0x6: "Level 5/7. Accident with wider consequences. Impact on people and environment: Limited release of radioactive material likely to require implementation of some planned countermeasures. Major health impact from radiation is likely. Impact on radiological barriers and control: Severe damage to the reactor core. Release of large quantities of radioactive material within an installation with a high probability of significant public exposure. This could arise from a major criticality accident or fire.",  # 0b0110
    0x7: "Level 6/7. Serious accident. Impact on people and environment: Significant release of radioactive material likely to require implementation of planned countermeasures.",  # 0b0111
    0x8: "Level 7/7. Major accident. Impact on people and environment: Major release of radioactive material with widespread health and environmental effects requiring implementation of planned and extended countermeasures."  # 0b1000
}

MatchTable_A18_D31 = {
    0x0: "Explosives",  # 0b0000
    0x1: "Flammable gases",  # 0b0001
    0x2: "Flammable aerosols and aerosols",  # 0b0010
    0x3: "Oxidizing gases",  # 0b0011
    0x4: "Gases under pressure",  # 0b0100
    0x5: "Flammable liquids",  # 0b0101
    0x6: "Flammable solids",  # 0b0110
    0x7: "Self-reactive substance/mixture",  # 0b0111
    0x8: "Pyrophoric liquids. Pyrophoric materials are often water-reactive as well and will ignite when they contact water or humid air.",  # 0b1000
    0x9: "Pyrophoric solids. Pyrophoric materials are often water-reactive as well and will ignite when they contact water or humid air.",  # 0b1001
    0xA: "Self-heating substance/mixture",  # 0b1010
    0xB: "Water-reactive - emits flammable gases",  # 0b1011
    0xC: "Oxidising liquids",  # 0b1100
    0xD: "Oxidising solids",  # 0b1101
    0xE: "Organic peroxides",  # 0b1110
    0xF: "Corrosive to metals"  # 0b1111
}

MatchTable_A18_D32 = {
    0x0: "Biohazard Level 1/4: Often pertains to agents that include viruses and bacteria, this biosafety level requires minimal precaution, such as wearing face masks and maintaining no close contact. The biological hazard examples in the first level include E. coli and other non-infectious bacteria.",  # 0b00
    0x1: "Biohazard Level 2/4: Usually causing severe diseases to humans, the second level classifies agents that can be transmitted through direct contact with infected materials. HIV and hepatitis B are some biological hazard examples that pose moderate risks to humans.",  # 0b01
    0x2: "Biohazard Level 3/4: Mainly through respiratory transmission, pathogens that are highly likely to become airborne can cause serious or lethal diseases to humans. Mycobacterium tuberculosis, the bacteria that causes tuberculosis, is an example of a level-3 biohazard.",  # 0b10
    0x3: "Biohazard Level 4/4: Extremely dangerous pathogens that expose humans to life-threatening diseases, the fourth and last level requires workers to utilize maximum protection and containment. Some biological hazard examples are the Ebola virus and the Lassa virus."  # 0b11
}

MatchTable_A18_D33 = {
    0x0: "Biological agents. These include bacteria, viruses, parasites, and fungi (such as yeasts and molds).",  # 0b00
    0x1: "Biotoxins. These refer to a group of substances with a biological origin that are toxic and poisonous to humans. Often, biotoxins are produced by plants, bacteria, insects, or certain animals, among others. Continuous exposure to these may cause, at the very least, a series of inflammatory reactions throughout the body.",  # 0b01
    0x2: "Blood and blood products. While blood isn't considered a biological hazard, it can still bring potential risks if it's contaminated or its source is in any way infected. Also, blood products such as red blood cells, white blood cells, plasma, tissues, and platelets are also hazardous if not properly handled.",  # 0b10
    0x3: "Environmental specimens. Generally, these refer to plants, soil, or water that potentially contain biological agents (include bacteria, viruses, parasites, and fungi) and biotoxins."  # 0b11
}

MatchTable_A18_D34 = {
    0x0: "PE1 - Mass explosion hazard in which the entire body of explosives explodes as one.",  # 0b00
    0x1: "PE2 - Serious projectile hazard but does not have a mass explosion hazard.",  # 0b01
    0x2: "PE3 - Fire hazard and either a minor blast hazard or a minor projection hazard, or both, but does not have a mass explosion hazard. Explosives which give rise to considerable radiant heat or which burn to produce a minor blast or projection hazard.",  # 0b10
    0x3: "PE4 - Fire or slight explosion hazard, or both, with only local effect. Explosives which present only a low hazard in the event of ignition or initiation, where no significant blast or projection of fragments of appreciable size or range is expected."  # 0b11
}

MatchTable_A18_D35 = {
    0x0: "Anthrax",  # 0b000000
    0x1: "Avian influenza in humans",  # 0b000001
    0x2: "Botulism",  # 0b000010
    0x3: "Brucellosis",  # 0b000011
    0x4: "Campylobacteriosis",  # 0b000100
    0x5: "Chikungunya virus disease",  # 0b000101
    0x6: "Chlamydia infections",  # 0b000110
    0x7: "Cholera",  # 0b000111
    0x8: "COVID-19",  # 0b001000
    0x9: "Creutzfeldt - Jakob Disease-variant (vCJD)",  # 0b001001
    0xA: "Cryptosporidiosis",  # 0b001010
    0xB: "Dengue",  # 0b001011
    0xC: "Diphtheria",  # 0b001100
    0xD: "Echinococcosis",  # 0b001101
    0xE: "Giardiasis",  # 0b001110
    0xF: "Gonorrhoea",  # 0b001111
    0x10: "Hepatitis A",  # 0b010000
    0x11: "Hepatitis B",  # 0b010001
    0x12: "Hepatitis C",  # 0b010010
    0x13: "HIV infection and AIDS",  # 0b010011
    0x14: "Infections with haemophilus influenza group B",  # 0b010100
    0x15: "Influenza including Influenza A(H1N1)",  # 0b010101
    0x16: "Invasive meningococcal disease",  # 0b010110
    0x17: "Invasive pneumococcal disease",  # 0b010111
    0x18: "Legionnaries' disease",  # 0b011000
    0x19: "Leptospirosis",  # 0b011001
    0x1A: "Listeriosis",  # 0b011010
    0x1B: "Lyme neuroborreliosis",  # 0b011011
    0x1C: "Malaria",  # 0b011100
    0x1D: "Measles",  # 0b011101
    0x1E: "Meningoccocal disease, invasive",  # 0b011110
    0x1F: "Mumps",  # 0b011111
    0x20: "Pertussis",  # 0b100000
    0x21: "Plague",  # 0b100001
    0x22: "Pneumoccocal invasive diseases",  # 0b100010
    0x23: "Poliomyelitis",  # 0b100011
    0x24: "Q fever",  # 0b100100
    0x25: "Rabies",  # 0b100101
    0x26: "Rubella",  # 0b100110
    0x27: "Rubella, congenital",  # 0b100111
    0x28: "Salmonellosis",  # 0b101000
    0x29: "Severe Acute Respiratory Syndrome (SARS)",  # 0b101001
    0x2A: "Shiga toxin /verocytotoxin-producing Escherichia coli (STEC/VTEC)",  # 0b101010
    0x2B: "Shigellosis",  # 0b101011
    0x2C: "Smallpox",  # 0b101100
    0x2D: "Syphilis",  # 0b101101
    0x2E: "Syphilis, congenital",  # 0b101110
    0x2F: "Tetanus",  # 0b101111
    0x30: "Tick-borne encephalitis",  # 0b110000
    0x31: "Toxoplasmosis, congenital",  # 0b110001
    0x32: "Trichinellosis",  # 0b110010
    0x33: "Tuberculosis",  # 0b110011
    0x34: "Tularaemia",  # 0b110100
    0x35: "Typhoid and paratyphoid fevers",  # 0b110101
    0x36: "Viral haemorrhagic fevers",  # 0b110110
    0x37: "West Nile virus infection",  # 0b110111
    0x38: "Yellow fever",  # 0b111000
    0x39: "Yersinosis",  # 0b111001
    0x3A: "Zika virus disease",  # 0b111010
    0x3B: "Zika virus disease, congenital",  # 0b111011
    0x3C: "Nosocomial infections",  # 0b111100
    0x3D: "Antimicrobial resistance",  # 0b111101
    0x3E: "unidentified infection",  # 0b111110
    0x3F: "not used",  # 0b111111
}

MatchTable_A18_D36 = {
    0x0: "Scale 1 and Intensity 1",  # 0b000
    0x1: "Scale 1 and Intensity 2",  # 0b001
    0x2: "Scale 1 and Intensity 3",  # 0b010
    0x3: "Scale 2 and Intensity 1",  # 0b011
    0x4: "Scale 2 and Intensity 2",  # 0b100
    0x5: "not used",  # 0b101
    0x6: "not used",  # 0b110
    0x7: "not used",  # 0b111
}
            
        
def _get_msg_A18_earthquake(a18_binary):
    message = ''
    D1 = MatchTable_A18_D1.get(int(a18_binary[0:4],2), "")
    D2 = MatchTable_A18_D2.get(int(a18_binary[4:7],2), "")
    D3 = MatchTable_A18_D3.get(int(a18_binary[7:11],2), "")
    D4 = MatchTable_A18_D4.get(int(a18_binary[11:15],2), "")
    message += "\tMagnitude on Richter Scale : " + D1 + "\n"
    message += "\tSeismic coefficient : " + D2 + "\n"
    message += "\tAzimuth from centre of main ellipse to epicentre :" +str(D3) + "\n"
    message += "\tVector length between centre of main ellipse and epicentre : " + str(D4) + "\n"
    return message
        
def _get_msg_A18_tsunami(a18_binary):
    D5 = MatchTable_A18_D5.get(int(a18_binary[0:3],2), "")
    message = '\tHeight of the wave : '+ D5 + '\n'
    return message
        
def _get_msg_A18_cold_heat(a18_binary):
    D6 = MatchTable_A18_D6.get(int(a18_binary[0:4],2), "")
    message = '\tTemperature range : ' + D6 + '\n'
    return message
        
def _get_msg_A18_hurricane(a18_binary):
    message = ''
    D7 = MatchTable_A18_D7.get(int(a18_binary[0:3],2), "")
    D8 = MatchTable_A18_D8.get(int(a18_binary[3:7],2), "")
    D9 = MatchTable_A18_D9.get(int(a18_binary[7:10],2), "")
    message += "\tHurricane categories : " + D7 + '\n'
    message += "\tWind speed : " + D8 + "\n"
    message += "\tRainfall amounts : " + D9 + "\n"
    return message
        
def _get_msg_A18_typhoon(a18_binary):
    message = ''
    D36 = MatchTable_A18_D36.get(int(a18_binary[0:3],2), "")
    D8 = MatchTable_A18_D8.get(int(a18_binary[3:7],2), "")
    D9 = MatchTable_A18_D9.get(int(a18_binary[7:10],2), "")
    message += "\tTyphoon categories : " + D36 + "\n"
    message += "\tWind speed : " + D8 + "\n"
    message += "\tRainfall amounts : " + D9 + "\n"
    return message
        
def _get_msg_A18_tornado(a18_binary):
    message = ''
    D8 = MatchTable_A18_D8.get(int(a18_binary[0:4],2), "")
    D9 = MatchTable_A18_D9.get(int(a18_binary[4:7],2), "")
    D11 = MatchTable_A18_D11.get(int(a18_binary[7:10],2), "")
    message += "\tWind speed : " + D8 + "\n"
    message += "\tRainfall amounts : " + D9 + "\n"
    message += "\tTornado probability : " + D11 + "\n"
    return message
        
def _get_msg_A18_storm(a18_binary):
    message = ''
    D8 = MatchTable_A18_D8.get(int(a18_binary[0:4],2), "")
    D9 = MatchTable_A18_D9.get(int(a18_binary[4:7],2), "")
    D10 = MatchTable_A18_D10.get(int(a18_binary[7:10],2), "")
    D16 = MatchTable_A18_D16.get(int(a18_binary[10:13],2), "")
    message += "\tWind speed : " + D8 + "\n"
    message += "\tRainfall amounts : " + D9 + "\n"
    message += "\tDamage category : " + D10 + "\n"
    message += "\tLightning intensity : " + D16 + "\n"
    return message
        
def _get_msg_A18_hail(a18_binary):
    message = ''
    D12 = MatchTable_A18_D12.get(int(a18_binary[0:4],2), "")
    message += "\tHail scale : " + D12 + "\n"
    return message
        
def _get_msg_A18_rainfall(a18_binary):
    message = ''
    D9 = MatchTable_A18_D9.get(int(a18_binary[0:3],2), "")
    D13 = MatchTable_A18_D13.get(int(a18_binary[3:7],2), "")
    message += "\tRainfail amounts : " + D9 + "\n"
    message += "\tVisibility : " + D13 + "\n"
    return message
        
def _get_msg_A18_snowfail(a18_binary):
    message = ''
    D14 = MatchTable_A18_D14.get(int(a18_binary[0:5],2), "")
    D13 = MatchTable_A18_D13.get(int(a18_binary[5:9],2), "")
    message += "\tSnow depth : " + D14 + "\n"
    message += "\tVisibility : " + D13 + "\n"
    return message
        
def _get_msg_A18_flood(a18_binary):
    message = ''
    D15 = MatchTable_A18_D15.get(int(a18_binary[0:2],2), "")
    message += "\tFlood severity : " + D15 + "\n"
    return message
        
def _get_msg_A18_lightning(a18_binary):
    message = ''
    D16 = MatchTable_A18_D16.get(int(a18_binary[0:3],2), "")
    message += "\tLightning intensity : " + D16 + "\n"
    return message
        
def _get_msg_A18_frost(a18_binary):
    message = ''
    D8 = MatchTable_A18_D8.get(int(a18_binary[0:4],2), "")
    D6 = MatchTable_A18_D6.get(int(a18_binary[4:8],2), "")
    message += "\tWind speed : " + D8 + "\n"
    message += "\tTemperature range : " + D6 + "\n"
    return message
        
def _get_msg_A18_derecho(a18_binary):
    message = ''
    D8 = MatchTable_A18_D8.get(int(a18_binary[0:4],2), "")
    D9 = MatchTable_A18_D9.get(int(a18_binary[4:7],2), "")
    D16 = MatchTable_A18_D16.get(int(a18_binary[7:10],2), "")
    D11 = MatchTable_A18_D11.get(int(a18_binary[10:13],2), "'")
    message += "\tWind speed : " + D8 + "\n"
    message += '\tRainfall amounts : ' + D9 + '\n'
    message += '\tLightning intensity : ' + D16 + "\n"
    message += "\tTornado probability : " + D11 + "\n"
    return message
        
def _get_msg_A18_fog(a18_binary):
    message = ''
    D17 = MatchTable_A18_D17.get(int(a18_binary[0:3],2), "")
    D13 = MatchTable_A18_D13.get(int(a18_binary[3:7],2), "")
    message += "\tFog level : " + D17 + "\n"
    message += "\tVisibility : " + D13 + "\n"
    return message
        
def _get_msg_A18_blizzard(a18_binary):
    message = ''
    D13 = MatchTable_A18_D13.get(int(a18_binary[0:4],2), "")
    D8 = MatchTable_A18_D8.get(int(a18_binary[4:8],2), "")
    message += "\tVisibility : " + D13 + "\n"
    message += "\tWind speed : " + D8 + "\n"
    return message
        
def _get_msg_A18_drought(a18_binary):
    message = ''
    D18 = MatchTable_A18_D18.get(int(a18_binary[0:2],2), "")
    message += "\tDrought level: " + D18 + "\n"
    return message
        
def _get_msg_A18_avalancherisk(a18_binary):
    message = ''
    D19 = MatchTable_A18_D19.get(int(a18_binary[0:3],2), "")
    message += "\Avalanche warning level : " + D19 + "\n"
    return message
        
def _get_msg_A18_tidalwave(a18_binary):
    message = ''
    D5 = MatchTable_A18_D5.get(int(a18_binary[0:3],2), "")
    message += "\tHeight of the wave : " + D5 + '\n'
    return message
        
def _get_msg_A18_ashfall(a18_binary):
    message = ''
    D20 = MatchTable_A18_D20.get(int(a18_binary[0:3],2), "")
    message += "\tAsh fall amounts : " + D20 + '\n'            
    return message
        
def _get_msg_A18_wind(a18_binary):
    message = ''
    D8 = MatchTable_A18_D8.get(int(a18_binary[0:4],2), "")
    D5 = MatchTable_A18_D5.get(int(a18_binary[4:7],2), "")
    message += "\tWind speed : " + D8 + '\n'            
    message += "\tHeight of the wave : " + D5 + '\n'            
    return message

def _get_msg_A18_solarstorm(a18_binary):
    message = ''
    D21 = MatchTable_A18_D21.get(int(a18_binary[0:3],2), "")
    message += "\tGeomagnetic scale : " + D21 + '\n'            
    return message
        
def _get_msg_A18_terrorism(a18_binary):
    message = ''
    D22 = MatchTable_A18_D22.get(int(a18_binary[0:3],2), "")
    message += "\tTerrorism threat level : " + D22 + '\n'            
    return message

def _get_msg_A18_fire(a18_binary):
    message = ''
    D23 = MatchTable_A18_D23.get(int(a18_binary[0:3],2), "")
    message += "\tFire risk level : " + D23 + '\n'            
    return message
        
def _get_msg_A18_water(a18_binary):
    message = ''
    D24 = MatchTable_A18_D24.get(int(a18_binary[0:3],2), "")
    message += "\tWater quality : " + D24 + '\n'            
    return message
        
def _get_msg_A18_uv(a18_binary):
    message = ''
    D25 = MatchTable_A18_D25.get(int(a18_binary[0:4],2), "")
    message += "\tUV radiation UV index : " + D25 + '\n'            
    return message
        
def _get_msg_A18_pandemia(a18_binary):
    message = ''
    D26 = MatchTable_A18_D26.get(int(a18_binary[0:5],2), "")
    D35 = MatchTable_A18_D35.get(int(a18_binary[5:5+6],2), "")
    message += "\tNumber of cases per 100 000 inhabitants : " + D26 + '\n'            
    message += "\tInfection type : " + D35 + '\n'            
    return message

def _get_msg_A18_noise(a18_binary):
    message = ''
    D27 = MatchTable_A18_D27.get(int(a18_binary[0:4],2), "")
    message += "\tNoise range : " + D27 + '\n'            
    return message

def _get_msg_A18_air(a18_binary):
    message = ''
    D28 = MatchTable_A18_D28.get(int(a18_binary[0:3],2), "")
    message += "\tAir pollution index : " + D28 + '\n'            
    return message

def _get_msg_A18_gas(a18_binary):
    message = ''
    D29 = MatchTable_A18_D29.get(int(a18_binary[0:5],2), "")
    message += "\tOutage estimated duration : " + D29 + '\n'
    return message

def _get_msg_A18_chemical(a18_binary):
    message = ''
    D31 = MatchTable_A18_D31.get(int(a18_binary[0:4],2), "")
    message += "\tHazard class : " + D31 + '\n'            
    return message

def _get_msg_A18_nuclear(a18_binary):
    message = ''
    D30 = MatchTable_A18_D30.get(int(a18_binary[0:4],2), "")
    message += "\tNuclear Event Scale : " + D30 + '\n'
    return message

def _get_msg_A18_biological(a18_binary):
    message = ''
    D32 = MatchTable_A18_D32.get(int(a18_binary[0:2],2), "")
    D33 = MatchTable_A18_D33.get(int(a18_binary[2:4],2), "")
    message += "\tBiohazard level : " + D32 + '\n'            
    message += "\tBiohazard type : " + D33 + '\n'            
    return message

def _get_msg_A18_CBRNE(a18_binary):
    message = ''
    D34 = MatchTable_A18_D34.get(int(a18_binary[0:2],2), "")
    message += "\tExplosive hazard type : " + D34 + '\n'
    return message

def _get_A18_values_B1(a18_binary):
    C1 = MatchTable_A18_C1.get(int(a18_binary[0:3], 2), 9999)
    C2 = MatchTable_A18_C2.get(int(a18_binary[3:6], 2), 9999)
    C3 = MatchTable_A18_C3.get(int(a18_binary[6:9], 2), 9999)
    C4 = MatchTable_A18_C4.get(int(a18_binary[9:12], 2), 9999)
    return C1, C2, C3, C4

def _get_A18_values_B2(a18_binary):
    C5 = MatchTable_A18_C5.get(int(a18_binary[0:7], 2), 9999)
    C6 = MatchTable_A18_C6.get(int(a18_binary[7:14], 2), 9999)
    return C5, C6

def _get_A18_values_B3(a18_binary):
    C7 = int(a18_binary[0:2], 2)
    C8 = MatchTable_A18_C8.get(int(a18_binary[2:5], 2), 9999)
    C9 = MatchTable_A18_C9.get(int(a18_binary[5:10], 2), 9999)
    C10 = MatchTable_A18_C10.get(int(a18_binary[10:15], 2), 9999)
    return C7, C8, C9, C10
    
def _get_A18_message_B1(a18_binary):
    message = ''
    C1, C2, C3, C4 = _get_A18_values_B1(a18_binary)
    message +='\tRefined Latitude of Centre of Main Ellipse : ' + str(format(C1, ".3f")) + "\n"
    message +='\tRefined Longitude of Centre of Main Ellipse : ' + str(format(C2, ".3f")) + "\n"
    message +='\tRefined Length of Semi-Major Axis : ' + str(format(C3, ".3f")) + "\n"
    message +='\tRefined Length of Semi-Minor Axis : ' + str(format(C4, ".3f")) + "\n"
    return message
    
def _get_A18_message_B2(a18_binary):
    message = ''
    C5, C6 = _get_A18_values_B2(a18_binary)
    message +='\tDelta latitude from Ellipse Centre : ' + str(C5) +'\n'
    message +='\tDelta longitude from Ellipse Centre : ' + str(C6) +'\n'
    return message
    
def _get_A18_message_B3(a18_binary):
    message = ''
    C7, C8, C9, C10 = _get_A18_values_B3(a18_binary)
    message += '\tShift of second ellipse centre : '+ str(C7) +'\n'
    message += '\tHomothetic factor of second ellipse : '+ str(C8) +'\n'
    message += '\tBearing angle of second ellipse : '+ str(C9) +'\n'
    message += '\tGuidance library for second ellipse : '+ str(C10) +'\n'
    return message

def _get_A18_message_B4(a18_binary, a4):
    message = ''
    if a4 == 0x24:  # 0b0100100
        message = _get_msg_A18_earthquake(a18_binary)
    elif a4 == 0x2C:  # 0b0101100
        message = _get_msg_A18_tsunami(a18_binary)
    elif a4 == 0x3F or a4 == 0x47:  # 0b0111111 or 0b1000111
        message = _get_msg_A18_cold_heat(a18_binary)
    elif a4 == 0x50:  # 0b1010000
        message = _get_msg_A18_hurricane(a18_binary)
    elif a4 == 0x52:  # 0b1010010
        message = _get_msg_A18_typhoon(a18_binary)
    elif a4 == 0x4F:  # 0b1001111
        message = _get_msg_A18_tornado(a18_binary)
    elif a4 == 0x4D:  # 0b1001101
        message = _get_msg_A18_storm(a18_binary)
    elif a4 == 0x46:  # 0b1000110
        message = _get_msg_A18_hail(a18_binary)
    elif a4 == 0x4A:  # 0b1001010
        message = _get_msg_A18_rainfall(a18_binary)
    elif a4 == 0x4C:  # 0b1001100
        message = _get_msg_A18_snowfail(a18_binary)
    elif a4 == 0x44:  # 0b1000100
        message = _get_msg_A18_flood(a18_binary)
    elif a4 == 0x48:  # 0b1001000
        message = _get_msg_A18_lightning(a18_binary)
    elif a4 == 0x51:  # 0b1010001
        message = _get_msg_A18_frost(a18_binary)
    elif a4 == 0x40:  # 0b1000000
        message = _get_msg_A18_derecho(a18_binary)
    elif a4 == 0x45:  # 0b1000101
        message = _get_msg_A18_fog(a18_binary)
    elif a4 == 0x4B:  # 0b1001011
        message = _get_msg_A18_blizzard(a18_binary)
    elif a4 == 0x41:  # 0b1000001
        message = _get_msg_A18_drought(a18_binary)
    elif a4 == 0x21:  # 0b0100001
        message = _get_msg_A18_avalancherisk(a18_binary)
    elif a4 == 0x2B:  # 0b0101011
        message = _get_msg_A18_tidalwave(a18_binary)
    elif a4 == 0x20:  # 0b0100000
        message = _get_msg_A18_ashfall(a18_binary)
    elif a4 == 0x2F:  # 0b0101111
        message = _get_msg_A18_wind(a18_binary)
    elif a4 == 0x25:  # 0b0100101
        message = _get_msg_A18_solarstorm(a18_binary)
    elif a4 == 0x67:  # 0b1100111
        message = _get_msg_A18_terrorism(a18_binary)
    elif a4 == 0x1B or a4 == 0x1E:  # 0b0011011 or 0b0011110
        message = _get_msg_A18_fire(a18_binary)
    elif a4 == 0x10 or a4 == 0x12 or a4 == 0x15:  # 0b0010000 or 0b0010010 or 0b0010101
        message = _get_msg_A18_water(a18_binary)
    elif a4 == 0x17:  # 0b0010111
        message = _get_msg_A18_uv(a18_binary)
    elif a4 == 0x35 or a4 == 0x33:  # 0b0110101 or 0b0110011
        message = _get_msg_A18_pandemia(a18_binary)
    elif a4 == 0x23:  # 0b0010011
        message = _get_msg_A18_noise(a18_binary)
    elif a4 == 0x0F:  # 0b0001111
        message = _get_msg_A18_air(a18_binary)
    elif a4 == 0x38 or a4 == 0x39 or a4 == 0x37 or a4 == 0x3C:  # 0b0111000 or 0b0111001 or 0b0110111 or 0b0111100
        message = _get_msg_A18_gas(a18_binary)
    elif a4 == 0x05:  # 0b0000101
        message == _get_msg_A18_chemical(a18_binary)
    elif a4 == 0x0B or a4 == 0x09 or a4 == 0x0A:  # 0b0001011 or 0b0001001 or 0b0001010
        message = _get_msg_A18_nuclear(a18_binary)
    elif a4 == 0x04:  # 0b0000100
        message = _get_msg_A18_biological(a18_binary)
    elif a4 == 0x06:  # 0b0000110
        message = _get_msg_A18_CBRNE(a18_binary)

    return message
    
def get_A18(a17, a18, a4):
    message = ''
    if a17 == 0x00:  # 0b00
        message = _get_A18_message_B1(format(a18, "015b")[2:])
    elif a17 == 0x01:  # 0b01
        message = _get_A18_message_B2(format(a18, "015b")[2:])
    elif a17 == 0x02:  # 0b10
        message = _get_A18_message_B3(format(a18, "015b")[2:])
    elif a17 == 0x03:  # 0b11
        message = _get_A18_message_B4(format(a18, "015b")[2:], a4)
    return message
        

def MT44_CAMF_msg_gen(CAMF):
    message = ''
    #A1
    A1 = get_A1(CAMF.A1)
    message += 'A1-Message Type: ' + A1 + '\n'
    #A2
    A2 = get_A2(CAMF.A2)
    message += 'A2-Country/Region Name: ' + A2 + '\n'
    #A3
    A3 = get_A3(CAMF.A2, CAMF.A3)
    message += 'A3-Provider Identifier: ' + A3 + '\n'
    #A4
    A4 = get_A4(CAMF.A4)
    message += 'A4-Hazard Category and Type: ' + A4 + '\n'  
    #A5
    A5 = get_A5(CAMF.A5)
    message += 'A5-Severity: ' + A5 + '\n'     
    #A6
    A6 = get_A6(CAMF.A6)
    message += 'A6-Hazard Onset: Week Number : ' + A6 + ' Week \n'     
    #A7
    A7 = get_A7(CAMF.A7)
    message += 'A7-Hazard Onset: Time of the Week : ' + A7 + '\n'     
    #A8
    A8 = get_A8(CAMF.A8)
    message += 'A8-Hazard Duration : ' + A8 + '\n'
    #A9
    A9 = get_A9(CAMF.A9)
    message += 'A9-Selection of Library : ' + A9 + '\n'      
    #A10
    A10 = get_A10(CAMF.A10)
    message += 'A10-Version of Library : Library version' + A10 + '\n' 
    #Determine the type of DCX message
    DCX_type = get_DCX_type(CAMF.A2, CAMF.A3)
    A11 = get_A11(CAMF.A11, DCX_type, CAMF.A9)
    message += "A11-Guidance to react library : " + A11 + "\n"
    #A12, A13, A14, A15, A16
    if not is_DCX_valid(DCX_type):
        print("Not Supported MT44 Message")
        return ''
    if is_DCX_JAlert(DCX_type):
        message += 'A12 to A18 : Not used\n'
    else:
        message += 'Target Area : Area enclosed in the ellipse indicated by the following parameters\n'
        #A12
        A12 = -90+(180/(2**16-1))*CAMF.A12
        message +="\tA12-Ellipse Centre Latitude : " + str(format(A12,".3f")) + '\n'
        #A13
        A13 = -180+(360/(2**17-1))*CAMF.A13
        message +="\tA13-Ellipse Centre Longitude : " + str(format(A13,".3f")) + '\n'    
        #A14
        A14 = get_A14(CAMF.A14)
        message += '\tA14-Ellipse Semi-Major Axis : ' + str(format(A14,".3f")) +'(km)\n'
        #A15
        A15 = get_A15(CAMF.A15)
        message += '\tA15-Ellipse Semi-Minor Axis : ' + str(format(A15,".3f")) +'(km)\n'
        #A16
        A16 = -90+180/2**6*CAMF.A16
        message +="\tA16-Ellipse Azimuth : " + str(format(A13,".2f")) + '(degrees)\n'
        #A17
        A17 = get_A17(CAMF.A17)
        message += "A17-Main Subject for Specific Settings : " + A17 + "\n"
        #A18
        A18 = get_A18(CAMF.A17, CAMF.A18, CAMF.A4)
        message += "A18-Specific Setting:\n"+ A18 
    
    return message, DCX_type