# Honeypot Project

## Overview
This project implements a low-interaction honeypot for monitoring and analyzing potential attacks. 

### Features:
- **Legitimate Site**: Serves on `port 80` for legitimate users.
- **Attacker Site**: Serves on `port 8080` to deceive attackers.
- **Honeypot**: Listens on `port 5000` to capture malicious activities.
- **Honeypot**: Provides fake file system.
- **RealTimeMonitoring**: Provide real time notification using canary token .

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required libraries socket ,paramiko ,threading

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Ritanshu27/Baitbox.git
   cd honeypot-project
