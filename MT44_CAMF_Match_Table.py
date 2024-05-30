# -*- coding: utf-8 -*-
"""
CAMF Matching Tables 

@author: Allystar Technology Co. Limited
"""

class DCX_Type:
    def __init__(self):
        self.type_table = {
            0:"DCX message (L-Alert)",
            1:"DCX message (J-Alert)",
            2:"DCX message (municipality-transmitted information [tentative name])",
            3:"DCX message (information from organizations outside Japan)"
        }
    
    def get_type_name(self, num):
        return self.type_table.get(num, "INVALID")
    
    def get_DCX_type(self, a2_msg, a3_msg):
        if a2_msg == 'Japan':
            if a3_msg == 'FMMC':
                return 0
            elif a3_msg == "FDMA" or a3_msg == "Related Ministries":
                return 1
            elif a3_msg == 'Municipality':
                return 2
            else:
                return 999
        else:
            return 3
        
    def is_valid(self, type):
        if type in {0, 1, 2, 3}:
            return True
        return False
    
    def is_JAlert(self, type):
        if type == 1:
            return True
        return False

class MatchTable_A1:
    def __init__(self):
        self.match_table = {
            0b00: "Test",
            0b01: "Alert",
            0b10: "Update",
            0b11: "All Clear"
        }

    def get_message_type(self, value):
        return self.match_table.get(value, "Unknown")

class MatchTable_A2():
    def __init__(self):
        self.match_table = {
            0b000000000: "Afghanistan",
            0b000000001: "Albania",
            0b000000010: "Antarctica",
            0b000000011: "Algeria",
            0b000000100: "American Samoa",
            0b000000101: "Andorra",
            0b000000110: "Angola",
            0b000000111: "Antigua and Barbuda",
            0b000001000: "Azerbaijan",
            0b000001001: "Argentina",
            0b000001010: "Australia",
            0b000001011: "Austria",
            0b000001100: "Bahamas (the)",
            0b000001101: "Bahrain",
            0b000001110: "Bangladesh",
            0b000001111: "Armenia",
            0b000010000: "Barbados",
            0b000010001: "Belgium",
            0b000010010: "Bermuda",
            0b000010011: "Bhutan",
            0b000010100: "Bolivia (Plurinational State of)",
            0b000010101: "Bosnia and Herzegovina",
            0b000010110: "Botswana",
            0b000010111: "Bouvet Island",
            0b000011000: "Brazil",
            0b000011001: "Belize",
            0b000011010: "British Indian Ocean Territory (the)",
            0b000011011: "Solomon Islands",
            0b000011100: "Virgin Islands (British)",
            0b000011101: "Brunei Darussalam",
            0b000011110: "Bulgaria",
            0b000011111: "Myanmar",
            0b000100000: "Burundi",
            0b000100001: "Belarus",
            0b000100010: "Cambodia",
            0b000100011: "Cameroon",
            0b000100100: "Canada",
            0b000100101: "Cabo Verde",
            0b000100110: "Cayman Islands (the)",
            0b000100111: "Central African Republic (the)",
            0b000101000: "Sri Lanka",
            0b000101001: "Chad",
            0b000101010: "Chile",
            0b000101011: "China",
            0b000101100: "Taiwan (Province of China)",
            0b000101101: "Christmas Island",
            0b000101110: "Cocos (Keeling) Islands (the)",
            0b000101111: "Colombia",
            0b000110000: "Comoros (the)",
            0b000110001: "Mayotte",
            0b000110010: "Congo (the)",
            0b000110011: "Congo (the Democratic Republic of the)",
            0b000110100: "Cook Islands (the)",
            0b000110101: "Costa Rica",
            0b000110110: "Croatia",
            0b000110111: "Cuba",
            0b000111000: "Cyprus",
            0b000111001: "Czechia",
            0b000111010: "Benin",
            0b000111011: "Denmark",
            0b000111100: "Dominica",
            0b000111101: "Dominican Republic (the)",
            0b000111110: "Ecuador",
            0b000111111: "El Salvador",
            0b001000000: "Equatorial Guinea",
            0b001000001: "Ethiopia",
            0b001000010: "Eritrea",
            0b001000011: "Estonia",
            0b001000100: "Faroe Islands (the)",
            0b001000101: "Falkland Islands (the) [Malvinas]",
            0b001000110: "South Georgia and the South Sandwich Islands",
            0b001000111: "Fiji",
            0b001001000: "Finland",
            0b001001001: "Åland Islands",
            0b001001010: "France",
            0b001001011: "French Guiana",
            0b001001100: "French Polynesia",
            0b001001101: "French Southern Territories (the)",
            0b001001110: "Djibouti",
            0b001001111: "Gabon",
            0b001010000: "Georgia",
            0b001010001: "Gambia (the)",
            0b001010010: "Palestine, State of",
            0b001010011: "Germany",
            0b001010100: "Ghana",
            0b001010101: "Gibraltar",
            0b001010110: "Kiribati",
            0b001010111: "Greece",
            0b001011000: "Greenland",
            0b001011001: "Grenada",
            0b001011010: "Guadeloupe",
            0b001011011: "Guam",
            0b001011100: "Guatemala",
            0b001011101: "Guinea",
            0b001011110: "Guyana",
            0b001011111: "Haiti",
            0b001100000: "Heard Island and McDonald Islands",
            0b001100001: "Holy See (the)",
            0b001100010: "Honduras",
            0b001100011: "Hong Kong",
            0b001100100: "Hungary",
            0b001100101: "Iceland",
            0b001100110: "India",
            0b001100111: "Indonesia",
            0b001101000: "Iran (Islamic Republic of)",
            0b001101001: "Iraq",
            0b001101010: "Ireland",
            0b001101011: "Israel",
            0b001101100: "Italy",
            0b001101101: "Côte d'Ivoire",
            0b001101110: "Jamaica",
            0b001101111: "Japan",
            0b001110000: "Kazakhstan",
            0b001110001: "Jordan",
            0b001110010: "Kenya",
            0b001110011: "Korea (the Democratic People's Republic of)",
            0b001110100: "Korea (the Republic of)",
            0b001110101: "Kuwait",
            0b001110110: "Kyrgyzstan",
            0b001110111: "Lao People's Democratic Republic (the)",
            0b001111000: "Lebanon",
            0b001111001: "Lesotho",
            0b001111010: "Latvia",
            0b001111011: "Liberia",
            0b001111100: "Libya",
            0b001111101: "Liechtenstein",
            0b001111110: "Lithuania",
            0b001111111: "Luxembourg",
            0b010000000: "Macao",
            0b010000001: "Madagascar",
            0b010000010: "Malawi",
            0b010000011: "Malaysia",
            0b010000100: "Maldives",
            0b010000101: "Mali",
            0b010000110: "Malta",
            0b010000111: "Martinique",
            0b010001000: "Mauritania",
            0b010001001: "Mauritius",
            0b010001010: "Mexico",
            0b010001011: "Monaco",
            0b010001100: "Mongolia",
            0b010001101: "Moldova (the Republic of)",
            0b010001110: "Montenegro",
            0b010001111: "Montserrat",
            0b010010000: "Morocco",
            0b010010001: "Mozambique",
            0b010010010: "Oman",
            0b010010011: "Namibia",
            0b010010100: "Nauru",
            0b010010101: "Nepal",
            0b010010110: "Netherlands (the)",
            0b010010111: "Curaçao",
            0b010011000: "Aruba",
            0b010011001: "Sint Maarten (Dutch part)",
            0b010011010: "Bonaire, Sint Eustatius and Saba",
            0b010011011: "New Caledonia",
            0b010011100: "Vanuatu",
            0b010011101: "New Zealand",
            0b010011110: "Nicaragua",
            0b010011111: "Niger (the)",
            0b010100000: "Nigeria",
            0b010100001: "Niue",
            0b010100010: "Norfolk Island",
            0b010100011: "Norway",
            0b010100100: "Northern Mariana Islands (the)",
            0b010100101: "United States Minor Outlying Islands (the)",
            0b010100110: "Micronesia (Federated States of)",
            0b010100111: "Marshall Islands (the)",
            0b010101000: "Palau",
            0b010101001: "Pakistan",
            0b010101010: "Panama",
            0b010101011: "Papua New Guinea",
            0b010101100: "Paraguay",
            0b010101101: "Peru",
            0b010101110: "Philippines (the)",
            0b010101111: "Pitcairn",
            0b010110000: "Poland",
            0b010110001: "Portugal",
            0b010110010: "Guinea-Bissau",
            0b010110011: "Timor-Leste",
            0b010110100: "Puerto Rico",
            0b010110101: "Qatar",
            0b010110110: "Réunion",
            0b010110111: "Romania",
            0b010111000: "Russian Federation (the)",
            0b010111001: "Rwanda",
            0b010111010: "Saint Barthélemy",
            0b010111011: "Saint Helena, Ascension and Tristan da Cunha",
            0b010111100: "Saint Kitts and Nevis",
            0b010111101: "Anguilla",
            0b010111110: "Saint Lucia",
            0b010111111: "Saint Martin (French part)",
            0b011000000: "Saint Pierre and Miquelon",
            0b011000001: "Saint Vincent and the Grenadines",
            0b011000010: "San Marino",
            0b011000011: "Sao Tome and Principe",
            0b011000100: "Saudi Arabia",
            0b011000101: "Senegal",
            0b011000110: "Serbia",
            0b011000111: "Seychelles",
            0b011001000: "Sierra Leone",
            0b011001001: "Singapore",
            0b011001010: "Slovakia",
            0b011001011: "Viet Nam",
            0b011001100: "Slovenia",
            0b011001101: "Somalia",
            0b011001110: "South Africa",
            0b011001111: "Zimbabwe",
            0b011010000: "Spain",
            0b011010001: "South Sudan",
            0b011010010: "Sudan (the)",
            0b011010011: "Western Sahara*",
            0b011010100: "Suriname",
            0b011010101: "Svalbard and Jan Mayen",
            0b011010110: "Eswatini",
            0b011010111: "Sweden",
            0b011011000: "Switzerland",
            0b011011001: "Syrian Arab Republic (the)",
            0b011011010: "Tajikistan",
            0b011011011: "Thailand",
            0b011011100: "Togo",
            0b011011101: "Tokelau",
            0b011011110: "Tonga",
            0b011011111: "Trinidad and Tobago",
            0b011100000: "United Arab Emirates (the)",
            0b011100001: "Tunisia",
            0b011100010: "Turkey",
            0b011100011: "Turkmenistan",
            0b011100100: "Turks and Caicos Islands (the)",
            0b011100101: "Tuvalu",
            0b011100110: "Uganda",
            0b011100111: "Ukraine",
            0b011101000: "North Macedonia",
            0b011101001: "Egypt",
            0b011101010: "United Kingdom of Great Britain and Northern Ireland (the)",
            0b011101011: "Guernsey",
            0b011101100: "Jersey",
            0b011101101: "Isle of Man",
            0b011101110: "Tanzania, the United Republic of",
            0b011101111: "United States of America (the)",
            0b011110000: "Virgin Islands (U.S.)",
            0b011110001: "Burkina Faso",
            0b011110010: "Uruguay",
            0b011110011: "Uzbekistan",
            0b011110100: "Venezuela (Bolivarian Republic of)",
            0b011110101: "Wallis and Futuna",
            0b011110110: "Samoa",
            0b011110111: "Yemen",
            0b011111000: "Zambia"
        }
    
    def is_reserved(self, a2):
        return (a2 in range(0b011111001, 0b111111111+1))
    
    def get_country_name(self, value):
        if self.is_reserved(value):
            return "Reserved"
        return self.match_table.get(value, "Unknown")

class MatchTable_A3:
    def __init__(self):
        self.match_table = {
            0b00000: {
                0b001101111: "Not Used",
                0b000001010: "Not Used",
                0b001000111: "Not Used",
                0b011011011: "Not Used"
            },
            0b00001: {
                0b001101111: "FMMC",
                0b000001010: "National Emergency Management Agency (NEMA)",
                0b001000111: "National Disaster Management Office (NDMO)",
                0b011011011: "Department of Disaster Prevention and Mitigation (DDPM)"
            },
            0b00010: {
                0b001101111: "FDMA",
                0b000001010: "Bureau of Meteorology (BOM)",
                0b001000111: "Fiji Meteorological Service (FMS)",
                0b011011011: "Thai Meteorological Department (TMD)"
            },
            0b00011: {
                0b001101111: "Related Ministries",
                0b000001010: "Australian Climate Service (ACS)",
                0b001000111: "Hydrology Section, Fiji Water Authority (FWA)",
                0b011011011: "National Disaster Warning Center (NDWC)"
            },
            0b00100: {
                0b001101111: "Municipality",
                0b000001010: "Geoscience Australia (GA)",
                0b001000111: "Mineral Resources Department (MRD)",
                0b011011011: "Department of Mineral Resources (DMR)"
            },
            0b00101: {
                0b001101111: "Reserved",
                0b000001010: "Commonwealth Scientific and Industrial Research Organisation (CSIRO)",
                0b001000111: "Fiji Broadcasting Corporation (FBC)",
                0b011011011: "Navy Hydrographic Department, Royal Thai Navy (RTN)"
            },
            0b00110: {
                0b001101111: "Reserved",
                0b000001010: "Australian Bureau of Statistics (ABS)",
                0b001000111: "Reserved",
                0b011011011: "Department of Water Resources (DWR)"
            },
            0b00111: {
                0b001101111: "Reserved",
                0b000001010: "Resilience New South Wales (Resilience NSW)",
                0b001000111: "Reserved",
                0b011011011: "Royal Irrigation Department (RID)"
            },
            0b01000: {
                0b001101111: "Reserved",
                0b000001010: "State Emergency Service New South Wales (SES)",
                0b001000111: "Reserved",
                0b011011011: "Department of Pollution Control (DPC)"
            },
            0b01001: {
                0b001101111: "New South Wales Rural Fire Service (NSW RFS)",
                0b000001010: "Reserved",
                0b001000111: "Geo-Informatics and Space Technology Development Agency (GISTDA)",
                0b011011011: "Reserved"
            },
            0b01010: {
                0b001101111: "Reserved",
                0b000001010: "Joint Australian Tsunami Warning Centre (JATWC)",
                0b001000111: "Reserved",
                0b011011011: "Electricity Generating Authority of Thailand (EGAT)"
            },
            0b01011: {
                0b001101111: "Reserved",
                0b000001010: "Flood Knowledge Centre (FKC)",
                0b001000111: "Reserved",
                0b011011011: "Royal Forest Department (RFD)"
            },
            0b01100: {
                0b001101111: "Reserved",
                0b000001010: "Australian Broadcasting Corporation (ABC)",
                0b001000111: "Reserved",
                0b011011011: "Department of Parks, Wildlife and Plant Conservation (DPWPC)"
            },
            0b01101: {
                0b001101111: "Reserved",
                0b000001010: "Reserved",
                0b001000111: "Reserved",
                0b011011011: "Water Crisis Prevention Center (WCPC)"
            },
            0b01110: {
                0b001101111: "Reserved",
                0b000001010: "Reserved",
                0b001000111: "Reserved",
                0b011011011: "Reserved"
            }
        }

    def is_reserved(self, a2, provider_id):
        return (a2 in {0b001101111, 0b000001010, 0b001000111, 0b011011011}) and (provider_id in range(0b01110 + 1, 0b100000))
    
    def get_provider_name(self, a2, provider_id):
        if provider_id in self.match_table and a2 in self.match_table[provider_id]:
            return self.match_table[provider_id][a2]
        if self.is_reserved(a2, provider_id):
            return "Reserved"
        else:
            return "Unknown Provider"

class MatchTable_A4:
    def __init__(self):
        self.match_table = {
            0b0000000: "not used",
            0b0000001: "Air strike",
            0b0000010: "Attack on IT systems",
            0b0000011: "Attack with nuclear weapons",
            0b0000100: "Biological hazard",
            0b0000101: "Chemical hazard",
            0b0000110: "Explosive hazard",
            0b0000111: "Meteorite impact",
            0b0001000: "Missile attack",
            0b0001001: "Nuclear hazard",
            0b0001010: "Nuclear power station accident",
            0b0001011: "Radiological hazard",
            0b0001100: "Satellite/space re-entry debris",
            0b0001101: "Siren test",
            0b0001110: "Acid rain",
            0b0001111: "Air pollution",
            0b0010000: "Contaminated drinking water",
            0b0010001: "Gas leak",
            0b0010010: "Marine pollution",
            0b0010011: "Noise pollution",
            0b0010100: "Plague of insects",
            0b0010101: "River pollution",            
            0b0010110: "Suspended dust",
            0b0010111: "UV radiation",
            0b0011000: "Conflagration",
            0b0011001: "Fire brigade deployment",
            0b0011010: "Fire gases",
            0b0011011: "Forest fire",
            0b0011100: "Fumes",
            0b0011101: "Odour nuisance",
            0b0011110: "Risk of fire",
            0b0011111: "Structure fire / Industrial fire",
            0b0100000: "Ash fall",
            0b0100001: "Avalanche risk",
            0b0100010: "Crack in the ground/sinkhole",
            0b0100011: "Debris flow",
            0b0100100: "Earthquake",
            0b0100101: "Geomagnetic or solar storm",
            0b0100110: "Glacial ice avalanche",
            0b0100111: "Landslide",
            0b0101000: "Lava flow",
            0b0101001: "Pyroclastic flow",
            0b0101010: "Snowdrifts",
            0b0101011: "Tidal wave",
            0b0101100: "Tsunami",
            0b0101101: "Volcanic mud flow",
            0b0101110: "Volcano eruption",
            0b0101111: "Wind/wave/storm surge",
            0b0110000: "Epizootic",
            0b0110001: "Food safety alert",
            0b0110010: "Health hazard",
            0b0110011: "Pandemic",
            0b0110100: "Pest infestation",
            0b0110101: "Risk of infection",
            0b0110110: "Building collapse",
            0b0110111: "Emergency number outage",
            0b0111000: "Gas supply outage",
            0b0111001: "Outage of IT systems",
            0b0111010: "Power outage",
            0b0111011: "Raw sewage",
            0b0111100: "Telephone line outage",
            0b0111101: "Black Ice",
            0b0111110: "Coastal flooding",
            0b0111111: "Cold wave",
            0b1000000: "Derecho",
            0b1000001: "Drought",
            0b1000010: "Dust storm",
            0b1000011: "Floating ice / icebergs",
            0b1000100: "Flood",
            0b1000101: "Fog",
            0b1000110: "Hail",
            0b1000111: "Heat wave",
            0b1001000: "Lightning",
            0b1001001: "Pollens",
            0b1001010: "Rainfall",
            0b1001011: "Snow storm / blizzard",
            0b1001100: "Snowfall",
            0b1001101: "Storm or thunderstorm",
            0b1001110: "Thawing",
            0b1001111: "Tornado",
            0b1010000: "Tropical cyclone (hurricane)",
            0b1010001: "Wind chill/frost",
            0b1010010: "Tropical cyclone (typhoon)",
            0b1010011: "Dam failure or bursting of a dam",
            0b1010100: "Dike failure or bursting of a dike",
            0b1010101: "Explosive ordnance disposal",
            0b1010110: "Factory accident",
            0b1010111: "Mine hazard",
            0b1011000: "SAFETY - Bomb/ammunition discovery",
            0b1011001: "Demonstration",
            0b1011010: "Hazardous material accident",
            0b1011011: "Life Threatening situation",
            0b1011100: "Major event",
            0b1011101: "Missing person/abduction",
            0b1011110: "Risk of explosion",
            0b1011111: "Safety warning",
            0b1100000: "Undefined flying object",
            0b1100001: "Unidentified animal",
            0b1100010: "Chemical attack",
            0b1100011: "Guerrilla attack",
            0b1100100: "Hijack",
            0b1100101: "Shooting or danger due to weapons",
            0b1100110: "Special forces attack",
            0b1100111: "Terrorism",
            0b1101000: " Aircraft crash",
            0b1101001: "Bridge collapse",
            0b1101010: "Dangerous goods accident",
            0b1101011: "Inland waterway transport accident",
            0b1101100: "Nautical disaster/Maritime/Marine Security",
            0b1101101: "Oil spill",
            0b1101110: "Road traffic incident",
            0b1101111: "Train/rail accident",
            0b1110000: "Tunnel accident",
            0b1110001: "Test alert"
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

    def is_reserved(self, a3):
        return (a3 in range (0b1110010, 0b11111111+1))

    def get_hazard_type(self, a3):
        if self.is_reserved(a3):
            return "Reserved"
        elif a3 in self.match_table:
            return self.match_table[a3]
        else:
            return "Unknown Hazard Type"

class MatchTable_A5:
    def __init__(self):
        self.severity_table = {
            0b00: "Unknown",
            0b01: "Moderate",
            0b10: "Severe",
            0b11: "Extreme"
        }

    def get_severity(self, code):
        return self.severity_table.get(code, "Invalid code")

class MatchTable_A6:
    def __init__(self):
        self.week_table = {
            0b0: "Current",
            0b1: "Next"
        }

    def get_week(self, code):
        return self.week_table.get(code, "Invalid code")    

class MatchTable_A7:
    def __init__(self):
        pass
    
    def is_not_used(self, a7):
        return a7 in {0, range(0b10011101100001, 0b11111111111111+1)}
    
    def get_week_day(self, a7):
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
        
    def get_hour(self, delta):
        hour = delta//60
        if hour == 12:
            return hour, "PM"
        elif hour > 12:
            return hour - 12, "PM"
        elif hour < 12:
            return hour, "AM"
        else:
            return 0, "NULL"
        
    def get_minutes(self, delta):
        minutes = delta % 60
        return minutes
    
    def get_time(self, a7):
        if self.is_not_used(a7):
            return "not used"
        day = self.get_week_day(a7)
        delta = a7 % 1440 - 1
        hour, noon = self.get_hour(delta)
        minutes = self.get_minutes(delta)
        return day + " - " + str(hour) + ":" + str(minutes) + " " + noon

class MatchTable_A8:
    def __init__(self):
        self.duration_table = {
            0b00: "Unknown",
            0b01: "Duration < 6H",
            0b10: "6H <= Duration < 12H",
            0b11: "12H <= Duration < 24H"
        }

    def get_hazard_duration(self, code):
        return self.duration_table.get(code, "Invalid code")        
    
class MatchTable_A9:
    def __init__(self):
        self.library_table = {
            0b0: "International library",
            0b1: "Country/region guidance library"
        }

    def get_library(self, code):
        return self.library_table.get(code, "Invalid code")
    
class MatchTable_A10:
    def __init__(self):
        self.library_version_table = {
            0b000: "#1",
            0b001: "#2",
            0b010: "#3",
            0b011: "#4",
            0b100: "#5",
            0b101: "#6",
            0b110: "#7",
            0b111: "#8"
        }

    def get_library_version(self, code):
        return self.library_version_table.get(code, "Invalid code")    

class MatchTable_A11:
    def __init__(self):
        self.match_table_0_1 = {
            0b00: "",
            0b01: "Stay",
            0b10: "Move to/toward",
            0b11: "Keep away from"
        }
        self.match_table_0_2 = {
            0b00000000: "",
            0b00000001: "Under/inside a solid structure",
            0b00000010: "3rd floor or higher",
            0b00000011: "Underground",
            0b00000100: "Mountain",
            0b00000101: "Water area",
            0b00000110: "Building where chemicals are handled, such as a factory",
            0b00000111: "Cliffs and areas at risk of collapse",
            0b01111111: "Take the best immediate action to save your life.",
            0b11111111: "Take the best immediate action to save your life."
        }
        self.match_table_1_1 = {
            0b00000: "IC-A-01 [empty]",
            0b00001: "IC-A-02 You are in the danger zone, leave the area immediately. Listen to radio or media for directions and information.",
            0b00010: "IC-A-03 You are in the danger zone, leave the area immediately and reach the evacuation point indicated by the area plotted in yellow. Listen to radio or media for directions and information.",
            0b00011: "IC-A-04 Seek shelter in a building immediately. Stay under cover and stay informed.",
            #Missing middle instructions, cannot found
            0b11111: "IC-A-32 Conditions have improved and are no longer expected to meet alert criteria."
        }
        self.match_table_1_2 = {
            0b00000: "IC-B-01 [empty]",
            0b00001: "IC-B-02 Check with the weather services and local authorities for additional information",
            0b00010: "IC-B-03 Find out the location of the information points set up by the authorities on official channels (radio, internet, TV, social networks...)",
            0b00011: "IC-B-04 Sensitive or vulnerable people should not go out unless they must.",
            0b11111: "IC-B-32 This replaces the warning previously in effect for this area."
        }
    
    def get_table_0_1(self, data):
        return self.match_table_0_1.get(data, "")
    
    def get_table_0_2(self, data):
        if data in range(0b00001000, 0b01111110):
            return "reserved"
        elif data in range(0b10000000, 0b11111110):
            return "Reserved for the evacuation action instruction text for J-Alert"
        else:
            return self.match_table_0_2.get(data, "")
    
    def get_table_1_1(self, data):
        return self.match_table_1_1.get(data, "")
    
    def get_table_1_2(self, data):
        return self.match_table_1_2.get(data, "")

    def get_table_0(self, A11):
        msg = ''
        A11_binary = format(A11, "010b")    
        msg += self.get_table_0_1(int(A11_binary[0:2], 2))
        if msg != '':
            msg += ' '
        msg += self.get_table_0_2(int(A11_binary[2:10], 2))
        return msg
        
        
    def get_table_1(self, A11, A9_bit1):
        msg = ""
        if A9_bit1 == 0:    
            A11_binary = format(A11, "010b") 
            msg += self.get_table_1_1(int(A11_binary[0:5], 2))
            if msg != '':
                msg += ' '
            msg += self.get_table_1_2(int(A11_binary[5:10], 2))
        return msg
    
    def get_format(self, A11, DCX_type, A9_bit1 = 999):
        if A11 == 0 and DCX_type == 2:
            return "Not specified (Reference EX2 to EX7.)"
        if DCX_type in {0, 1, 2}:
            return "\"" + self.get_table_0(A11) + "\""
        elif DCX_type == 3:
            return "\"" + self.get_table_1(A11, A9_bit1) + "\""
        else:
            return ""



class MatchTable_A14:
    def __init__(self):
        self.library_version_radius_table = {
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

    def get_radius(self, code):
        return self.library_version_radius_table.get(code, "Invalid radius")

class MatchTable_A15:
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

    def get_radius(self, code):
        return self.match_table.get(code, "Invalid radius")

class MatchTable_A17:
    def __init__(self):
        self.match_table = {
            0b00: "B1 - Improved Resolution of Main Ellipse",
            0b01: "B2 - Position of the Centre of the Hazard",
            0b10: "B3 - Secondary Ellipse Definition",
            0b11: "B4 - Quantitative and detailed information about the Hazard"
        }

    def get_subject(self, code):
        return self.match_table.get(code, "Invalid code")

class MatchTable_A18:
    def __init__(self):
        self.match_table_C1 = {
            0b000: 0.000000,
            0b001: 0.000343,
            0b010: 0.000687,
            0b011: 0.001030,
            0b100: 0.001373,
            0b101: 0.001717,
            0b110: 0.002060,
            0b111: 0.002403
        }
        self.match_table_C2 = {
            0b000: 0.000000000,
            0b001: 0.000343325,
            0b010: 0.000686651,
            0b011: 0.001029976,
            0b100: 0.001373301,
            0b101: 0.001716627,
            0b110: 0.002059952,
            0b111: 0.002403278
        }
        self.match_table_C3 = {
            0b000: 0.000,
            0b001: 0.125,
            0b010: 0.250,
            0b011: 0.375,
            0b100: 0.500,
            0b101: 0.625,
            0b110: 0.750,
            0b111: 0.875
        }
        self.match_table_C4 = {
            0b000: 0.0,
            0b001: 0.125,
            0b010: 0.250,
            0b011: 0.375,
            0b100: 0.500,
            0b101: 0.625,
            0b110: 0.750,
            0b111: 0.875
        }        
        self.match_table_C5 = {
            0b0000000: -10.000000000,
            0b0000001: -9.843750000,
            0b0000010: -9.687500000,
            0b0000011: -9.531250000,
            0b0000100: -9.375000000,
            0b0000101: -9.218750000,
            0b0000110: -9.062500000,
            0b0000111: -8.906250000,
            0b0001000: -8.750000000,
            0b0001001: -8.593750000,
            0b0001010: -8.437500000,
            0b0001011: -8.281250000,
            0b0001100: -8.125000000,
            0b0001101: -7.968750000,
            0b0001110: -7.812500000,
            0b0001111: -7.656250000,
            0b0010000: -7.500000000,
            0b0010001: -7.343750000,
            0b0010010: -7.187500000,
            0b0010011: -7.031250000,
            0b0010100: -6.875000000,
            0b0010101: -6.718750000,
            0b0010110: -6.562500000,
            0b0010111: -6.406250000,
            0b0011000: -6.250000000,
            0b0011001: -6.093750000,
            0b0011010: -5.937500000,
            0b0011011: -5.781250000,
            0b0011100: -5.625000000,
            0b0011101: -5.468750000,
            0b0011110: -5.312500000,
            0b0011111: -5.156250000,
            0b0100000: -5.000000000,
            0b0100001: -4.843750000,
            0b0100010: -4.687500000,
            0b0100011: -4.531250000,
            0b0100100: -4.375000000,
            0b0100101: -4.218750000,
            0b0100110: -4.062500000,
            0b0100111: -3.906250000,
            0b0101000: -3.750000000,
            0b0101001: -3.593750000,
            0b0101010: -3.437500000,
            0b0101011: -3.281250000,
            0b0101100: -3.125000000,
            0b0101101: -2.968750000,
            0b0101110: -2.812500000,
            0b0101111: -2.656250000,
            0b0110000: -2.500000000,
            0b0110001: -2.343750000,
            0b0110010: -2.187500000,
            0b0110011: -2.031250000,
            0b0110100: -1.875000000,
            0b0110101: -1.718750000,
            0b0110110: -1.562500000,
            0b0110111: -1.406250000,
            0b0111000: -1.250000000,
            0b0111001: -1.093750000,
            0b0111010: -0.937500000,
            0b0111011: -0.781250000,
            0b0111100: -0.625000000,
            0b0111101: -0.468750000,
            0b0111110: -0.312500000,
            0b0111111: -0.156250000,
            0b1000000: 0.156250000,
            0b1000001: 0.312500000,
            0b1000010: 0.468750000,
            0b1000011: 0.625000000,
            0b1000100: 0.781250000,
            0b1000101: 0.937500000,
            0b1000110: 1.093750000,
            0b1000111: 1.250000000,
            0b1001000: 1.406250000,
            0b1001001: 1.562500000,
            0b1001010: 1.718750000,
            0b1001011: 1.875000000,
            0b1001100: 2.031250000,
            0b1001101: 2.187500000,
            0b1001110: 2.343750000,
            0b1001111: 2.500000000,
            0b1010000: 2.656250000,
            0b1010001: 2.812500000,
            0b1010010: 2.968750000,
            0b1010011: 3.125000000,
            0b1010100: 3.281250000,
            0b1010101: 3.437500000,
            0b1010110: 3.593750000,
            0b1010111: 3.750000000,
            0b1011000: 3.906250000,
            0b1011001: 4.062500000,
            0b1011010: 4.218750000,
            0b1011011: 4.375000000,
            0b1011100: 4.531250000,
            0b1011101: 4.687500000,
            0b1011110: 4.843750000,
            0b1011111: 5.000000000,
            0b1100000: 5.156250000,
            0b1100001: 5.312500000,
            0b1100010: 5.468750000,
            0b1100011: 5.625000000,
            0b1100100: 5.781250000,
            0b1100101: 5.937500000,
            0b1100110: 6.093750000,
            0b1100111: 6.250000000,
            0b1101000: 6.406250000,
            0b1101001: 6.562500000,
            0b1101010: 6.718750000,
            0b1101011: 6.875000000,
            0b1101100: 7.031250000,
            0b1101101: 7.187500000,
            0b1101110: 7.343750000,
            0b1101111: 7.500000000,
            0b1110000: 7.656250000,
            0b1110001: 7.812500000,
            0b1110010: 7.968750000,
            0b1110011: 8.125000000,
            0b1110100: 8.281250000,
            0b1110101: 8.437500000,
            0b1110110: 8.593750000,
            0b1110111: 8.750000000,
            0b1111000: 8.906250000,
            0b1111001: 9.062500000,
            0b1111010: 9.218750000,
            0b1111011: 9.375000000,
            0b1111100: 9.531250000,
            0b1111101: 9.687500000,
            0b1111110: 9.843750000,
            0b1111111: 10.000000000            
        }
        self.match_table_C6 = {
            0b0000000: -10.000000000,
            0b0000001: -9.843750000,
            0b0000010: -9.687500000,
            0b0000011: -9.531250000,
            0b0000100: -9.375000000,
            0b0000101: -9.218750000,
            0b0000110: -9.062500000,
            0b0000111: -8.906250000,
            0b0001000: -8.750000000,
            0b0001001: -8.593750000,
            0b0001010: -8.437500000,
            0b0001011: -8.281250000,
            0b0001100: -8.125000000,
            0b0001101: -7.968750000,
            0b0001110: -7.812500000,
            0b0001111: -7.656250000,
            0b0010000: -7.500000000,
            0b0010001: -7.343750000,
            0b0010010: -7.187500000,
            0b0010011: -7.031250000,
            0b0010100: -6.875000000,
            0b0010101: -6.718750000,
            0b0010110: -6.562500000,
            0b0010111: -6.406250000,
            0b0011000: -6.250000000,
            0b0011001: -6.093750000,
            0b0011010: -5.937500000,
            0b0011011: -5.781250000,
            0b0011100: -5.625000000,
            0b0011101: -5.468750000,
            0b0011110: -5.312500000,
            0b0011111: -5.156250000,
            0b0100000: -5.000000000,
            0b0100001: -4.843750000,
            0b0100010: -4.687500000,
            0b0100011: -4.531250000,
            0b0100100: -4.375000000,
            0b0100101: -4.218750000,
            0b0100110: -4.062500000,
            0b0100111: -3.906250000,
            0b0101000: -3.750000000,
            0b0101001: -3.593750000,
            0b0101010: -3.437500000,
            0b0101011: -3.281250000,
            0b0101100: -3.125000000,
            0b0101101: -2.968750000,
            0b0101110: -2.812500000,
            0b0101111: -2.656250000,
            0b0110000: -2.500000000,
            0b0110001: -2.343750000,
            0b0110010: -2.187500000,
            0b0110011: -2.031250000,
            0b0110100: -1.875000000,
            0b0110101: -1.718750000,
            0b0110110: -1.562500000,
            0b0110111: -1.406250000,
            0b0111000: -1.250000000,
            0b0111001: -1.093750000,
            0b0111010: -0.937500000,
            0b0111011: -0.781250000,
            0b0111100: -0.625000000,
            0b0111101: -0.468750000,
            0b0111110: -0.312500000,
            0b0111111: -0.156250000,
            0b1000000: 0.156250000,
            0b1000001: 0.312500000,
            0b1000010: 0.468750000,
            0b1000011: 0.625000000,
            0b1000100: 0.781250000,
            0b1000101: 0.937500000,
            0b1000110: 1.093750000,
            0b1000111: 1.250000000,
            0b1001000: 1.406250000,
            0b1001001: 1.562500000,
            0b1001010: 1.718750000,
            0b1001011: 1.875000000,
            0b1001100: 2.031250000,
            0b1001101: 2.187500000,
            0b1001110: 2.343750000,
            0b1001111: 2.500000000,
            0b1010000: 2.656250000,
            0b1010001: 2.812500000,
            0b1010010: 2.968750000,
            0b1010011: 3.125000000,
            0b1010100: 3.281250000,
            0b1010101: 3.437500000,
            0b1010110: 3.593750000,
            0b1010111: 3.750000000,
            0b1011000: 3.906250000,
            0b1011001: 4.062500000,
            0b1011010: 4.218750000,
            0b1011011: 4.375000000,
            0b1011100: 4.531250000,
            0b1011101: 4.687500000,
            0b1011110: 4.843750000,
            0b1011111: 5.000000000,
            0b1100000: 5.156250000,
            0b1100001: 5.312500000,
            0b1100010: 5.468750000,
            0b1100011: 5.625000000,
            0b1100100: 5.781250000,
            0b1100101: 5.937500000,
            0b1100110: 6.093750000,
            0b1100111: 6.250000000,
            0b1101000: 6.406250000,
            0b1101001: 6.562500000,
            0b1101010: 6.718750000,
            0b1101011: 6.875000000,
            0b1101100: 7.031250000,
            0b1101101: 7.187500000,
            0b1101110: 7.343750000,
            0b1101111: 7.500000000,
            0b1110000: 7.656250000,
            0b1110001: 7.812500000,
            0b1110010: 7.968750000,
            0b1110011: 8.125000000,
            0b1110100: 8.281250000,
            0b1110101: 8.437500000,
            0b1110110: 8.593750000,
            0b1110111: 8.750000000,
            0b1111000: 8.906250000,
            0b1111001: 9.062500000,
            0b1111010: 9.218750000,
            0b1111011: 9.375000000,
            0b1111100: 9.531250000,
            0b1111101: 9.687500000,
            0b1111110: 9.843750000,
            0b1111111: 10.000000000            
            
        }
        self.match_table_C8 = {
            0b000: 0.25,
            0b001: 0.5,
            0b010: 0.75,
            0b011: 1,
            0b100: 1.25,
            0b101: 1.5,
            0b110: 1.75,
            0b111: 2
        }
        self.match_table_C9 = {
            0b00000: 0,
            0b00001: 11.25,
            0b00010: 22.5,
            0b00011: 33.75,
            0b00100: 45,
            0b00101: 56.25,
            0b00110: 67.5,
            0b00111: 78.75,
            0b01000: 90,
            0b01001: 101.25,
            0b01010: 112.5,
            0b01011: 123.75,
            0b01100: 135,
            0b01101: 146.25,
            0b01110: 157.5,
            0b01111: 168.75,
            0b10000: 180,
            0b10001: 191.25,
            0b10010: 202.5,
            0b10011: 213.75,
            0b10100: 225,
            0b10101: 236.25,
            0b10110: 247.5,
            0b10111: 258.75,
            0b11000: 270,
            0b11001: 281.25,
            0b11010: 292.5,
            0b11011: 303.75,
            0b11100: 315,
            0b11101: 326.25,
            0b11110: 337.5,
            0b11111: 348.75
        }
        self.match_table_C10 = {
            0b00000: 'IC-C-01',
            0b00001: 'IC-C-02',
            0b00010: 'IC-C-03',
            0b00011: 'IC-C-04',
            0b00100: 'IC-C-05',
            0b00101: 'IC-C-06',
            0b00110: 'IC-C-07',
            0b00111: 'IC-C-08',
            0b01000: 'IC-C-09',
            0b01001: 'IC-C-10',
            0b01010: 'IC-C-11',
            0b01011: 'IC-C-12',
            0b01100: 'IC-C-13',
            0b01101: 'IC-C-14',
            0b01110: 'IC-C-15',
            0b01111: 'IC-C-16',
            0b10000: 'IC-C-17',
            0b10001: 'IC-C-18',
            0b10010: 'IC-C-19',
            0b10011: 'IC-C-20',
            0b10100: 'IC-C-21',
            0b10101: 'IC-C-22',
            0b10110: 'IC-C-23',
            0b10111: 'IC-C-24',
            0b11000: 'IC-C-25',
            0b11001: 'IC-C-26',
            0b11010: 'IC-C-27',
            0b11011: 'IC-C-28',
            0b11100: 'IC-C-29',
            0b11101: 'IC-C-30',
            0b11110: 'IC-C-31',
            0b11111: 'IC-C-32'
        }
    
    class MatchTable_A18_B4:
        def __init__(self):
            self.match_table_D1 = {
            0b0000: "1.0-1.9",
            0b0001: "2.0-2.9",
            0b0010: "3.0-3.9",
            0b0011: "4.0-4.9",
            0b0100: "5.0-5.9",
            0b0101: "6.0-6.9",
            0b0110: "7.0-7.9",
            0b0111: "8.0-8.9",
            0b1000: "9.0 and greater"
            }
            self.match_table_D2 = {
            0b000: "2",
            0b001: "3",
            0b010: "4",
            0b011: "5 weak",
            0b100: "5 strong",
            0b101: "6 weak",
            0b110: "6 strong",
            0b111: "7"
            }
            self.match_table_D3 = {
            0b0000: 0,
            0b0001: 22,
            0b0010: 45,
            0b0011: 67,
            0b0100: 90,
            0b0101: 112,
            0b0110: 135,
            0b0111: 157,
            0b1000: 180,
            0b1001: 202,
            0b1010: 225,
            0b1011: 247,
            0b1100: 270,
            0b1101: 292,
            0b1110: 315,
            0b1111: 337
            }
            self.match_table_D4 = {
            0b0000: 0.25,
            0b0001: 0.5,
            0b0010: 0.75,
            0b0011: 1.0,
            0b0100: 2.0,
            0b0101: 3.0,
            0b0110: 5.0,
            0b0111: 10.0,
            0b1000: 20.0,
            0b1001: 30.0,
            0b1010: 40.0,
            0b1011: 50.0,
            0b1100: 70.0,
            0b1101: 100.0,
            0b1110: 150.0,
            0b1111: 200.0
            }
            self.match_table_D5 = {
            0b000: "H ≤ 0.5",
            0b001: "0.5 < H ≤ 1.0",
            0b010: "1.0 < H ≤ 1.5",
            0b011: "1.5 < H ≤ 2.0",
            0b100: "2.0 < H ≤ 3.0",
            0b101: "3.0 < H ≤ 5.0",
            0b110: "5.0 < H ≤ 10.0",
            0b111: "H > 10.0"
            }
            self.match_table_D6 = {
            0b0000: "T ≤ -30",
            0b0001: "-30 < T ≤ -25",
            0b0010: "-25 < T ≤ -20",
            0b0011: "-20 < T ≤ -15",
            0b0100: "-15 < T ≤ -10",
            0b0101: "-10 < T ≤ -5",
            0b0110: "-5 < T ≤ 0",
            0b0111: "0 < T ≤ 5",
            0b1000: "5 < T ≤ 10",
            0b1001: "10 < T ≤ 15",
            0b1010: "15 < T ≤ 20",
            0b1011: "20 < T ≤ 25",
            0b1100: "25 < T ≤ 30",
            0b1101: "30 < T ≤ 35",
            0b1110: "35 < T ≤ 45",
            0b1111: "T > 45"
            }
            self.match_table_D7 = {
            0b000: ("Category 1/5 hurricane: Very dangerous winds will produce some damage. Winds range from 120 to "
                    "150 km/h. Falling debris could strike people, livestock and pets, and older mobile homes could be "
                    "destroyed. Protected glass windows will generally make it through the hurricane without major "
                    "damage. Frame homes, apartments and shopping centres may experience some damage, and "
                    "snapped power lines could result in short-term power outages."),
            0b001: ("Category 2/5 hurricane: Extremely dangerous winds will cause extensive damage. Winds range "
                    "between 150 and 180 km/h. There is a bigger risk of injury or death to people, livestock and pets from "
                    "flying debris. Older mobile homes will likely be destroyed, and debris can ruin newer mobile homes, "
                    "too. Frame homes, apartment buildings and shopping centres may see major roof and siding damage, "
                    "and many trees will be uprooted. Residents should expect near total power loss after a Category 2 "
                    "hurricane, with outages lasting anywhere from a few days to a few weeks."),
            0b010: ("Category 3/5 hurricane: Devastating damage will occur. In a Category 3 hurricane, winds range from "
                    "180 to 210 km/h. There is a high risk of injury or death to people, livestock and pets from flying and "
                    "falling debris. Nearly all older mobile homes will be destroyed, and most new ones will experience "
                    "significant damage. Even well-built frame homes, apartments and industrial buildings will likely "
                    "experience major damage, and the storm will uproot many trees that may block roads. Electricity and "
                    "water will likely be unavailable for several days to a few weeks after the storm."),
            0b011: ("Category 4/5 hurricane: Catastrophic damage will occur. During a Category 4 hurricane, winds range "
                    "from 210 to 250 km/h. At these speeds, falling and flying debris poses a very high risk of injury or "
                    "death to people, pets and livestock. Again, most mobile homes will be destroyed, even newer ones. "
                    "Some frame homes may totally collapse, while well-built homes will likely see severe damage to their "
                    "roofs, and apartment buildings can experience damage to upper floors. A Category 4 hurricane will " 
                    "blow out most windows on high-rise buildings, uproot most trees and will likely down many power "
                    "lines."),
            0b100: ("Category 5/5 hurricane: Catastrophic damage will occur. In a Category 5 hurricane, the highest "
                    "category hurricane, winds are 250 km/h or higher. People, livestock and pets can be in danger from "
                    "flying debris, even indoors. Most mobile homes will be completely destroyed, and a high percentage "
                    "of frame homes will be destroyed. Commercial buildings with wood roofs will experience severe "
                    "damage, metal buildings may collapse and high-rise windows will nearly all be blown out. A Category "
                    "5 hurricane is likely to uproot most trees and ruin most power poles. People should expect long-term "
                    "water shortages and power outages.")
            }
            self.match_table_D8 = {
            0b0000: "Beaufort 0. 0 km/h < v < 1 km/h - Calm",
            0b0001: "Beaufort 1. 1 km/h < v < 5 km/h - Light Air",
            0b0010: "Beaufort 2. 6 km/h < v < 11 km/h - Light Breeze",
            0b0011: "Beaufort 3. 12 km/h < v < 19 km/h - Gentle Breeze",
            0b0100: "Beaufort 4. 20 km/h < v < 30 km/h - Moderate Breeze",
            0b0101: "Beaufort 5. 31 km/h < v < 39 km/h - Fresh Breeze",
            0b0110: "Beaufort 6. 40 km/h < v < 50 km/h - Strong Breeze",
            0b0111: "Beaufort 7. 51 km/h < v < 61 km/h - Near Gale",
            0b1000: "Beaufort 8. 62 km/h < v < 74 km/h - Gale",
            0b1001: "Beaufort 9. 75 km/h < v < 88 km/h - Strong Gale",
            0b1010: "Beaufort 10. 89 km/h < v < 102 km/h - Storm",
            0b1011: "Beaufort 11. 103 km/h < v < 117 km/h - Violent Storm",
            0b1100: "Beaufort 12. V > 118 km/h - Hurricane",
            0b1101: "not used",
            0b1110: "not used",
            0b1111: "not used"
            }
            self.match_table_D9 = {
            0b000: "p ≤ 2.5 mm/h",
            0b001: "2.5 < p ≤ 7.5 mm/h",
            0b010: "7.5 < p ≤ 10 mm/h",
            0b011: "10 < p ≤ 20 mm/h",
            0b100: "20 < p ≤ 30 mm/h",
            0b101: "30 < p ≤ 50 mm/h",
            0b110: "50 < p ≤ 80 mm/h",
            0b111: "80 < p mm/h"
            }
            self.match_table_D10 = {
            0b000: "Category 1 - Very dangerous winds will produce some damage. Scale 1 and Intensity 1",
            0b001: "Category 2 - Extremely dangerous winds will cause extensive damage. Scale 1 and Intensity 2",
            0b010: "Category 3 - Devastating damage will occur. Scale 1 and Intensity 3",
            0b011: "Category 4 - Catastrophic damage will occur. Scale 2 and Intensity 1",
            0b100: "Category 5 - Catastrophic damage will occur. Scale 2 and Intensity 2",
            0b101: "Category 5 - Catastrophic damage will occur. Scale 3 and Intensity 3",
            0b110: "not used",
            0b111: "not used"
            }
            self.match_table_D11 = {
            0b000: """Non-Threatening
- Threat: No discernible threat to life and property.
- Minimum Action: Listen for forecast changes; review tornado safety rules.
- Potential Impact: None expected; strong wind gusts may still occur.""",
            0b001: """Very Low
- Threat: A very low threat to life and property.
- Minimum Action: Preparations should be made for a very low likelihood (or a 2 to 4% probability) of tornadoes; isolated tornadoes of F0 to F1 intensity possible.
- Potential Impact: The potential for isolated locations to experience minor to moderate tornado damage.""",
            0b010: """Low
- Threat: A low threat to life and property.
- Minimum Action: Preparations should be made for a low likelihood (or a 5 to 14% probability) of tornadoes; scattered tornadoes of F0 to F1 intensity possible.
- Potential Impact: The potential for scattered locations to experience minor to moderate tornado damage.""",
            0b011: """Moderate
- Threat: A moderate threat to life and property.
- Minimum Action: Preparations should be made for a moderate likelihood (or a 15 to 29% probability) of tornadoes; many tornadoes (even families) of F0 to F1 intensity possible.
- Potential Impact: The potential for many locations to experience minor to moderate tornado damage (see below). Some tornadoes may have longer damage tracks.""",
            0b100: """High
- Threat: A high threat to life and property.
- Minimum Action: Preparations should be made for a high likelihood (or a 30 to 44% probability) of tornadoes; scattered tornadoes possible with isolated tornadoes of F2 to F5 intensity also possible.
- Potential Impact: The potential for isolated locations to experience major tornado damage (see below), among scattered locations of minor to moderate tornado damage. Some tornadoes may have longer damage tracks.""",
            0b101: """Extreme
- Threat: An extreme threat to life and property.
- Minimum Action: Preparations should be made for a very high likelihood (or a 45% probability or greater) of tornadoes; many tornadoes (even families) possible with scattered tornadoes of F2 to F5 intensity also possible.
- Potential Impact: The potential for scattered locations to experience major tornado damage (see below), among many locations of minor to moderate tornado damage. Some tornadoes may have longer damage tracks.""",
            0b110: "not used",
            0b111: "not used"
            }
            self.match_table_D12 = {
            0b0000: "H0 - Hard hail. Typical hail diameter of 5 mm. No damage",
            0b0001: "H1 - Potentially damaging. Typical hail diameter of 5-15 mm. Slight general damage to plants, crops",
            0b0010: "H2 - Significant. Typical hail diameter of 10-20 mm. Slight general damage to fruit, crops, vegetation",
            0b0011: "H3 - Severe. Typical hail diameter of 20-30 mm (size of a walnut). Severe damage to fruit and crops, damage to glass and plastic structures, paint and wood scored",
            0b0100: "H4 - Severe. Typical hail diameter of 25-40 mm (size of a squash ball). Widespread glass damage, vehicle bodywork damage",
            0b0101: "H5 - Destructive. Typical hail diameter of 30-50 mm (size of a golf ball). Wholesale destruction of glass, damage to tiled roofs, significant risk of injuries",
            0b0110: "H6 - Destructive. Typical hail diameter of 40-60 mm. Bodywork of grounded aircraft dented, brick walls pitted",
            0b0111: "H7 - Destructive. Typical hail diameter of 50-75 mm (size of a tennis ball). Severe roof damage, risk of serious injuries",
            0b1000: "H8 - Destructive. Typical hail diameter of 60-90 mm (size of a large orange). Severe damage to aircraft bodywork",
            0b1001: "H9 - Super Hailstorms. Typical hail diameter of 75-100 mm (size of a grapefruit). Extensive structural damage. Risk of severe or even fatal injuries to persons caught in the open",
            0b1010: "H10 - Super Hailstorms. Typical hail diameter > 100 mm (size of a melon). Extensive structural damage. Risk of severe or even fatal injuries to persons caught in the open"
            }
            self.match_table_D13 = {
            0b0000: "Dense fog: visibility < 20 m",
            0b0001: "Thick fog: 20 m < visibility < 200 m",
            0b0010: "Moderate fog: 200 m < visibility < 500 m",
            0b0011: "Light fog: 500 m < visibility < 1000 m",
            0b0100: "Thin fog: 1 km < visibility < 2 km",
            0b0101: "Haze: 2 km < visibility < 4 km",
            0b0110: "Light haze: 4 km < visibility < 10 km",
            0b0111: "Clear: 10 km < visibility < 20 km",
            0b1000: "Very clear: 20 km < visibility < 50 km",
            0b1001: "Exceptionally clear: visibility > 50 km"
            }
            self.match_table_D14 = {            0b00000: "0 < daily snow depth ≤ 20 cm",
            0b00001: "20 < daily snow depth ≤ 40 cm",
            0b00010: "40 < daily snow depth ≤ 60 cm",
            0b00011: "60 < daily snow depth ≤ 80 cm",
            0b00100: "80 < daily snow depth ≤ 100 cm",
            0b00101: "100 < daily snow depth ≤ 120 cm",
            0b00110: "120 < daily snow depth ≤ 140 cm",
            0b00111: "140 < daily snow depth ≤ 160 cm",
            0b01000: "160 < daily snow depth ≤ 180 cm",
            0b01001: "180 < daily snow depth ≤ 200 cm",
            0b01010: "200 < daily snow depth ≤ 220 cm",
            0b01011: "220 < daily snow depth ≤ 240 cm",
            0b01100: "240 < daily snow depth ≤ 260 cm",
            0b01101: "260 < daily snow depth ≤ 280 cm",
            0b01110: "280 < daily snow depth ≤ 300 cm",
            0b01111: "300 < daily snow depth ≤ 320 cm",
            0b10000: "320 < daily snow depth ≤ 340 cm",
            0b10001: "340 < daily snow depth ≤ 360 cm",
            0b10010: "360 < daily snow depth ≤ 380 cm",
            0b10011: "380 < daily snow depth ≤ 400 cm",
            0b10100: "400 < daily snow depth ≤ 420 cm",
            0b10101: "420 < daily snow depth ≤ 440 cm",
            0b10110: "440 < daily snow depth ≤ 460 cm",
            0b10111: "460 < daily snow depth ≤ 480 cm",
            0b11000: "480 < daily snow depth ≤ 500 cm",
            0b11001: "500 < daily snow depth ≤ 520 cm",
            0b11010: "520 < daily snow depth ≤ 540 cm",
            0b11011: "540 < daily snow depth ≤ 560 cm",
            0b11100: "560 < daily snow depth ≤ 580 cm",
            0b11101: "580 < daily snow depth ≤ 600 cm",
            0b11110: "daily snow depth > 600 cm",
            0b11111: "not used"
            }
            self.match_table_D15 = {
            0b00: "Minor Flooding - minimal or no property damage, but possibly some public threat.",
            0b01: "Moderate Flooding - some inundation of structures and roads near stream. Some evacuations of people and/or transfer of property to higher elevations.",
            0b10: "Major Flooding - extensive inundation of structures and roads. Significant evacuations of people and/or transfer of property to higher elevations.",
            0b11: "Record Flooding"
            }
            self.match_table_D16 = {
            0b000: "LAL 1 - No thunderstorms",
            0b001: "LAL 2 - Isolated thunderstorms. Light rain will occasionally reach the ground. Lightning is very infrequent, 1 to 5 cloud to ground strikes in a 5-minute period.",
            0b010: "LAL 3 - Widely scattered thunderstorms. Light to moderate rain will reach the ground. Lightning is infrequent, 6 to 10 cloud to ground strikes in a 5-minute period.",
            0b011: "LAL 4 - Scattered thunderstorms. Moderate rain is commonly produced. Lightning is frequent, 11 to 15 cloud to ground strikes in a 5-minute period.",
            0b100: "LAL 5 - Numerous thunderstorms. Rainfall is moderate to heavy. Lightning is frequent and intense, greater than 15 cloud to ground strikes in a 5-minute period.",
            0b101: "LAL 6 - Dry lightning (same as LAL 3 but without rain). This type of lightning has the potential for extreme fire activity and is normally highlighted in fire weather forecasts with a Red Flag Warning."
            }
            self.match_table_D17 = {
            0b000: "Level 1 of 5: Slight fog or Mist. On land, objects appear hazy or blurry. Road and rail traffic are unhindered. On sea, the horizon cannot be seen. Lights and landmarks can be seen at working distances.",
            0b001: "Level 2 of 5: Slight fog. On land, railroad traffic takes additional caution. On sea, lights on passing vessels are generally not distinct at distances under 1 mile. Fog signals are sounded.",
            0b010: "Level 3 of 5: Moderate fog. On land, rail and road traffic is obstructed. On sea, lights on passing vessels are generally not distinct at distances under 1 mile. Fog signals are sounded. On rivers, navigation is unhindered but extra caution is required.",
            0b011: "Level 4 of 5: Moderate fog. On land, rail and road traffic is impeded. On sea, lights on ships and other vessels cannot be seen at distances of 4 miles or less. On rivers, navigation is suspended.",
            0b100: "Level 5 of 5: Thick fog. On land, all traffic is impeded and totally disorganized. On sea, lights on ships and other vessels cannot be seen at distances of 4 miles or less. On rivers, navigation is suspended."
            }
            self.match_table_D18 = {
            0b00: "D1 – Moderate Drought – PDSI = -2.0 to -2.9\n\t\tSome damage to crops, pastures\n\t\tStreams, reservoirs, or wells low, some water shortages developing or imminent\n\t\tVoluntary water-use restrictions requested",
            0b01: "D2 – Severe Drought – PDSI = -3.0 to -3.9\n\t\tCrop or pasture losses likely\n\t\tWater shortages common\n\t\tWater restrictions imposed",
            0b10: "D3 – Extreme Drought – PDSI = -4.0 to -4.9\n\t\tMajor crop/pasture losses\n\t\tWidespread water shortages or restrictions",
            0b11: "D4 – Exceptional Drought – PDSI = -5.0 or less\n\t\tExceptional and widespread crop/pasture losses\n\t\tShortages of water in reservoirs, streams, and wells creating water emergencies"
            }
            self.match_table_D19 = {
            0b000: "1 – Low.\nGenerally stable conditions.\nTriggering is generally possible only from high additional loads in isolated areas of very steep, extreme terrain. Only small and medium natural avalanches are possible.",
            0b001: "2 – Moderate.\nHeightened avalanche conditions on specific terrain features.\nTriggering is possible, primarily from high additional loads, particularly on the indicated steep slopes. Very large natural avalanches are unlikely.",
            0b010: "3 – Considerable.\nDangerous avalanche conditions.\nTriggering is possible, even from low additional loads, particularly on the indicated steep slopes. In certain situations, some large, and in isolated cases very large natural avalanches are possible.",
            0b011: "4 – High.\nVery dangerous avalanche conditions.\nTriggering is likely, even from low additional loads, on many steep slopes. In some cases, numerous large and often very large natural avalanches can be expected.",
            0b100: "5 – Very high.\nExtraordinary avalanche conditions.\nNumerous very large and often extremely large natural avalanches can be expected, even in moderately steep terrain."
            }
            self.match_table_D20 = {
            0b000: "Less than 1 mm ash thickness.\nPossible impact: Will act as an irritant to lungs and eyes. Possible minor damage to vehicles, houses, and equipment caused by fine abrasive ash. Possible contamination of water supplies, particularly roof-fed tank supplies. Dust may affect road visibility and traction for an extended period.",
            0b001: "1-5 mm ash thickness.\nPossible impact: Will act as an irritant to lungs and eyes. Minor damage to vehicles, houses, and equipment caused by fine abrasive ash. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Dust may affect road visibility and traction for an extended period. Roads may need to be cleared to reduce the dust nuisance and prevent storm-water systems from becoming blocked. Possible crop damage. Some livestock may be affected.",
            0b010: "5-100 mm ash thickness.\nPossible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Most buildings will support the ash load but weaker roof structures may collapse at 100 mm ash thickness, particularly if the ash is wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road transport may be halted due to the build-up of ash on roads. Cars still working may soon stop due to clogging of air-filters. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Likely crop damage. Most pastures will be killed by over 50 mm of ash. Some livestock may be affected.",
            0b011: "100-300 mm ash thickness.\nPossible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Buildings that are not cleared of ash will run the risk of roof collapse, especially large flat-roofed structures and if ash becomes wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road transport may be halted due to the build-up of ash on roads. Cars still working may soon stop due to clogging of air-filters. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Likely crop damage. Most pastures will be killed by over 50 mm of ash. Some livestock may be affected.",
            0b100: "> 300 mm ash thickness.\nPossible impact: Will act as an irritant to lungs and eyes. Damage to vehicles, houses, and equipment caused by fine abrasive ash. Buildings that are not cleared of ash will run the risk of roof collapse, especially large flat-roofed structures and if ash becomes wet. Possible contamination of water supplies, particularly roof-fed tank supplies. Electricity and water supplies may be cut or limited. Road unusable until cleared. Rail transport may be forced to stop due to signal failure brought on by short circuiting if ash becomes wet. Heavy kill of vegetation. Livestock and other animals killed or heavily distressed."
            }
            self.match_table_D21 = {
            0b000: "G1 - Minor\nPower systems: Weak power grid fluctuations can occur.\nSpacecraft operations: Minor impact on satellite operations possible.\nOther systems: Migratory animals are affected at this and higher levels; aurora is commonly visible at high latitudes.",
            0b001: "G2 - Moderate\nPower systems: High-latitude power systems may experience voltage alarms, long-duration storms may cause transformer damage.\nSpacecraft operations: Corrective actions to orientation may be required by ground control; possible changes in drag affect orbit predictions.\nOther systems: HF radio propagation can fade at higher latitudes, and aurora has been seen as low as 55° geomagnetic lat.",
            0b010: "G3 - Strong\nPower systems: Voltage corrections may be required, false alarms triggered on some protection devices.\nSpacecraft operations: Surface charging may occur on satellite components, drag may increase on low-Earth-orbit satellites, and corrections may be needed for orientation problems.\nOther systems: Intermittent satellite navigation and low-frequency radio navigation problems may occur, HF radio may be intermittent, and aurora has been seen as low as 50° geomagnetic lat.",
            0b011: "G4 - Severe\nPower systems: Possible widespread voltage control problems and some protective systems will mistakenly trip out key assets from the grid.\nSpacecraft operations: May experience surface charging and tracking problems, corrections may be needed for orientation problems.\nOther systems: Induced pipeline currents affect preventive measures, HF radio propagation sporadic, satellite navigation degraded for hours, low-frequency radio navigation disrupted, and aurora has been seen as low as 45° geomagnetic lat.",
            0b100: "G5 - Extreme\nPower systems: Widespread voltage control problems and protective system problems can occur; some grid systems may experience complete collapse or blackouts. Transformers may experience damage.\nSpacecraft operations: May experience extensive surface charging, problems with orientation, uplink/downlink, and tracking satellites.\nOther systems: Pipeline currents can reach hundreds of amps, HF (high frequency) radio propagation may be impossible in many areas for one to two days, satellite navigation may be degraded for days, low-frequency radio navigation can be out for hours, and aurora has been seen as low as 40° geomagnetic lat."
            }
            self.match_table_D22 = {
            0b000: "Very low threat level. A violent act of terrorism is highly unlikely. Measures are in place to keep the population safe.",
            0b001: "Low threat level. A violent act of terrorism is possible but unlikely. Measures are in place to keep the population safe.",
            0b010: "Medium threat level. A violent act of terrorism could occur. Additional measures are in place to keep the population safe.",
            0b011: "High threat level. A violent act of terrorism is likely. Heightened measures are in place to keep the population safe.",
            0b100: "Critical threat level. A violent act of terrorism is highly likely and could occur imminently. Exceptional measures are in place to keep the population safe."
            }
            self.match_table_D23 = {
            0b000: "Danger level 1/5 (low or none danger). Small fires cannot be entirely ruled out, but require a high energy input. Lightning hardly ever causes a fire. Rate of spread: Generally slow. Characteristics: Surface or crawling fires, crowns of trees are not affected, topsoil does not burn. Fire-fighting: Forest fire is easy to extinguish. Behaviour: Do not carelessly discard cigarettes, tobacco products or lighters.",
            0b001: "Danger level 2/5 (moderate danger). Local fires can start spontaneously. Lightning only rarely causes a conflagration. Rate of spread: Slow to medium. Characteristics: Surface or crawling fires, crowns of trees are rarely affected, topsoil is burnt a little or not at all. Fire-fighting: Forest fire is ordinarily easy to extinguish. Behaviour: Do not carelessly discard cigarettes, tobacco products or lighters. Always watch barbecue fires and immediately extinguish stray sparks.",
            0b010: "Danger level 3/5 (considerable danger): Burning matches and flying sparks from barbecue fires can ignite a fire. Lightning can also trigger widespread fires. Rate of spread: High in open terrain, medium in the forest. Characteristics. Topsoil is partly burnt; individual crown fires are possible. Fire-fighting: Forest fire can be extinguished only by experts using modern equipment. Behaviour: Light barbecue fires only in existing fire places. Always watch the fire and immediately extinguish stray sparks.",
            0b011: "Danger level 4/5 (high danger). Burning matches, flying sparks from barbecue fires and lightning will very probably ignite a fire. Rate of spread: High, including in forests. Characteristics: Intense surface fires can ignite the crowns of individual trees, spotting is possible, burning topsoil. Fire-fighting: Forest fire is difficult to extinguish and commands extensive resources. Behaviour: As a general rule, do not make any fires outdoors. Permanent fire places (concreted base) in locations designated by the authorities can be used with the utmost caution. Do not make fires in strong winds.",
            0b100: "Danger level 5/5 (very high danger). Fires can start at any time. Rate of spread: Very high over a long period. Characteristics: Very intense burning, extensive crown fires, long-distance spotting. Fire-fighting: Forest fire is virtually impossible to extinguish. Behaviour: Do not make any fires outdoors. Follow the instructions and observe the fire bans imposed by the local authorities."
            }
            self.match_table_D24 = {
            0b000: "Excellent water quality",
            0b001: "Good water quality",
            0b010: "Poor water quality",
            0b011: "Very poor water quality",
            0b100: "Suitable for drinking purposes",
            0b101: "Unsuitable for drinking purpose",
            0b110: "not used",
            0b111: "not used"
            }
            self.match_table_D25 = {
            0b0000: "Index 0 - 2 Low. No protection needed. You can safely stay outside using minimal sun protection.",
            0b0001: "Index 3/11 Moderate. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",
            0b0010: "Index 4/11 Moderate. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",
            0b0011: "Index 5/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",
            0b0100: "Index 6/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",
            0b0101: "Index 7/11 High. Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.",
            0b0110: "Index 8/11 Very high. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",
            0b0111: "Index 9/11 Very high. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",
            0b1000: "Index 10/11 Extreme. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin.",
            0b1001: "Index 11/11 Extreme. Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin."
            }
            self.match_table_D26 = {
            0b00000: "0 - 9",
            0b00001: "10 - 20",
            0b00010: "21 - 50",
            0b00011: "51 - 70",
            0b00100: "71 - 100",
            0b00101: "101 - 125",
            0b00110: "126 - 150",
            0b00111: "151 - 175",
            0b01000: "176 - 200",
            0b01001: "201 - 250",
            0b01010: "251 - 300",
            0b01011: "301 - 350",
            0b01100: "351 - 400",
            0b01101: "401 - 450",
            0b01110: "451 - 500",
            0b01111: "501 - 750",
            0b10000: "751 - 1000",
            0b10001: "> 1000",
            0b10010: "> 2000",
            0b10011: "> 3000",
            0b10100: "> 5000"
            }
            self.match_table_D27 = {
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
            self.match_table_D28 = {
            0b000: "Index value 0 - 50. Good. Green. Advisory: None",
            0b001: "Index value 51 - 100. Moderate. Yellow. Unusually sensitive individuals should consider limiting prolonged outdoor exertion",
            0b010: "Index value 101 - 150. Unhealthy for sensitive groups. Orange. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion",
            0b011: "Index value 151 - 200. Unhealthy. Red. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. Everyone else should limit prolonged outdoor exertion.",
            0b100: "Index value 201 - 300. Very unhealthy. Purple. Children, active adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. Everyone else should limit outdoor exertion.",
            0b101: "Index value 301 - 500. Hazardous. Brown. Everyone should avoid all physical activity outdoors."
            }
            self.match_table_D29 = {
            0b00000: "0 < duration < 30 min",
            0b00001: "30 min ≤ duration < 45 min",
            0b00010: "45 min ≤ duration < 1 h",
            0b00011: "1 h ≤ duration < 1h 30min",
            0b00100: "1h 30min ≤ duration < 2 h",
            0b00101: "2 h ≤ duration < 3 h",
            0b00110: "3 h ≤ duration < 4 h",
            0b00111: "4 h ≤ duration < 5 h",
            0b01000: "5 h ≤ duration < 10 h",
            0b01001: "10 h ≤ duration < 24 h",
            0b01010: "24 h ≤ duration < 2 days",
            0b01011: "2 days ≤ duration < 7 days",
            0b01100: "7 days ≤ duration",
            0b01101: "Unknown",
            0b01110: "not used",
            0b01111: "not used",
            0b10000: "not used"
            }
            self.match_table_D30 = {
            0b0000: "Unknown",
            0b0001: "Level 0/7. Deviation. No safety significance",
            0b0010: "Level 1/7. Anomaly. Overexposure in excess of statutory annual limits. Minor problems with safety components with significant defence-in-depth remaining. Low activity lost or stolen radioactive source, device, or transport package.",
            0b0011: "Level 2/7. Incident. Impact on people and environment: Exposure of the public in excess of 10 mSv. Exposure of workers in excess of the statutory annual limits. Impact on radiological barriers and control: Radiation levels in an operating area of more than 50 mSv/h. Significant contamination within the facility into an area not expected by design. Possible cause: Significant failures in safety provisions but with no actual consequences. Found highly radioactive sealed orphan source, device or transport package with safety provisions intact. Inadequate packaging of a highly radioactive sealed source.",
            0b0100: "Level 3/7. Serious incident. Impact on people and environment: Exposure in excess of ten times the statutory annual limit for workers. Non-lethal deterministic health effect (e.g., burns) from radiation. Impact on radiological barriers and control: Exposure rates of more than 1 Sv/h in an operating area. Severe contamination in an area not expected by design, with a low probability of significant public exposure. Possible cause: Near-accident at a nuclear power plant with no safety provisions remaining. Lost or stolen highly radioactive sealed source. Misdelivered highly radioactive sealed source without adequate procedures in place to handle it.",
            0b0101: "Level 4/7. Accident with local consequences. Impact on people and environment: Minor release of radioactive material unlikely to result in implementation of planned countermeasures other than local food controls. Impact on radiological barriers and control: Release of significant quantities of radioactive material within an installation with a high probability of significant public exposure.",
            0b0110: "Level 5/7. Accident with wider consequences. Impact on people and environment: Limited release of radioactive material likely to require implementation of some planned countermeasures. Major health impact from radiation is likely. Impact on radiological barriers and control: Severe damage to the reactor core. Release of large quantities of radioactive material within an installation with a high probability of significant public exposure. This could arise from a major criticality accident or fire.",
            0b0111: "Level 6/7. Serious accident. Impact on people and environment: Significant release of radioactive material likely to require implementation of planned countermeasures.",
            0b1000: "Level 7/7. Major accident. Impact on people and environment: Major release of radioactive material with widespread health and environmental effects requiring implementation of planned and extended countermeasures."
            }
            self.match_table_D31 = {
            0b0000: "Explosives",
            0b0001: "Flammable gases",
            0b0010: "Flammable aerosols and aerosols",
            0b0011: "Oxidizing gases",
            0b0100: "Gases under pressure",
            0b0101: "Flammable liquids",
            0b0110: "Flammable solids",
            0b0111: "Self-reactive substance/mixture",
            0b1000: "Pyrophoric liquids. Pyrophoric materials are often water-reactive as well and will ignite when they contact water or humid air.",
            0b1001: "Pyrophoric solids. Pyrophoric materials are often water-reactive as well and will ignite when they contact water or humid air.",
            0b1010: "Self-heating substance/mixture",
            0b1011: "Water-reactive - emits flammable gases",
            0b1100: "Oxidising liquids",
            0b1101: "Oxidising solids",
            0b1110: "Organic peroxides",
            0b1111: "Corrosive to metals"
            }
            self.match_table_D32 = {
            0b00: "Biohazard Level 1/4: Often pertains to agents that include viruses and bacteria, this biosafety level requires minimal precaution, such as wearing face masks and maintaining no close contact. The biological hazard examples in the first level include E. coli and other non-infectious bacteria.",
            0b01: "Biohazard Level 2/4: Usually causing severe diseases to humans, the second level classifies agents that can be transmitted through direct contact with infected materials. HIV and hepatitis B are some biological hazard examples that pose moderate risks to humans.",
            0b10: "Biohazard Level 3/4: Mainly through respiratory transmission, pathogens that are highly likely to become airborne can cause serious or lethal diseases to humans. Mycobacterium tuberculosis, the bacteria that causes tuberculosis, is an example of a level-3 biohazard.",
            0b11: "Biohazard Level 4/4: Extremely dangerous pathogens that expose humans to life-threatening diseases, the fourth and last level requires workers to utilize maximum protection and containment. Some biological hazard examples are the Ebola virus and the Lassa virus."
            }
            self.match_table_D33 = {
            0b00: "Biological agents. These include bacteria, viruses, parasites, and fungi (such as yeasts and molds).",
            0b01: "Biotoxins. These refer to a group of substances with a biological origin that are toxic and poisonous to humans. Often, biotoxins are produced by plants, bacteria, insects, or certain animals, among others. Continuous exposure to these may cause, at the very least, a series of inflammatory reactions throughout the body.",
            0b10: "Blood and blood products. While blood isn't considered a biological hazard, it can still bring potential risks if it's contaminated or its source is in any way infected. Also, blood products such as red blood cells, white blood cells, plasma, tissues, and platelets are also hazardous if not properly handled.",
            0b11: "Environmental specimens. Generally, these refer to plants, soil, or water that potentially contain biological agents (include bacteria, viruses, parasites, and fungi) and biotoxins."
            }
            self.match_table_D34 = {
            0b00: "PE1 - Mass explosion hazard in which the entire body of explosives explodes as one.",
            0b01: "PE2 - Serious projectile hazard but does not have a mass explosion hazard.",
            0b10: "PE3 - Fire hazard and either a minor blast hazard or a minor projection hazard, or both, but does not have a mass explosion hazard. Explosives which give rise to considerable radiant heat or which burn to produce a minor blast or projection hazard.",
            0b11: "PE4 - Fire or slight explosion hazard, or both, with only local effect. Explosives which present only a low hazard in the event of ignition or initiation, where no significant blast or projection of fragments of appreciable size or range is expected."
            }
            self.match_table_D35 = {
            0b000000: "Anthrax",
            0b000001: "Avian influenza in humans",
            0b000010: "Botulism",
            0b000011: "Brucellosis",
            0b000100: "Campylobacteriosis",
            0b000101: "Chikungunya virus disease",
            0b000110: "Chlamydia infections",
            0b000111: "Cholera",
            0b001000: "COVID-19",
            0b001001: "Creutzfeldt - Jakob Disease-variant (vCJD)",
            0b001010: "Cryptosporidiosis",
            0b001011: "Dengue",
            0b001100: "Diphtheria",
            0b001101: "Echinococcosis",
            0b001110: "Giardiasis",
            0b001111: "Gonorrhoea",
            0b010000: "Hepatitis A",
            0b010001: "Hepatitis B",
            0b010010: "Hepatitis C",
            0b010011: "HIV infection and AIDS",
            0b010100: "Infections with haemophilus influenza group B",
            0b010101: "Influenza including Influenza A(H1N1)",
            0b010110: "Invasive meningococcal disease",
            0b010111: "Invasive pneumococcal disease",
            0b011000: "Legionnaries' disease",
            0b011001: "Leptospirosis",
            0b011010: "Listeriosis",
            0b011011: "Lyme neuroborreliosis",
            0b011100: "Malaria",
            0b011101: "Measles",
            0b011110: "Meningoccocal disease, invasive",
            0b011111: "Mumps",
            0b100000: "Pertussis",
            0b100001: "Plague",
            0b100010: "Pneumoccocal invasive diseases",
            0b100011: "Poliomyelitis",
            0b100100: "Q fever",
            0b100101: "Rabies",
            0b100110: "Rubella",
            0b100111: "Rubella, congenital",
            0b101000: "Salmonellosis",
            0b101001: "Severe Acute Respiratory Syndrome (SARS)",
            0b101010: "Shiga toxin /verocytotoxin-producing Escherichia coli (STEC/VTEC)",
            0b101011: "Shigellosis",
            0b101100: "Smallpox",
            0b101101: "Syphilis",
            0b101110: "Syphilis, congenital",
            0b101111: "Tetanus",
            0b110000: "Tick-borne encephalitis",
            0b110001: "Toxoplasmosis, congenital",
            0b110010: "Trichinellosis",
            0b110011: "Tuberculosis",
            0b110100: "Tularaemia",
            0b110101: "Typhoid and paratyphoid fevers",
            0b110110: "Viral haemorrhagic fevers",
            0b110111: "West Nile virus infection",
            0b111000: "Yellow fever",
            0b111001: "Yersinosis",
            0b111010: "Zika virus disease",
            0b111011: "Zika virus disease, congenital",
            0b111100: "Nosocomial infections",
            0b111101: "Antimicrobial resistance",
            0b111110: "unidentified infection",
            0b111111: "not used"
            }
            self.match_table_D36 = {
            0b000: "Scale 1 and Intensity 1",
            0b001: "Scale 1 and Intensity 2",
            0b010: "Scale 1 and Intensity 3",
            0b011: "Scale 2 and Intensity 1",
            0b100: "Scale 2 and Intensity 2",
            0b101: "not used",
            0b110: "not used",
            0b111: "not used"
            }
            
        def get_values_earthquake(self, a18_binary):
            D1 = self.match_table_D1.get(int(a18_binary[0:4],2), "")
            D2 = self.match_table_D2.get(int(a18_binary[4:7],2), "")
            D3 = self.match_table_D3.get(int(a18_binary[7:11],2), "")
            D4 = self.match_table_D4.get(int(a18_binary[11:15],2), "")
            return D1, D2, D3, D4
        
        def get_msg_earthquake(self, a18_binary):
            message = ''
            D1, D2, D3, D4 = self.get_values_earthquake(a18_binary)
            message += "\tMagnitude on Richter Scale : " + D1 + "\n"
            message += "\tSeismic coefficient : " + D2 + "\n"
            message += "\tAzimuth from centre of main ellipse to epicentre :" +str(D3) + "\n"
            message += "\tVector length between centre of main ellipse and epicentre : " + str(D4) + "\n"
            return message
        
        def get_msg_tsunami(self, a18_binary):
            D5 = self.match_table_D5.get(int(a18_binary[0:3],2), "")
            message = '\tHeight of the wave : '+ D5 + '\n'
            return message
        
        def get_msg_cold_heat(self, a18_binary):
            D6 = self.match_table_D6.get(int(a18_binary[0:4],2), "")
            message = '\tTemperature range : ' + D6 + '\n'
            return message
        
        def get_msg_hurricane(self, a18_binary):
            message = ''
            D7 = self.match_table_D7.get(int(a18_binary[0:3],2), "")
            D8 = self.match_table_D8.get(int(a18_binary[3:7],2), "")
            D9 = self.match_table_D9.get(int(a18_binary[7:10],2), "")
            message += "\tHurricane categories : " + D7 + '\n'
            message += "\tWind speed : " + D8 + "\n"
            message += "\tRainfall amounts : " + D9 + "\n"
            return message
        
        def get_msg_typhoon(self, a18_binary):
            message = ''
            D36 = self.match_table_D36.get(int(a18_binary[0:3],2), "")
            D8 = self.match_table_D8.get(int(a18_binary[3:7],2), "")
            D9 = self.match_table_D9.get(int(a18_binary[7:10],2), "")
            message += "\tTyphoon categories : " + D36 + "\n"
            message += "\tWind speed : " + D8 + "\n"
            message += "\tRainfall amounts : " + D9 + "\n"
            return message
        
        def get_msg_tornado(self, a18_binary):
            message = ''
            D8 = self.match_table_D8.get(int(a18_binary[0:4],2), "")
            D9 = self.match_table_D9.get(int(a18_binary[4:7],2), "")
            D11 = self.match_table_D11.get(int(a18_binary[7:10],2), "")
            message += "\tWind speed : " + D8 + "\n"
            message += "\tRainfall amounts : " + D9 + "\n"
            message += "\tTornado probability : " + D11 + "\n"
            return message
        
        def get_msg_storm(self, a18_binary):
            message = ''
            D8 = self.match_table_D8.get(int(a18_binary[0:4],2), "")
            D9 = self.match_table_D9.get(int(a18_binary[4:7],2), "")
            D10 = self.match_table_D10.get(int(a18_binary[7:10],2), "")
            D16 = self.match_table_D16.get(int(a18_binary[10:13],2), "")
            message += "\tWind speed : " + D8 + "\n"
            message += "\tRainfall amounts : " + D9 + "\n"
            message += "\tDamage category : " + D10 + "\n"
            message += "\tLightning intensity : " + D16 + "\n"
            return message
        
        def get_msg_hail(self, a18_binary):
            message = ''
            D12 = self.match_table_D12.get(int(a18_binary[0:4],2), "")
            message += "\tHail scale : " + D12 + "\n"
            return message
        
        def get_msg_rainfall(self, a18_binary):
            message = ''
            D9 = self.match_table_D9.get(int(a18_binary[0:3],2), "")
            D13 = self.match_table_D13.get(int(a18_binary[3:7],2), "")
            message += "\tRainfail amounts : " + D9 + "\n"
            message += "\tVisibility : " + D13 + "\n"
            return message
        
        def get_msg_snowfail(self, a18_binary):
            message = ''
            D14 = self.match_table_D14.get(int(a18_binary[0:5],2), "")
            D13 = self.match_table_D13.get(int(a18_binary[5:9],2), "")
            message += "\tSnow depth : " + D14 + "\n"
            message += "\tVisibility : " + D13 + "\n"
            return message
        
        def get_msg_flood(self, a18_binary):
            message = ''
            D15 = self.match_table_D15.get(int(a18_binary[0:2],2), "")
            message += "\tFlood severity : " + D15 + "\n"
            return message
        
        def get_msg_lightning(self, a18_binary):
            message = ''
            D16 = self.match_table_D16.get(int(a18_binary[0:3],2), "")
            message += "\tLightning intensity : " + D16 + "\n"
            return message
        
        def get_msg_frost(self, a18_binary):
            message = ''
            D8 = self.match_table_D8.get(int(a18_binary[0:4],2), "")
            D6 = self.match_table_D6.get(int(a18_binary[4:8],2), "")
            message += "\tWind speed : " + D8 + "\n"
            message += "\tTemperature range : " + D6 + "\n"
            return message
        
        def get_msg_derecho(self, a18_binary):
            message = ''
            D8 = self.match_table_D8.get(int(a18_binary[0:4],2), "")
            D9 = self.match_table_D9.get(int(a18_binary[4:7],2), "")
            D16 = self.match_table_D16.get(int(a18_binary[7:10],2), "")
            D11 = self.match_table_D11.get(int(a18_binary[10:13],2), "'")
            message += "\tWind speed : " + D8 + "\n"
            message += '\tRainfall amounts : ' + D9 + '\n'
            message += '\tLightning intensity : ' + D16 + "\n"
            message += "\tTornado probability : " + D11 + "\n"
            return message
        
        def get_msg_fog(self, a18_binary):
            message = ''
            D17 = self.match_table_D17.get(int(a18_binary[0:3],2), "")
            D13 = self.match_table_D13.get(int(a18_binary[3:7],2), "")
            message += "\tFog level : " + D17 + "\n"
            message += "\tVisibility : " + D13 + "\n"
            return message
        
        def get_msg_blizzard(self, a18_binary):
            message = ''
            D13 = self.match_table_D13.get(int(a18_binary[0:4],2), "")
            D8 = self.match_table_D8.get(int(a18_binary[4:8],2), "")
            message += "\tVisibility : " + D13 + "\n"
            message += "\tWind speed : " + D8 + "\n"
            return message
        
        def get_msg_drought(self, a18_binary):
            message = ''
            D18 = self.match_table_D18.get(int(a18_binary[0:2],2), "")
            message += "\tDrought level: " + D18 + "\n"
            return message
        
        def get_msg_avalancherisk(self, a18_binary):
            message = ''
            D19 = self.match_table_D19.get(int(a18_binary[0:3],2), "")
            message += "\Avalanche warning level : " + D19 + "\n"
            return message
        
        def get_msg_tidalwave(self, a18_binary):
            message = ''
            D5 = self.match_table_D5.get(int(a18_binary[0:3],2), "")
            message += "\tHeight of the wave : " + D5 + '\n'
            return message
        
        def get_msg_ashfall(self, a18_binary):
            message = ''
            D20 = self.match_table_D20.get(int(a18_binary[0:3],2), "")
            message += "\tAsh fall amounts : " + D20 + '\n'            
            return message
        
        def get_msg_wind(self, a18_binary):
            message = ''
            D8 = self.match_table_D8.get(int(a18_binary[0:4],2), "")
            D5 = self.match_table_D5.get(int(a18_binary[4:7],2), "")
            message += "\tWind speed : " + D8 + '\n'            
            message += "\tHeight of the wave : " + D5 + '\n'            
            return message
        
        def get_msg_solarstorm(self, a18_binary):
            message = ''
            D21 = self.match_table_D21.get(int(a18_binary[0:3],2), "")
            message += "\tGeomagnetic scale : " + D21 + '\n'            
            return message
        
        def get_msg_terrorism(self, a18_binary):
            message = ''
            D22 = self.match_table_D22.get(int(a18_binary[0:3],2), "")
            message += "\tTerrorism threat level : " + D22 + '\n'            
            return message
        
        def get_msg_fire(self, a18_binary):
            message = ''
            D23 = self.match_table_D23.get(int(a18_binary[0:3],2), "")
            message += "\tFire risk level : " + D23 + '\n'            
            return message
        
        def get_msg_water(self, a18_binary):
            message = ''
            D24 = self.match_table_D24.get(int(a18_binary[0:3],2), "")
            message += "\tWater quality : " + D24 + '\n'            
            return message
        
        def get_msg_uv(self, a18_binary):
            message = ''
            D25 = self.match_table_D25.get(int(a18_binary[0:4],2), "")
            message += "\tUV radiation UV index : " + D25 + '\n'            
            return message
        
        def get_msg_pandemia(self, a18_binary):
            message = ''
            D26 = self.match_table_D26.get(int(a18_binary[0:5],2), "")
            D35 = self.match_table_D35.get(int(a18_binary[5:5+6],2), "")
            message += "\tNumber of cases per 100 000 inhabitants : " + D26 + '\n'            
            message += "\tInfection type : " + D35 + '\n'            
            return message
        
        def get_msg_noise(self, a18_binary):
            message = ''
            D27 = self.match_table_D27.get(int(a18_binary[0:4],2), "")
            message += "\tNoise range : " + D27 + '\n'            
            return message
        
        def get_msg_air(self, a18_binary):
            message = ''
            D28 = self.match_table_D28.get(int(a18_binary[0:3],2), "")
            message += "\tAir pollution index : " + D28 + '\n'            
            return message
        
        def get_msg_gas(self, a18_binary):
            message = ''
            D29 = self.match_table_D29.get(int(a18_binary[0:5],2), "")
            message += "\tOutage estimated duration : " + D29 + '\n'
            return message
        
        def get_msg_chemical(self, a18_binary):
            message = ''
            D31 = self.match_table_D31.get(int(a18_binary[0:4],2), "")
            message += "\tHazard class : " + D31 + '\n'            
            return message
        
        def get_msg_nuclear(self, a18_binary):
            message = ''
            D30 = self.match_table_D30.get(int(a18_binary[0:4],2), "")
            message += "\tNuclear Event Scale : " + D30 + '\n'
            return message
        
        def get_msg_biological(self, a18_binary):
            message = ''
            D32 = self.match_table_D32.get(int(a18_binary[0:2],2), "")
            D33 = self.match_table_D33.get(int(a18_binary[2:4],2), "")
            message += "\tBiohazard level : " + D32 + '\n'            
            message += "\tBiohazard type : " + D33 + '\n'            
            return message
        
        def get_msg_CBRNE(self, a18_binary):
            message = ''
            D34 = self.match_table_D34.get(int(a18_binary[0:2],2), "")
            message += "\tExplosive hazard type : " + D34 + '\n'
            return message
        
        
    matchtable_A18_B4 = MatchTable_A18_B4()
    
    def get_values_B1(self, a18_binary):
        C1 = self.match_table_C1.get(int(a18_binary[0:3], 2), 9999)
        C2 = self.match_table_C2.get(int(a18_binary[3:6], 2), 9999)
        C3 = self.match_table_C3.get(int(a18_binary[6:9], 2), 9999)
        C4 = self.match_table_C4.get(int(a18_binary[9:12], 2), 9999)
        return C1, C2, C3, C4
    
    def get_values_B2(self, a18_binary):
        C5 = self.match_table_C5.get(int(a18_binary[0:7], 2), 9999)
        C6 = self.match_table_C6.get(int(a18_binary[7:14], 2), 9999)
        return C5, C6

    def get_values_B3(self, a18_binary):
        C7 = int(a18_binary[0:2], 2)
        C8 = self.match_table_C8.get(int(a18_binary[2:5], 2), 9999)
        C9 = self.match_table_C9.get(int(a18_binary[5:10], 2), 9999)
        C10 = self.match_table_C10.get(int(a18_binary[10:15], 2), 9999)
        return C7, C8, C9, C10
    
    def get_message_B1(self, a18_binary):
        message = ''
        C1, C2, C3, C4 = self.get_values_B1(a18_binary)
        message +='\tRefined Latitude of Centre of Main Ellipse : ' + str(format(C1, ".3f")) + "\n"
        message +='\tRefined Longitude of Centre of Main Ellipse : ' + str(format(C2, ".3f")) + "\n"
        message +='\tRefined Length of Semi-Major Axis : ' + str(format(C3, ".3f")) + "\n"
        message +='\tRefined Length of Semi-Minor Axis : ' + str(format(C4, ".3f")) + "\n"
        return message
    
    def get_message_B2(self, a18_binary):
        message = ''
        C5, C6 = self.get_values_B2(a18_binary)
        message +='\tDelta latitude from Ellipse Centre : ' + str(C5) +'\n'
        message +='\tDelta longitude from Ellipse Centre : ' + str(C6) +'\n'
        return message
    
    def get_message_B3(self, a18_binary):
        message = ''
        C7, C8, C9, C10 = self.get_message_B3(a18_binary)
        message += '\tShift of second ellipse centre : '+ str(C7) +'\n'
        message += '\tHomothetic factor of second ellipse : '+ str(C8) +'\n'
        message += '\tBearing angle of second ellipse : '+ str(C9) +'\n'
        message += '\tGuidance library for second ellipse : '+ str(C10) +'\n'
        return message

    def get_message_B4(self, a18_binary, a4):
        message = ''
        if a4 == 0b0100100:
            message = self.matchtable_A18_B4.get_msg_earthquake(a18_binary)
        elif a4 == 0b0101100:
            message = self.matchtable_A18_B4.get_msg_tsunami(a18_binary)
        elif a4 == 0b0111111 or a4 == 0b1000111:
            message = self.matchtable_A18_B4.get_msg_cold_heat(a18_binary)
        elif a4 == 0b1010000:
            message = self.matchtable_A18_B4.get_msg_hurricane(a18_binary)
        elif a4 == 0b1010010:
            message = self.matchtable_A18_B4.get_msg_typhoon(a18_binary)
        elif a4 == 0b1001111:
            message = self.matchtable_A18_B4.get_msg_tornado(a18_binary)
        elif a4 == 0b1001101:
            message = self.matchtable_A18_B4.get_msg_storm(a18_binary)
        elif a4 == 0b1000110:
            message = self.matchtable_A18_B4.get_msg_hail(a18_binary)
        elif a4 == 0b1001010:
            message = self.matchtable_A18_B4.get_msg_rainfall(a18_binary)
        elif a4 == 0b1001100:
            message = self.matchtable_A18_B4.get_msg_snowfail(a18_binary)
        elif a4 == 0b1000100:
            message = self.matchtable_A18_B4.get_msg_flood(a18_binary)
        elif a4 == 0b1001000:
            message = self.matchtable_A18_B4.get_msg_lightning(a18_binary)
        elif a4 == 0b1010001:
            message = self.matchtable_A18_B4.get_msg_frost(a18_binary)
        elif a4 == 0b1000000:
            message = self.matchtable_A18_B4.get_msg_derecho(a18_binary)
        elif a4 == 0b1000101:
            message = self.matchtable_A18_B4.get_msg_fog(a18_binary)
        elif a4 == 0b1001011:
            message = self.matchtable_A18_B4.get_msg_blizzard(a18_binary)
        elif a4 == 0b1000001:
            message = self.matchtable_A18_B4.get_msg_drought(a18_binary)
        elif a4 == 0b0100001:
            message = self.matchtable_A18_B4.get_msg_avalancherisk(a18_binary)
        elif a4 == 0b0101011:
            message = self.matchtable_A18_B4.get_msg_tidalwave(a18_binary)
        elif a4 == 0b0100000:
            message = self.matchtable_A18_B4.get_msg_ashfall(a18_binary)
        elif a4 == 0b0101111:
            message = self.matchtable_A18_B4.get_msg_wind(a18_binary)
        elif a4 == 0b0100101:
            message = self.matchtable_A18_B4.get_msg_solarstorm(a18_binary)
        elif a4 == 0b1100111:
            message = self.matchtable_A18_B4.get_msg_terrorism(a18_binary)
        elif a4 == 0b0011011 or a4 == 0b0011110:
            message = self.matchtable_A18_B4.get_msg_fire(a18_binary)
        elif a4 == 0b0010000 or a4 == 0b0010010 or a4 == 0b0010101:
            message = self.matchtable_A18_B4.get_msg_water(a18_binary)
        elif a4 == 0b0010111:
            message = self.matchtable_A18_B4.get_msg_uv(a18_binary)
        elif a4 == 0b0110101 or a4 == 0b0110011:
            message = self.matchtable_A18_B4.get_msg_pandemia(a18_binary)
        elif a4 == 0b0010011:
            message = self.matchtable_A18_B4.get_msg_noise(a18_binary)
        elif a4 == 0b0001111:
            message = self.matchtable_A18_B4.get_msg_air(a18_binary)
        elif a4 == 0b0111000 or a4 == 0b0111001 or a4 == 0b0110111 or a4 == 0b0111100:
            message = self.matchtable_A18_B4.get_msg_gas(a18_binary)
        elif a4 == 0b0000101:
            message == self.matchtable_A18_B4.get_msg_chemical(a18_binary)
        elif a4 == 0b0001011 or a4 == 0b0001001 or a4 == 0b0001010:
            message = self.matchtable_A18_B4.get_msg_nuclear(a18_binary)
        elif a4 == 0b0000100:
            message = self.matchtable_A18_B4.get_msg_biological(a18_binary)
        elif a4 == 0b0000110:
            message = self.matchtable_A18_B4.get_msg_CBRNE(a18_binary)

        return message
    
    def get_message(self, a17, a18, a4):
        message = ''
        if a17 == 0b00:
            message = self.get_message_B1(format(a18, "015b")[2:])
        elif a17 == 0b01:
            message = self.get_message_B2(format(a18, "015b")[2:])
        elif a17 == 0b10:
            message = self.get_message_B3(format(a18, "015b")[2:])
        elif a17 == 0b11:
            message = self.get_message_B4(format(a18, "015b")[2:], a4)
        return message
        
        
        
    




matchtable_A1 = MatchTable_A1()
matchtable_A2 = MatchTable_A2()
matchtable_A3 = MatchTable_A3()
matchtable_A4 = MatchTable_A4()
matchtable_A5 = MatchTable_A5()
matchtable_A6 = MatchTable_A6()
matchtable_A7 = MatchTable_A7()
matchtable_A8 = MatchTable_A8()
matchtable_A9 = MatchTable_A9()
matchtable_A10 = MatchTable_A10()
matchtable_A11 = MatchTable_A11()
DCX = DCX_Type()
matchtable_A14 = MatchTable_A14()
matchtable_A15 = MatchTable_A15()
matchtable_A17 = MatchTable_A17()
matchtable_A18 = MatchTable_A18()


def MT44_CAMF_msg_gen(CAMF):
    message = ''
    #A1
    A1 = matchtable_A1.get_message_type(CAMF.A1)
    message += 'A1-Message Type: ' + A1 + '\n'
    #A2
    A2 = matchtable_A2.get_country_name(CAMF.A2)
    message += 'A2-Country/Region Name: ' + A2 + '\n'
    #A3
    A3 = matchtable_A3.get_provider_name(CAMF.A2, CAMF.A3)
    message += 'A3-Provider Identifier: ' + A3 + '\n'
    #A4
    A4 = matchtable_A4.get_hazard_type(CAMF.A4)
    message += 'A4-Hazard Category and Type: ' + A4 + '\n'  
    #A5
    A5 = matchtable_A5.get_severity(CAMF.A5)
    message += 'A5-Severity: ' + A5 + '\n'     
    #A6
    A6 = matchtable_A6.get_week(CAMF.A6)
    message += 'A6-Hazard Onset: Week Number : ' + A6 + ' Week \n'     
    #A7
    A7 = matchtable_A7.get_time(CAMF.A7)
    message += 'A7-Hazard Onset: Time of the Week : ' + A7 + '\n'     
    #A8
    A8 = matchtable_A8.get_hazard_duration(CAMF.A8)
    message += 'A8-Hazard Duration : ' + A8 + '\n'
    #A9
    A9 = matchtable_A9.get_library(CAMF.A9)
    message += 'A9-Selection of Library : ' + A9 + '\n'      
    #A10
    A10 = matchtable_A10.get_library_version(CAMF.A10)
    message += 'A10-Version of Library : LIbrary version' + A10 + '\n' 
    #Determine the type of DCX message
    DCX_type = DCX.get_DCX_type(A2, A3)
    A11 = matchtable_A11.get_format(CAMF.A11, DCX_type, CAMF.A9)
    message += "A11-Guidance to react library : " + A11 + "\n"
    #A12, A13, A14, A15, A16
    if not DCX.is_valid(DCX_type):
        print("Not Supported MT44 Message")
        return ''
    if DCX.is_JAlert(DCX_type):
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
        A14 = matchtable_A14.get_radius(CAMF.A14)
        message += '\tA14-Ellipse Semi-Major Axis : ' + str(format(A14,".3f")) +'(km)\n'
        #A15
        A15 = matchtable_A15.get_radius(CAMF.A15)
        message += '\tA15-Ellipse Semi-Minor Axis : ' + str(format(A15,".3f")) +'(km)\n'
        #A16
        A16 = -90+180/2**6*CAMF.A16
        message +="\tA16-Ellipse Azimuth : " + str(format(A13,".2f")) + '(degrees)\n'
        #A17
        A17 = matchtable_A17.get_subject(CAMF.A17)
        message += "A17-Main Subject for Specific Settings : " + A17 + "\n"
        #A18
        A18 = matchtable_A18.get_message(CAMF.A17, CAMF.A18, CAMF.A4)
        message += "A18-Specific Setting:\n"+ A18 
    
    
    
    
    
    
    return message, DCX_type