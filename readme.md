# Honeypot Project

## Overview
This project implements a low-interaction honeypot for monitoring and analyzing potential attacks. 

### Features:
- **Legitimate Site**: Serves on `port 80` for legitimate users.
- **Attacker Site**: Serves on `port 8080` to deceive attackers.
- **Honeypot**: Listens on `port 5000` to capture malicious activities.
- **Honeypot**: Provides fake file system.
- **RealTimeMonitoring**: Provide real time notification using canary token .

  To know How the project is working Please check this link to understand the full working of the project.
  -  https://drive.google.com/file/d/1XO4dx6v4vd3WDy-zLG_FYOotpMoon70I/view?usp=sharing

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required libraries socket ,paramiko ,threading

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Ritanshu27/Baitbox.git
   cd honeypot-project
