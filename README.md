# User Guideline for QZSS L1S MT43 & MT44 Message Decoder
## Introduction
This guide will help you decode QZQSM messages sent by the HD8140 GNSS receiver using a Python program. Specifically, it focuses on decoding QZSS L1S MT43 Disaster Category 14 (Marine) type messages and displaying the warning messages in Japanese.
## Prerequisites
Python Installation: Ensure Python is installed on your system. You can download it from python.org.
## Running Procedure
1.	Run the python file MT43_MT44_decoder.py

2.	When prompted, enter the path of the nmea.txt file that you want to decode. This file should contain the $QZQSM messages.

3.	Next, enter the desired path for storing the decoded message. This is the path where the decoded messages for MT43 and MT44 will be written.

4.	The script will then process the nmea.txt file, extract the necessary information from the $QZQSM messages, and decode the messages for MT43 and MT44. The decoded messages will be generated and written into the specified path.
## Conclusion
This guide provides a straightforward approach to decoding QZQSM messages from an HD8140 GNSS receiver using Python.  Adjust the script as necessary to handle different message formats and additional error handling.
