# CodeAlpha_BasicNetworkSniffer

## Overview
This project is developed as part of the Cyber Security Internship at CodeAlpha. It is a Python-based Network Sniffer designed to capture live network packets and inspect traffic details.

## Features
- Real-time packet sniffing using Scapy.
- Extracts Source IP and Destination IP addresses.
- Protocol identification (TCP, UDP, ICMP).
- Payload data preview for security analysis.

## Requirements
- Python 3.10+
- Npcap (Windows packet capture library)
- Scapy

## How to Run
1. Open terminal as Administrator.
2. Run the sniffer script:
   ```bash
   python sniffer.py