# User Guide for QZSS L1S MT43 & MT44 Message Python Decoder
Copyright (c) 2024 Allystar Technology Co., Ltd.

## Introduction to DC Report Service
The DC Report Service is part of the Quasi-Zenith Satellite System (QZSS) and provides various disaster and crisis management reports. The service ensures timely dissemination of critical information related to natural disasters such as earthquakes, tsunamis, and marine conditions. The messages are transmitted via L1S signals and are designed to assist in disaster prevention and response activities.

### Service Specifications
- **Message Transmission**: DC Reports are transmitted using L1S signals, which are part of the sub-meter level augmentation service (SLAS).
- **Message Types**: The primary message type for disaster information is MT43, covering various disaster categories including marine conditions.
- **Transmission Rate**: Messages are classified based on priority, with "Maximum priority," "Priority," "Regular," and "Training/Test" classifications determining the transmission rate.

### Disaster Categories
The DC Report Service categorizes messages into several disaster types, each associated with a specific code. The categories include:
- **1**: Earthquake Early Warning
- **2**: Hypocenter Information
- **3**: Seismic Intensity Information
- **4**: Nankai Trough Earthquake
- **5**: Tsunami
- **6**: Northwest Pacific Tsunami
- **8**: Volcano
- **9**: Ash Fall
- **10**: Weather
- **11**: Flood
- **12**: Typhoon
- **14**: Marine

### Marine Disaster Reports
For marine-related disasters, the messages include warnings about various hazardous marine conditions such as high waves, strong winds, typhoons, and other marine weather phenomena. The marine disaster category (code 14) ensures that relevant warnings are broadcast to aid maritime safety and disaster preparedness.

## Guide to Decoding QZQSM Messages

The following guide demonstrates how to decode the DC Report messages by using the raw data sent from the Allystar GNSS Receiver.

### Prerequisites
- **Python Installation**: Ensure Python is installed on your system. You can download it from python.org.
- **NMEA File**: Ensure you have a valid NMEA log file containing the $QZQSM messages to decode. The NMEA log file, e.g. `nmea.txt` can be saved by using Satrack.

### Running Procedure
1. **Run the Decoder Script**:
   Execute the Python file `MT43_MT44_decoder.py` using your Python environment.
   ```bash
   python MT43_MT44_decoder.py
   ```

2. **Input NMEA File Path**:
   When prompted, enter the path of the `nmea.txt` file that you want to decode. This file should contain the $QZQSM messages.

3. **Specify Output Path**:
   Enter the desired path for storing the decoded message. This is where the decoded messages for MT43 and MT44 will be written.

4. **Message Decoding**:
   The script will then process the `nmea.txt` file, extract the necessary information from the $QZQSM messages, and decode the messages for MT43 and MT44. The decoded messages will be generated and written into the specified path.

### Detailed Information on MT43 Messages
#### Sentence Format
All output data is interpreted as ASCII characters. The sentence begins with the message header `$QZQSM` followed by various fields. Below is the format for a QZQSM sentence:
```
$QZQSM,<Satellite ID>,<DC Report Message>*<Checksum><CR><LF>
```
- **Message Header**: `$QZQSM`
- **Satellite ID**: 2 characters (e.g., `56, 57, 61`)
- **DC Report Message**: 63 characters
- **Checksum**: 2 characters

#### Example Sentence
```
$QZQSM,55,53AC12345・・・・・・・9ABCDEFC*1F
```

#### Disaster Category Code
MT43 messages include various disaster categories. For Disaster Category 14 (Marine), the message includes warnings related to marine conditions. The structure of these messages is based on the JMA-DC Report formats.

#### Parameter Definitions
Key parameters for MT43 (Marine) messages include:
- **Report Classification (Rc)**: Indicates the priority of the message.
  - 3: Regular
  - 7: Training/Test
- **Disaster Category (Dc)**: Code for marine disaster reports.
  - 14: 防災気象情報(海上)
- **Report Time (At)**: UTC time when JMA issued the information.
  - Month (AtMo): 1-12
  - Day (AtD): 1-31
  - Hour (AtH): 0-23
  - Minute (AtMi): 0-59
- **Information Type (It)**: Type of the information.
  - 0: Issue: 発表
  - 1: Correction: 訂正

### Example Decoding Process
1. **Extract $QZQSM Messages**:
   The script extracts messages that start with `$QZQSM` from the `nmea.txt` file.
   
2. **Decode Message Parameters**:
   Each message is decoded to extract parameters like Report Classification, Disaster Category, Report Time, and Information Type.

3. **Translate to Japanese**:
   The warning messages are translated into Japanese for local understanding.

## Conclusion
This guide provides a straightforward approach to decoding QZQSM messages from an HD8140 GNSS receiver using Python. Adjust the script as necessary to handle different message formats and additional error handling. For more detailed specifications, refer to the QZSS Interface Specification Document.

---

**References**:
- Interface Specification Document: IS-QZSS-DCR-012 
